#!/usr/bin/env python3
"""Configure the ChatGPT bridge and initialize user-owned continuity state."""

from __future__ import annotations

import argparse
import atexit
import hashlib
import json
import os
import re
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = re.compile(r"^[A-Za-z0-9_.-]+$")
SHA256_HEX = re.compile(r"^[0-9a-f]{64}$")
TEMPLATE_FIELD = re.compile(r"\{\{([A-Z0-9_]+)\}\}")
BRIDGE_IDENTITY_HEADER = re.compile(
    r"\AWork from the present\. Act directly when the conversation and working set "
    r"suffice; a new chat alone does not require a boot\.\r?\n\r?\n"
    r"User-owned kernel (?:repository|instance):\s*"
    r"([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\.\s*(?:\r?\n|$)"
)
INSTANCE_LOCK_NAME = ".INSTANCE.write.lock"
CANONICAL_UPSTREAM = "https://github.com/GrazianoGuiducci/kernel_chat"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Configure a user-owned kernel_chat instance."
    )
    parser.add_argument("--github-user", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--project-name")
    parser.add_argument("--project-source")
    parser.add_argument(
        "--replace-adapter",
        action="store_true",
        help="Replace the local configured adapter for the existing instance identity; does not change installed host instructions.",
    )
    parser.add_argument(
        "--preview-adapter",
        action="store_true",
        help="Print the candidate adapter without writing adapter or state files.",
    )
    parser.add_argument(
        "--replace-state",
        action="store_true",
        help="Replace state/CURRENT.md and state/SOURCES.md if they exist.",
    )
    parser.add_argument(
        "--refresh-instance",
        action="store_true",
        help="Refresh package/available-bridge identity while preserving configured artifact identity/provenance and observations.",
    )
    parser.add_argument(
        "--confirm-host-installation",
        action="store_true",
        help="Record operator confirmation for the already-reconciled current configured bridge; mutates INSTANCE only.",
    )
    parser.add_argument(
        "--expected-bridge-sha256",
        help="Exact configured bridge digest that was delivered for the operator action being confirmed.",
    )
    return parser.parse_args()


def validate_slug(value: str, label: str) -> None:
    if not SLUG.fullmatch(value):
        raise SystemExit(f"{label} contains unsupported characters: {value!r}")


def render(path: Path, replacements: dict[str, str]) -> str:
    """Render template fields once; inserted user data is never reinterpreted."""

    text = path.read_text(encoding="utf-8")

    def replace_field(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in replacements:
            raise SystemExit(f"Unresolved template field in {path}: {{{{{key}}}}}")
        return replacements[key]

    return TEMPLATE_FIELD.sub(replace_field, text)


def atomic_write_text(path: Path, content: str) -> None:
    """Publish one text file without truncating the previous incarnation first."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary = Path(handle.name)
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary is not None:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass


def write_owned_file(path: Path, content: str, replace: bool) -> str:
    if path.exists() and not replace:
        return "kept"
    atomic_write_text(path, content)
    return "written"


def acquire_instance_write_lock(instance_path: Path) -> Path:
    """Serialize cooperative writers of INSTANCE without hiding stale ownership."""

    lock_path = instance_path.parent / INSTANCE_LOCK_NAME
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        descriptor = os.open(
            lock_path,
            os.O_CREAT | os.O_EXCL | os.O_WRONLY,
            0o600,
        )
    except FileExistsError as exc:
        raise SystemExit(
            f"INSTANCE write lock already exists: {lock_path}. "
            "Another configurator may still be writing, or an earlier process may "
            "have stopped unexpectedly. Inspect the lock and current INSTANCE; "
            "remove the lock only after establishing that no writer still owns it."
        ) from exc

    try:
        payload = {
            "pid": os.getpid(),
            "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(payload, handle, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
    except BaseException:
        try:
            lock_path.unlink()
        except FileNotFoundError:
            pass
        raise

    def release() -> None:
        try:
            lock_path.unlink()
        except FileNotFoundError:
            pass

    atexit.register(release)
    return lock_path


def normalized_github_repository(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    parts = value.strip().split("/")
    if len(parts) != 2 or not all(parts):
        return None
    return "/".join(part.casefold() for part in parts)


def same_github_repository(left: object, right: object) -> bool:
    left_normalized = normalized_github_repository(left)
    right_normalized = normalized_github_repository(right)
    return (
        left_normalized is not None
        and right_normalized is not None
        and left_normalized == right_normalized
    )


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def decode_bridge(data: bytes, path: Path) -> str:
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise SystemExit(f"Configured adapter is not valid UTF-8: {path}: {exc}") from exc


def read_semver(path: Path, label: str) -> str:
    value = path.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", value):
        raise SystemExit(f"{label} is not semantic: {value!r}")
    return value


def configured_bridge_repository(text: str) -> str | None:
    """Return a repository only for the recognized constitutive bridge header."""

    match = BRIDGE_IDENTITY_HEADER.match(text)
    return match.group(1) if match is not None else None


def load_instance(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Cannot read valid instance state from {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SystemExit(f"Instance state must be a JSON object: {path}")
    schema = value.get("schema")
    if schema != "kernel_chat.instance.v1":
        raise SystemExit(
            f"Unsupported instance schema in {path}: {schema!r}. "
            "This configurator only mutates kernel_chat.instance.v1."
        )
    host_adapter = value.get("host_adapter")
    if host_adapter != "chatgpt":
        raise SystemExit(
            f"Unsupported host_adapter in {path}: {host_adapter!r}. "
            "This configurator only mutates the ChatGPT incarnation."
        )
    return value


def render_json(value: dict[str, object]) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def initial_instance(
    template_path: Path,
    replacements: dict[str, str],
) -> dict[str, object]:
    try:
        rendered = render(template_path, replacements)
        value = json.loads(rendered)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid instance template: {exc}") from exc
    if not isinstance(value, dict):
        raise SystemExit("Instance template must render to a JSON object.")
    return value


def refresh_instance(
    current: dict[str, object],
    *,
    package_source_version: str,
    available_bridge_template_version: str,
    observed_bridge_sha256: str | None,
    observed_bridge_repository: str | None,
    configured_bridge_template_version: str | None = None,
    adapter_replaced: bool = False,
) -> dict[str, object]:
    value = dict(current)
    value["schema"] = "kernel_chat.instance.v1"
    value["canonical_upstream"] = CANONICAL_UPSTREAM
    value["package_source_version"] = package_source_version
    value["host_adapter"] = "chatgpt"
    value["available_bridge_template_version"] = available_bridge_template_version

    # Older development receipts used one field for both the template available
    # in the package and the provenance of the configured bridge. That
    # distinction cannot be reconstructed safely from the old field alone.
    value.pop("bridge_template_version", None)

    if adapter_replaced:
        # Replacement is the explicit reconciliation effect for the local
        # configured artifact. It can establish byte identity, target and
        # template provenance because this command generated the new bridge.
        if observed_bridge_sha256 is None:
            raise SystemExit("Adapter replacement requires observable configured bridge bytes.")
        value["configured_bridge_sha256"] = observed_bridge_sha256
        value["configured_bridge_template_version"] = (
            configured_bridge_template_version
            if configured_bridge_template_version is not None
            else available_bridge_template_version
        )
        value["configured_bridge_repository"] = (
            observed_bridge_repository if observed_bridge_repository is not None else "unknown"
        )
    else:
        # A package/instance refresh observes the current local bridge but does
        # not accept drift as the new configured incarnation.
        if not isinstance(value.get("configured_bridge_template_version"), str):
            value["configured_bridge_template_version"] = "unknown"
        recorded_digest = value.get("configured_bridge_sha256")
        if (
            observed_bridge_sha256 is not None
            and "configured_bridge_repository" not in value
            and recorded_digest == observed_bridge_sha256
        ):
            value["configured_bridge_repository"] = (
                observed_bridge_repository if observed_bridge_repository is not None else "unknown"
            )

    host = value.get("host_installation")
    if not isinstance(host, dict):
        host = {
            "state": "unknown",
            "confirmed_at": None,
            "installed_bridge_sha256": None,
            "installed_bridge_repository": None,
            "installed_bridge_template_version": None,
        }
    else:
        host = dict(host)
        host.setdefault("confirmed_at", None)
        host.setdefault("installed_bridge_sha256", None)
        host.setdefault("installed_bridge_repository", None)
        host.setdefault("installed_bridge_template_version", None)

    if adapter_replaced:
        # A requested replacement is not automatically a material host drift.
        # If the resulting configured bytes are exactly the incarnation the
        # operator already confirmed, preserve that confirmation. Otherwise the
        # host remains on the previous installed incarnation until re-confirmed.
        installed_repository = host.get("installed_bridge_repository")
        repository_matches = (
            installed_repository in (None, "", "unknown")
            or observed_bridge_repository is None
            or same_github_repository(
                installed_repository, observed_bridge_repository
            )
        )
        confirmed_at = host.get("confirmed_at")
        prior_state = host.get("state")
        receipt_still_applicable = prior_state in (
            "installed_operator_confirmed",
            "local_adapter_updated_host_unconfirmed",
        )
        receipt_matches_result = (
            receipt_still_applicable
            and host.get("installed_bridge_sha256") == observed_bridge_sha256
            and isinstance(confirmed_at, str)
            and bool(confirmed_at.strip())
            and repository_matches
        )
        host["state"] = (
            "installed_operator_confirmed"
            if receipt_matches_result
            else "local_adapter_updated_host_unconfirmed"
        )

    value["host_installation"] = host

    source_contact = value.get("source_contact")
    if not isinstance(source_contact, dict):
        value["source_contact"] = {
            "last_observed_revision": None,
            "last_observed_at": None,
            "material_delta": None,
        }
    return value

def confirm_host_installation(
    current: dict[str, object],
    *,
    installed_bridge_sha256: str,
    installed_bridge_repository: str,
    installed_bridge_template_version: str,
) -> dict[str, object]:
    value = dict(current)
    host = value.get("host_installation")
    if not isinstance(host, dict):
        host = {}
    else:
        host = dict(host)
    host["state"] = "installed_operator_confirmed"
    host["confirmed_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    host["installed_bridge_sha256"] = installed_bridge_sha256
    host["installed_bridge_repository"] = installed_bridge_repository
    host["installed_bridge_template_version"] = installed_bridge_template_version
    value["host_installation"] = host
    return value

def main() -> int:
    args = parse_args()
    validate_slug(args.github_user, "--github-user")
    validate_slug(args.repository, "--repository")

    project_name = args.project_name.strip() if args.project_name else ""
    project_source = args.project_source.strip() if args.project_source else ""
    if bool(project_name) != bool(project_source):
        raise SystemExit("--project-name and --project-source must be supplied together.")
    project_selected = bool(project_name)

    if args.confirm_host_installation and (
        args.replace_adapter
        or args.preview_adapter
        or args.replace_state
        or args.refresh_instance
    ):
        raise SystemExit(
            "--confirm-host-installation is an exact receipt effect and cannot be "
            "combined with adapter/state/instance mutation flags."
        )
    if args.expected_bridge_sha256 and not args.confirm_host_installation:
        raise SystemExit(
            "--expected-bridge-sha256 is valid only with --confirm-host-installation."
        )
    if args.confirm_host_installation and not args.expected_bridge_sha256:
        raise SystemExit(
            "--confirm-host-installation requires --expected-bridge-sha256 for the "
            "bridge incarnation that was actually delivered to the operator."
        )
    if args.expected_bridge_sha256 and not SHA256_HEX.fullmatch(
        args.expected_bridge_sha256
    ):
        raise SystemExit("--expected-bridge-sha256 must be a lowercase SHA-256 digest.")

    instance_repository = f"{args.github_user}/{args.repository}"
    package_source_version = read_semver(ROOT / "VERSION", "VERSION")
    bridge_template_version = read_semver(
        ROOT / "adapters/chatgpt/VERSION", "ChatGPT bridge VERSION"
    )

    adapter_template = ROOT / "adapters/chatgpt/CUSTOM_INSTRUCTIONS.template.md"
    adapter_output = ROOT / "adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md"
    current_template = ROOT / "templates/state/CURRENT.md"
    sources_template = ROOT / "templates/state/SOURCES.md"
    instance_template = ROOT / "templates/state/INSTANCE.json"
    instance_output = ROOT / "state/INSTANCE.json"

    if args.preview_adapter:
        adapter_candidate = render(
            adapter_template,
            {
                "GITHUB_USER": args.github_user,
                "REPOSITORY": args.repository,
            },
        )
        print(adapter_candidate, end="")
        return 0

    acquire_instance_write_lock(instance_output)

    adapter_preexisting = adapter_output.exists()
    existing_instance = load_instance(instance_output) if instance_output.exists() else None

    if args.refresh_instance and existing_instance is None:
        raise SystemExit(
            "--refresh-instance requires an existing state/INSTANCE.json. "
            "Run ordinary configuration to form a new instance."
        )

    if existing_instance is not None and not args.preview_adapter:
        recorded_instance_repository = existing_instance.get("instance_repository")
        if not same_github_repository(
            recorded_instance_repository, instance_repository
        ):
            raise SystemExit(
                "Command repository identity does not match INSTANCE.instance_repository. "
                "Use the repository identity already owned by the instance; repository "
                "identity migration requires a separate explicit effect. "
                "--preview-adapter may still inspect a no-write candidate for another target."
            )

    if args.confirm_host_installation:
        if existing_instance is None:
            raise SystemExit(
                "Cannot confirm host installation before state/INSTANCE.json exists."
            )
        if not adapter_preexisting:
            raise SystemExit(
                "Cannot confirm host installation without a configured ChatGPT adapter."
            )

        recorded_repository = existing_instance.get("instance_repository")
        if not same_github_repository(recorded_repository, instance_repository):
            raise SystemExit(
                "Host confirmation repository does not match INSTANCE.instance_repository: "
                f"{instance_repository!r} != {recorded_repository!r}"
            )

        actual_adapter_bytes = adapter_output.read_bytes()
        actual_adapter = decode_bridge(actual_adapter_bytes, adapter_output)
        embedded_repository = configured_bridge_repository(actual_adapter)
        if (
            embedded_repository is not None
            and not same_github_repository(embedded_repository, recorded_repository)
        ):
            raise SystemExit(
                "Configured adapter targets a different user-owned repository than "
                "INSTANCE: "
                f"{embedded_repository!r} != {recorded_repository!r}"
            )

        digest = sha256_bytes(actual_adapter_bytes)
        if digest != args.expected_bridge_sha256:
            raise SystemExit(
                "Operator confirmation refers to a different bridge delivery than the "
                "currently configured adapter. Re-deliver the current configured bridge "
                "and confirm that exact incarnation instead of transferring a late "
                "confirmation across bridge changes."
            )
        recorded_digest = existing_instance.get("configured_bridge_sha256")
        if recorded_digest != digest:
            raise SystemExit(
                "Configured adapter bytes differ from INSTANCE.configured_bridge_sha256. "
                "Host confirmation cannot reconcile local artifact drift; review or "
                "replace the adapter first."
            )

        receipt_repository = existing_instance.get("configured_bridge_repository")
        if not isinstance(receipt_repository, str) or not receipt_repository.strip():
            receipt_repository = "unknown"
        if (
            receipt_repository != "unknown"
            and embedded_repository is not None
            and not same_github_repository(receipt_repository, embedded_repository)
        ):
            raise SystemExit(
                "Configured adapter repository differs from the persisted configured "
                "bridge repository receipt."
            )
        if (
            receipt_repository != "unknown"
            and not same_github_repository(receipt_repository, recorded_repository)
        ):
            raise SystemExit(
                "Persisted configured bridge repository differs from INSTANCE.instance_repository."
            )

        installed_repository = (
            embedded_repository
            if embedded_repository is not None
            else receipt_repository
        )
        configured_template = existing_instance.get("configured_bridge_template_version")
        installed_template = (
            configured_template
            if isinstance(configured_template, str) and configured_template.strip()
            else "unknown"
        )
        confirmed = confirm_host_installation(
            existing_instance,
            installed_bridge_sha256=digest,
            installed_bridge_repository=installed_repository,
            installed_bridge_template_version=installed_template,
        )
        atomic_write_text(instance_output, render_json(confirmed))
        print("state/INSTANCE.json=host-confirmed")
        print(
            "HOST INSTALLATION RECEIPT: operator confirmation bound to configured "
            f"bridge digest {digest}; repository={installed_repository}; "
            f"template={installed_template}."
        )
        return 0

    if project_selected:
        context_kind = "project"
        context_name = project_name
        context_source = project_source
        initial_source_note = f"Initial project context: `{project_name}`."
        initial_source_row = (
            f"| {project_source} | Project owner | Owner-native project truth | "
            "When project facts, current state, or implementation can change the result |"
        )
    else:
        context_kind = "none_selected"
        context_name = "none selected"
        context_source = "none selected"
        initial_source_note = (
            "No initial project or domain source was selected. Add a source only when "
            "its distinct ownership or evidence role can change the work."
        )
        initial_source_row = ""

    replacements = {
        "GITHUB_USER": args.github_user,
        "REPOSITORY": args.repository,
        "CONTEXT_KIND": context_kind,
        "CONTEXT_NAME": context_name,
        "CONTEXT_SOURCE": context_source,
        "INITIAL_SOURCE_NOTE": initial_source_note,
        "INITIAL_SOURCE_ROW": initial_source_row,
        "DATE": date.today().isoformat(),
    }

    # Resolve every candidate before mutation. Preview is an observation effect:
    # it must not inherit preservation/decoding prerequisites from the old bridge.
    adapter_candidate = render(adapter_template, replacements)
    current_candidate = render(current_template, replacements)
    sources_candidate = render(sources_template, replacements)

    if args.preview_adapter:
        print(adapter_candidate, end="")
        return 0

    previous_adapter_bytes = adapter_output.read_bytes() if adapter_preexisting else None
    missing_existing_adapter = (
        existing_instance is not None
        and not adapter_preexisting
        and not args.replace_adapter
    )
    if missing_existing_adapter:
        actual_adapter_bytes = None
        actual_adapter = None
        adapter_digest = None
        embedded_repository = None
        adapter_bytes_changed = False
    else:
        if adapter_preexisting and not args.replace_adapter:
            actual_adapter_bytes = previous_adapter_bytes
            actual_adapter = decode_bridge(actual_adapter_bytes, adapter_output)
        else:
            actual_adapter = adapter_candidate
            actual_adapter_bytes = adapter_candidate.encode("utf-8")
        adapter_digest = sha256_bytes(actual_adapter_bytes)
        embedded_repository = configured_bridge_repository(actual_adapter)
        adapter_bytes_changed = (
            args.replace_adapter
            and (previous_adapter_bytes is None or previous_adapter_bytes != actual_adapter_bytes)
        )

    preserved_repository: object = (
        existing_instance.get("instance_repository")
        if existing_instance is not None
        else instance_repository
    )
    if adapter_preexisting and not args.replace_adapter:
        if not isinstance(preserved_repository, str) or not preserved_repository.strip():
            raise SystemExit(
                "Cannot preserve configured adapter because the instance repository "
                "identity is missing or invalid."
            )
        if (
            embedded_repository is not None
            and not same_github_repository(embedded_repository, preserved_repository)
        ):
            raise SystemExit(
                "Existing configured adapter targets a different user-owned repository "
                "than the instance being preserved: "
                f"{embedded_repository!r} != {preserved_repository!r}. "
                "Use matching --github-user/--repository values or select "
                "--replace-adapter to generate a bridge for the intended instance."
            )

    if existing_instance is None:
        if adapter_digest is None:
            raise SystemExit("Initial configuration requires configured bridge bytes.")
        instance_replacements = {
            "GITHUB_USER": args.github_user,
            "REPOSITORY": args.repository,
            "PACKAGE_SOURCE_VERSION": package_source_version,
            "BRIDGE_TEMPLATE_VERSION": bridge_template_version,
            "CONFIGURED_BRIDGE_TEMPLATE_VERSION": (
                "unknown" if adapter_preexisting and not args.replace_adapter else bridge_template_version
            ),
            "CONFIGURED_BRIDGE_REPOSITORY": (
                embedded_repository
                if adapter_preexisting and not args.replace_adapter and embedded_repository is not None
                else ("unknown" if adapter_preexisting and not args.replace_adapter else instance_repository)
            ),
            "CONFIGURED_BRIDGE_SHA256": adapter_digest,
            "HOST_INSTALLATION_STATE": (
                "local_adapter_updated_host_unconfirmed"
                if adapter_preexisting and args.replace_adapter
                else ("unknown" if adapter_preexisting else "pending_operator_confirmation")
            ),
        }
        instance_candidate = initial_instance(instance_template, instance_replacements)
        instance_action = "written"
    elif args.replace_adapter or args.refresh_instance:
        instance_candidate = refresh_instance(
            existing_instance,
            package_source_version=package_source_version,
            available_bridge_template_version=bridge_template_version,
            observed_bridge_sha256=adapter_digest,
            observed_bridge_repository=embedded_repository,
            configured_bridge_template_version=(
                bridge_template_version if args.replace_adapter else None
            ),
            adapter_replaced=args.replace_adapter,
        )
        instance_action = "refreshed"
    else:
        instance_candidate = existing_instance
        instance_action = "kept"

    if missing_existing_adapter:
        adapter_status = "missing-preserved"
    else:
        adapter_status = write_owned_file(
            adapter_output, adapter_candidate, bool(adapter_bytes_changed)
        )
    current_output = ROOT / "state/CURRENT.md"
    sources_output = ROOT / "state/SOURCES.md"
    if existing_instance is not None and not args.replace_state and not current_output.exists():
        current_status = "missing-preserved"
    else:
        current_status = write_owned_file(
            current_output, current_candidate, args.replace_state
        )
    if existing_instance is not None and not args.replace_state and not sources_output.exists():
        sources_status = "missing-preserved"
    else:
        sources_status = write_owned_file(
            sources_output, sources_candidate, args.replace_state
        )

    if not instance_output.exists():
        instance_output.parent.mkdir(parents=True, exist_ok=True)
        atomic_write_text(instance_output, render_json(instance_candidate))
        instance_status = "written"
    elif instance_action == "refreshed":
        atomic_write_text(instance_output, render_json(instance_candidate))
        instance_status = "refreshed"
    else:
        instance_status = "kept"

    actual_chars = (
        len(adapter_output.read_text(encoding="utf-8"))
        if adapter_output.exists()
        else 0
    )
    relative_adapter = adapter_output.relative_to(ROOT).as_posix()
    print(f"adapter={relative_adapter} status={adapter_status} chars={actual_chars}")
    if adapter_digest is not None:
        print(f"confirmation_bridge_sha256={adapter_digest}")
    print(f"state/INSTANCE.json={instance_status}")
    print("HOST UI BOUNDARY: this script does not install or update ChatGPT Custom Instructions.")

    if existing_instance is None and not adapter_preexisting:
        print(
            "NEXT OPERATOR ACTION FOR ADOPTION: copy the complete text from "
            f"{relative_adapter} into ChatGPT Custom Instructions through the "
            "ChatGPT UI and save it."
        )
        print(
            "After that UI action, run the same repository identity with "
            "--confirm-host-installation to bind the operator confirmation to the "
            "already-reconciled configured bridge identity."
        )
        print(
            "Until the operator confirms that UI action, report: "
            "repository configured / host activation pending."
        )
    elif args.replace_adapter:
        host = (
            instance_candidate.get("host_installation")
            if isinstance(instance_candidate, dict)
            else None
        )
        if isinstance(host, dict) and host.get("state") == "installed_operator_confirmed":
            print(
                "Configured adapter already matches the operator-confirmed host "
                "incarnation. No ChatGPT UI update is required."
            )
        else:
            print(
                "NEXT OPERATOR ACTION FOR HOST UPDATE: the local configured adapter was "
                f"replaced. To update ChatGPT, copy the complete text from {relative_adapter} "
                "into ChatGPT Custom Instructions through the ChatGPT UI and save it."
            )
            print(
                "After that UI action, run the same repository identity with "
                "--confirm-host-installation to bind the installed-host receipt to the "
                "already-reconciled configured bridge identity."
            )
            print(
                "Until the operator confirms that UI action, report: "
                "local adapter updated / host instructions unchanged."
            )
    elif missing_existing_adapter:
        print(
            "Configured adapter is absent locally. State/package work completed without "
            "regenerating it; use --replace-adapter only when local bridge regeneration "
            "is explicitly selected."
        )
    else:
        print("Configured adapter preserved. No host update occurred.")
        if embedded_repository is None:
            print(
                "BRIDGE IDENTITY NOTICE: the preserved adapter repository identity "
                "could not be verified from known kernel_chat bridge syntax."
            )
        print(
            "If first adoption is still pending, the operator must copy the existing "
            f"{relative_adapter} into ChatGPT Custom Instructions through the ChatGPT UI. "
            "For an adapter update, review --preview-adapter and select --replace-adapter "
            "before asking the operator to update the host."
        )

    print(f"state/CURRENT.md={current_status}")
    print(f"state/SOURCES.md={sources_status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
