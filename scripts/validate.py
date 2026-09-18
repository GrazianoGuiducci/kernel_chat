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
    "adapters/chatgpt/VERSION",
    "adapters/chatgpt/CUSTOM_INSTRUCTIONS.template.md",
    "templates/state/INSTANCE.json",
    "templates/state/CURRENT.md",
    "templates/state/SOURCES.md",
    "scripts/configure.py",
    "tests/test_configure.py",
    "tests/test_validate.py",
]

SEMVER = re.compile(r"\d+\.\d+\.\d+")
SHA256 = re.compile(r"[0-9a-f]{64}")
BRIDGE_REPOSITORY = re.compile(
    r"^User-owned kernel (?:repository|instance):\s*"
    r"([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\.\s*$",
    re.MULTILINE,
)

AGENT_DISCOVERY_ROUTES = (
    "kernel/KERNEL.md#mobile-observation-without-losing-the-point",
    "kernel/EVOLUTION.md#converge-the-changed-resultant",
)


def read_semver(path: Path, label: str, errors: list[str]) -> str | None:
    if not path.is_file():
        return None
    value = path.read_text(encoding="utf-8").strip()
    if not SEMVER.fullmatch(value):
        errors.append(f"{label} is not semantic: {value!r}")
    return value


def bridge_repositories(text: str) -> set[str]:
    return set(BRIDGE_REPOSITORY.findall(text))


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


def _blank_markdown_region(text: str) -> str:
    return "".join(char if char in "\r\n" else " " for char in text)


def markdown_link_surface(text: str) -> str:
    """Return the navigation-active Markdown surface used by package checks."""
    # HTML comments are not part of rendered navigation.
    text = re.sub(
        r"<!--.*?-->",
        lambda match: _blank_markdown_region(match.group(0)),
        text,
        flags=re.DOTALL,
    )

    visible: list[str] = []
    fence_char: str | None = None
    fence_length = 0

    for line in text.splitlines(keepends=True):
        body = line.rstrip("\r\n")
        ending = line[len(body):]

        if fence_char is not None:
            closing = re.match(
                rf"^ {{0,3}}{re.escape(fence_char)}{{{fence_length},}}[ \t]*$",
                body,
            )
            visible.append(_blank_markdown_region(body) + ending)
            if closing:
                fence_char = None
                fence_length = 0
            continue

        opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", body)
        if opening:
            marker = opening.group(1)
            fence_char = marker[0]
            fence_length = len(marker)
            visible.append(_blank_markdown_region(body) + ending)
            continue

        if body.startswith("    ") or body.startswith("\t"):
            visible.append(_blank_markdown_region(body) + ending)
            continue

        visible.append(line)

    surface = "".join(visible)

    # CommonMark code spans may cross line boundaries. Hide complete spans
    # before looking for active links, while preserving newlines for multiline
    # malformed-link detection.
    chars = list(surface)
    i = 0
    while i < len(surface):
        if surface[i] != "`":
            i += 1
            continue
        j = i
        while j < len(surface) and surface[j] == "`":
            j += 1
        run_length = j - i
        pattern = re.compile(
            rf"(?<!`)`{{{run_length}}}(?!`)"
        )
        closing = pattern.search(surface, j)
        if closing is None:
            i = j
            continue
        end = closing.end()
        for index in range(i, end):
            if chars[index] not in "\r\n":
                chars[index] = " "
        i = end

    return "".join(chars)


def markdown_heading_anchors(text: str) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    surface = markdown_link_surface(text)
    for line in surface.splitlines():
        match = re.match(r"^ {0,3}#{1,6}[ \t]+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        heading = re.sub(r"<[^>]+>", "", match.group(1))
        heading = heading.strip().lower()
        heading = re.sub(r"[^\w\- ]", "", heading)
        heading = re.sub(r"[ \t]+", "-", heading)
        base = heading.strip("-")
        if not base:
            continue
        index = counts.get(base, 0)
        counts[base] = index + 1
        anchors.add(base if index == 0 else f"{base}-{index}")
    return anchors


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    version = read_semver(ROOT / "VERSION", "VERSION", errors)
    bridge_version = read_semver(
        ROOT / "adapters/chatgpt/VERSION", "ChatGPT bridge VERSION", errors
    )

    adapter_template = ROOT / "adapters/chatgpt/CUSTOM_INSTRUCTIONS.template.md"
    if adapter_template.is_file():
        template = adapter_template.read_text(encoding="utf-8")
        for marker in ("{{GITHUB_USER}}", "{{REPOSITORY}}"):
            if template.count(marker) != 1:
                errors.append(f"adapter template must contain {marker} once")
        for relation in ("state/CURRENT.md", "AGENTS.md", "effect authority"):
            if relation not in template:
                errors.append(f"adapter template missing bridge relation: {relation}")
        if re.search(r"{{PROJECT_[A-Z_]+}}", template):
            errors.append("adapter template must not require project-specific fields")

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
        agents_surface = markdown_link_surface(
            agents_path.read_text(encoding="utf-8")
        )
        for route in AGENT_DISCOVERY_ROUTES:
            if f"]({route})" not in agents_surface:
                errors.append(f"AGENTS.md missing operating discovery route: {route}")
                continue
            destination, anchor = route.split("#", 1)
            target = ROOT / destination
            if not target.is_file():
                errors.append(
                    f"AGENTS.md discovery route target is missing: {route}"
                )
                continue
            anchors = markdown_heading_anchors(
                target.read_text(encoding="utf-8")
            )
            if anchor not in anchors:
                errors.append(
                    f"AGENTS.md discovery route anchor is missing: {route}"
                )

    # Package contract Markdown must lead to existing local owners.
    # This checks reachability, not whether a model understands or uses them.
    for relative in REQUIRED:
        path = ROOT / relative
        if path.suffix != ".md" or not path.is_file():
            continue
        markdown = markdown_link_surface(path.read_text(encoding="utf-8"))
        if re.search(
            r"\[[^\]\r\n]+\][ \t]*\r?\n[ \t]*\([^\r\n)]+\)",
            markdown,
        ):
            errors.append(
                f"malformed multiline Markdown inline link in {path.relative_to(ROOT)}"
            )

        for target in re.findall(r"\]\(([^\s)]+)\)", markdown):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            destination = target.split("#", 1)[0]
            if destination and not (path.parent / destination).exists():
                errors.append(f"broken local link in {path.relative_to(ROOT)}: {target}")

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
