#!/usr/bin/env python3
"""Dependency-free structural validation for kernel_chat."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "INSTALL.md",
    "CONTRIBUTING.md",
    "AGENTS.md",
    "CURRENT_STATE.md",
    ".github/ISSUE_TEMPLATE/evolution-feedback.md",
    "docs/ADOPTION_GUIDE.md",
    "docs/ARCHITECTURE.md",
    "docs/USER_GUIDE.md",
    "docs/EVOLUTION_GUIDE.md",
    "state/README.md",
    "VERSION",
    "LICENSE",
    "kernel/KERNEL.md",
    "kernel/COMPETENCE.md",
    "kernel/FDLA.md",
    "kernel/EVOLUTION.md",
    "operations/CURRENT.md",
    "operations/FLOWS.md",
    "operations/REQUESTS_RESULTS.md",
    "operations/RECEIPTS_RECOVERY.md",
    "adapters/conversational/VERSION",
    "adapters/conversational/INSTRUCTIONS.template.md",
    "adapters/conversational/README.md",
    "adapters/chatgpt/VERSION",
    "adapters/chatgpt/CUSTOM_INSTRUCTIONS.template.md",
    "templates/state/INSTANCE.json",
    "templates/state/CURRENT.md",
    "templates/state/SOURCES.md",
    "scripts/configure.py",
    "tests/test_configure.py",
    "tests/test_validate.py",
    "tests/test_markdown_consumer.py",
    "requirements-test.txt",
]

SEMVER = re.compile(r"\d+\.\d+\.\d+")
SHA256 = re.compile(r"[0-9a-f]{64}")
BRIDGE_IDENTITY_HEADER = re.compile(
    r"\A(?:"
    r"Kernel source:\s*github:([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\.\s*(?:\r?\n|$)"
    r"|Work from the present\. Act directly when the conversation and working set "
    r"suffice; a new chat alone does not require a boot\.\r?\n\r?\n"
    r"User-owned kernel (?:repository|instance):\s*"
    r"([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\.\s*(?:\r?\n|$)"
    r")"
)

AGENT_DISCOVERY_ROUTES = (
    (
        "kernel/KERNEL.md#kernel-chat-mobile-observation",
        '<a name="kernel-chat-mobile-observation"></a>',
    ),
    (
        "kernel/EVOLUTION.md#kernel-chat-converge-resultant",
        '<a name="kernel-chat-converge-resultant"></a>',
    ),
)


def read_semver(path: Path, label: str, errors: list[str]) -> str | None:
    if not path.is_file():
        return None
    value = path.read_text(encoding="utf-8").strip()
    if not SEMVER.fullmatch(value):
        errors.append(f"{label} is not semantic: {value!r}")
    return value


def bridge_repositories(text: str) -> set[str]:
    match = BRIDGE_IDENTITY_HEADER.match(text)
    if match is None:
        return set()
    return {group for group in match.groups() if group is not None}


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


def validate_instance(value: object, label: str, errors: list[str]) -> None:
    if not isinstance(value, dict):
        errors.append(f"{label} must be a JSON object")
        return

    for key in (
        "schema",
        "instance_repository",
        "canonical_upstream",
        "package_source_version",
        "host_adapter",
        "available_bridge_template_version",
        "configured_bridge_template_version",
        "configured_bridge_sha256",
        "host_installation",
        "source_contact",
    ):
        if key not in value:
            errors.append(f"{label} missing field: {key}")

    if value.get("schema") != "kernel_chat.instance.v1":
        errors.append(f"{label} has unsupported schema: {value.get('schema')!r}")

    for key in ("instance_repository", "canonical_upstream", "host_adapter"):
        candidate = value.get(key)
        if not isinstance(candidate, str) or not candidate.strip():
            errors.append(f"{label} field {key} must be a non-empty string")

    for key in ("package_source_version", "available_bridge_template_version"):
        candidate = value.get(key)
        if not isinstance(candidate, str) or not SEMVER.fullmatch(candidate):
            errors.append(f"{label} field {key} is not semantic: {candidate!r}")

    configured_version = value.get("configured_bridge_template_version")
    if not isinstance(configured_version, str) or not (
        configured_version == "unknown" or SEMVER.fullmatch(configured_version)
    ):
        errors.append(
            f"{label} configured_bridge_template_version must be semantic or 'unknown': "
            f"{configured_version!r}"
        )

    configured_repository = value.get("configured_bridge_repository")
    if configured_repository is not None and (
        not isinstance(configured_repository, str) or not configured_repository.strip()
    ):
        errors.append(f"{label} configured_bridge_repository must be absent or a non-empty string")
    elif (
        isinstance(configured_repository, str)
        and configured_repository != "unknown"
        and not same_github_repository(
            configured_repository, value.get("instance_repository")
        )
    ):
        errors.append(
            f"{label} configured_bridge_repository must match instance_repository "
            "when its target is known"
        )

    digest = value.get("configured_bridge_sha256")
    if not isinstance(digest, str) or not SHA256.fullmatch(digest):
        errors.append(f"{label} configured_bridge_sha256 is invalid")

    host = value.get("host_installation")
    if not isinstance(host, dict):
        errors.append(f"{label} host_installation must be an object")
    else:
        for key in ("state", "confirmed_at", "installed_bridge_sha256"):
            if key not in host:
                errors.append(f"{label} host_installation missing field: {key}")
        if not isinstance(host.get("state"), str) or not host.get("state"):
            errors.append(f"{label} host_installation.state must be a non-empty string")

        confirmed_at = host.get("confirmed_at")
        if confirmed_at is not None and (
            not isinstance(confirmed_at, str) or not confirmed_at.strip()
        ):
            errors.append(
                f"{label} host_installation.confirmed_at must be null or a non-empty string"
            )

        installed_digest = host.get("installed_bridge_sha256")
        if installed_digest is not None and (
            not isinstance(installed_digest, str) or not SHA256.fullmatch(installed_digest)
        ):
            errors.append(
                f"{label} host_installation.installed_bridge_sha256 is invalid"
            )

        installed_repository = host.get("installed_bridge_repository")
        if installed_repository is not None and (
            not isinstance(installed_repository, str) or not installed_repository.strip()
        ):
            errors.append(
                f"{label} host_installation.installed_bridge_repository must be null or a non-empty string"
            )

        installed_template = host.get("installed_bridge_template_version")
        if installed_template is not None and (
            not isinstance(installed_template, str)
            or not (installed_template == "unknown" or SEMVER.fullmatch(installed_template))
        ):
            errors.append(
                f"{label} host_installation.installed_bridge_template_version must be null, semantic, or 'unknown'"
            )

        if host.get("state") == "installed_operator_confirmed":
            if installed_digest is None:
                errors.append(
                    f"{label} installed_operator_confirmed requires installed_bridge_sha256"
                )
            if not isinstance(confirmed_at, str) or not confirmed_at.strip():
                errors.append(
                    f"{label} installed_operator_confirmed requires confirmed_at"
                )

        configured_digest = value.get("configured_bridge_sha256")
        if (
            isinstance(configured_digest, str)
            and isinstance(installed_digest, str)
            and configured_digest == installed_digest
            and isinstance(configured_repository, str)
            and configured_repository not in ("", "unknown")
            and isinstance(installed_repository, str)
            and installed_repository not in ("", "unknown")
            and not same_github_repository(
                configured_repository, installed_repository
            )
        ):
            errors.append(
                f"{label} same bridge digest has conflicting configured/installed "
                "repository identities"
            )

    source_contact = value.get("source_contact")
    if not isinstance(source_contact, dict):
        errors.append(f"{label} source_contact must be an object")
    else:
        for key in ("last_observed_revision", "last_observed_at", "material_delta"):
            if key not in source_contact:
                errors.append(f"{label} source_contact missing field: {key}")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def has_discovery_route_declaration(text: str, route: str) -> bool:
    declaration = f"- `{route}`"
    return any(line.strip() == declaration for line in text.splitlines())


def has_owner_marker(text: str, marker: str) -> bool:
    return any(line.strip() == marker for line in text.splitlines())


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    version = read_semver(ROOT / "VERSION", "VERSION", errors)
    bridge_version = read_semver(
        ROOT / "adapters/conversational/VERSION",
        "conversational instructions VERSION",
        errors,
    )

    adapter_template = ROOT / "adapters/conversational/INSTRUCTIONS.template.md"
    if adapter_template.is_file():
        template = adapter_template.read_text(encoding="utf-8")
        if template.count("{{KERNEL_SOURCE}}") != 1:
            errors.append(
                "conversational instructions template must contain {{KERNEL_SOURCE}} once"
            )
        for relation in (
            "AGENTS.md",
            "state/CURRENT.md",
            "state/SOURCES.md",
            "kernel/KERNEL.md",
            "kernel/COMPETENCE.md",
            "kernel/FDLA.md",
            "kernel/EVOLUTION.md",
            "kernel/KERNEL.md#kernel-chat-competence-trace",
            "A competence can make another competence pertinent",
            "reusable learning",
            "Do not presume",
            "without narrowing the field",
        ):
            if relation not in template:
                errors.append(
                    f"conversational instructions template missing relation: {relation}"
                )
        if re.search(r"{{(?:GITHUB|PROJECT|CHATGPT)_[A-Z_]+}}", template):
            errors.append(
                "conversational instructions template must remain provider/source neutral"
            )

    chatgpt_compat = ROOT / "adapters/chatgpt/CUSTOM_INSTRUCTIONS.template.md"
    if chatgpt_compat.is_file():
        compatibility = chatgpt_compat.read_text(encoding="utf-8")
        if "../conversational/INSTRUCTIONS.template.md" not in compatibility:
            errors.append(
                "ChatGPT compatibility template must point to the conversational instruction source"
            )

    instance_template = ROOT / "templates/state/INSTANCE.json"
    if instance_template.is_file():
        rendered = instance_template.read_text(encoding="utf-8")
        replacements = {
            "GITHUB_USER": "example-user",
            "REPOSITORY": "example-kernel",
            "PACKAGE_SOURCE_VERSION": version or "0.0.0",
            "BRIDGE_TEMPLATE_VERSION": bridge_version or "0.0.0",
            "CONFIGURED_BRIDGE_TEMPLATE_VERSION": bridge_version or "0.0.0",
            "CONFIGURED_BRIDGE_REPOSITORY": "example-user/example-kernel",
            "CONFIGURED_BRIDGE_SHA256": "0" * 64,
            "HOST_INSTALLATION_STATE": "pending_operator_confirmation",
        }
        for key, value in replacements.items():
            rendered = rendered.replace("{{" + key + "}}", value)
        unresolved = sorted(set(re.findall(r"{{[A-Z_]+}}", rendered)))
        if unresolved:
            errors.append(f"instance template has unresolved fields: {unresolved}")
        else:
            try:
                validate_instance(json.loads(rendered), "instance template", errors)
            except json.JSONDecodeError as exc:
                errors.append(f"invalid instance template JSON: {exc}")

    configured = ROOT / "adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md"
    configured_bytes: bytes | None = None
    configured_text: str | None = None
    if configured.exists():
        configured_bytes = configured.read_bytes()
        try:
            configured_text = configured_bytes.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"configured adapter is not valid UTF-8: {exc}")
        if configured_text is not None and re.search(r"{{[A-Z_]+}}", configured_text):
            errors.append("configured adapter contains unresolved fields")
        if configured_text is not None:
            warnings.append(f"configured adapter present locally ({len(configured_text)} chars)")

    for relative in ("state/CURRENT.md", "state/SOURCES.md"):
        path = ROOT / relative
        if path.exists() and re.search(
            r"{{[A-Z_]+}}", path.read_text(encoding="utf-8")
        ):
            errors.append(f"configured state contains unresolved fields: {relative}")

    instance_path = ROOT / "state/INSTANCE.json"
    instance_value: dict[str, object] | None = None
    if instance_path.exists():
        try:
            parsed = json.loads(instance_path.read_text(encoding="utf-8"))
            validate_instance(parsed, "state/INSTANCE.json", errors)
            if isinstance(parsed, dict):
                instance_value = parsed
        except json.JSONDecodeError as exc:
            errors.append(f"invalid state/INSTANCE.json: {exc}")

    # Drift is observable without declaring a migration invalid. A user-owned
    # instance may legitimately remain on an older adopted package or bridge
    # while reconciliation is still pending.
    if instance_value is not None and configured_text is None:
        warnings.append(
            "configured adapter is absent locally; persisted INSTANCE identity is "
            "preserved and regeneration requires an explicit adapter replacement"
        )

    if instance_value is not None:
        if version and instance_value.get("package_source_version") != version:
            warnings.append(
                "instance package source differs from repository VERSION: "
                f"{instance_value.get('package_source_version')!r} != {version!r}"
            )

        available_version = instance_value.get("available_bridge_template_version")
        if bridge_version and available_version != bridge_version:
            warnings.append(
                "instance available bridge template differs from repository bridge VERSION: "
                f"{available_version!r} != {bridge_version!r}"
            )

        configured_version = instance_value.get("configured_bridge_template_version")
        if configured_version == "unknown":
            warnings.append(
                "configured bridge template provenance is unknown; preserve the bridge "
                "until its origin/fit is reconciled rather than assuming current template identity"
            )
        elif bridge_version and configured_version != bridge_version:
            warnings.append(
                "configured bridge derives from a different template version than the "
                f"currently available bridge: {configured_version!r} != {bridge_version!r}"
            )

        if configured_text is not None and configured_bytes is not None:
            actual_digest = sha256_bytes(configured_bytes)
            if instance_value.get("configured_bridge_sha256") != actual_digest:
                warnings.append(
                    "instance configured bridge digest differs from local configured bridge; "
                    "reconcile customization/replacement before claiming synchronization"
                )

            configured_receipt_repository = instance_value.get("configured_bridge_repository")
            if configured_receipt_repository is None:
                warnings.append(
                    "legacy INSTANCE receipt has no configured bridge repository field"
                )
            elif configured_receipt_repository == "unknown":
                warnings.append(
                    "configured bridge repository identity is unknown in INSTANCE"
                )

            repositories = bridge_repositories(configured_text)
            if len(repositories) > 1:
                errors.append(
                    "configured bridge contains conflicting user-owned repository identities: "
                    f"{sorted(repositories)!r}"
                )
            elif len(repositories) == 1:
                configured_repository = next(iter(repositories))
                if not same_github_repository(
                    configured_repository, instance_value.get("instance_repository")
                ):
                    warnings.append(
                        "configured bridge targets a different user-owned repository than "
                        "INSTANCE.instance_repository: "
                        f"{configured_repository!r} != "
                        f"{instance_value.get('instance_repository')!r}"
                    )
                receipt_repository = instance_value.get("configured_bridge_repository")
                if (
                    isinstance(receipt_repository, str)
                    and receipt_repository not in ("", "unknown")
                    and not same_github_repository(
                        receipt_repository, configured_repository
                    )
                ):
                    warnings.append(
                        "configured bridge repository differs from the persisted configured "
                        "bridge repository receipt: "
                        f"{configured_repository!r} != {receipt_repository!r}"
                    )
            else:
                warnings.append(
                    "configured bridge repository identity could not be verified from known "
                    "kernel_chat bridge syntax"
                )

            host = instance_value.get("host_installation")
            if isinstance(host, dict):
                installed_digest = host.get("installed_bridge_sha256")
                if isinstance(installed_digest, str) and installed_digest != actual_digest:
                    warnings.append(
                        "local configured bridge differs from the last operator-confirmed "
                        "installed bridge digest; host resynchronization may be pending"
                    )
                installed_repository = host.get("installed_bridge_repository")
                if (
                    isinstance(installed_repository, str)
                    and installed_repository not in ("", "unknown")
                    and len(repositories) == 1
                    and not same_github_repository(
                        installed_repository, next(iter(repositories))
                    )
                ):
                    warnings.append(
                        "local configured bridge repository differs from the last "
                        "operator-confirmed installed bridge repository"
                    )

    agents_path = ROOT / "AGENTS.md"
    if agents_path.is_file():
        agents_text = agents_path.read_text(encoding="utf-8")
        for route, marker in AGENT_DISCOVERY_ROUTES:
            if not has_discovery_route_declaration(agents_text, route):
                errors.append(
                    f"AGENTS.md missing structural discovery route: {route}"
                )
                continue
            destination = route.split("#", 1)[0]
            target = ROOT / destination
            if not target.is_file():
                errors.append(
                    f"AGENTS.md discovery route target is missing: {route}"
                )
                continue
            if not has_owner_marker(
                target.read_text(encoding="utf-8"), marker
            ):
                errors.append(
                    f"AGENTS.md discovery route owner marker is missing: {route}"
                )

    # Full Markdown consumer semantics are tested with an independent CommonMark
    # oracle in the regression suite. The dependency-free runtime validator does
    # not claim to parse arbitrary Markdown.

    result = {
        "valid": not errors,
        "version": version,
        "bridge_version": bridge_version,
        "errors": errors,
        "warnings": warnings,
        "scope": "repository structure and configured artifacts; not host behavior",
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
