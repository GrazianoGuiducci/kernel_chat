#!/usr/bin/env python3
"""Dependency-free structural validation for kernel_chat."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "INSTALL.md",
    "AGENTS.md",
    "CURRENT_STATE.md",
    "VERSION",
    "LICENSE",
    "kernel/KERNEL.md",
    "kernel/COMPETENCE.md",
    "kernel/FDLA.md",
    "kernel/EVOLUTION.md",
    "adapters/chatgpt/CUSTOM_INSTRUCTIONS.template.md",
    "templates/state/CURRENT.md",
    "templates/state/SOURCES.md",
    "scripts/configure.py",
]


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    version_path = ROOT / "VERSION"
    if version_path.is_file():
        version = version_path.read_text(encoding="utf-8").strip()
        if not re.fullmatch(r"\d+\.\d+\.\d+", version):
            errors.append(f"VERSION is not semantic: {version!r}")

    adapter_template = ROOT / "adapters/chatgpt/CUSTOM_INSTRUCTIONS.template.md"
    if adapter_template.is_file():
        template = adapter_template.read_text(encoding="utf-8")
        for marker in ("{{GITHUB_USER}}", "{{REPOSITORY}}"):
            if template.count(marker) != 1:
                errors.append(f"adapter template must contain {marker} once")

    configured = ROOT / "adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md"
    if configured.exists():
        text = configured.read_text(encoding="utf-8")
        if re.search(r"{{[A-Z_]+}}", text):
            errors.append("configured adapter contains unresolved fields")
        warnings.append(f"configured adapter present locally ({len(text)} chars)")

    for relative in ("state/CURRENT.md", "state/SOURCES.md"):
        path = ROOT / relative
        if path.exists() and re.search(
            r"{{[A-Z_]+}}", path.read_text(encoding="utf-8")
        ):
            errors.append(f"configured state contains unresolved fields: {relative}")

    result = {
        "valid": not errors,
        "version": version_path.read_text(encoding="utf-8").strip()
        if version_path.is_file()
        else None,
        "errors": errors,
        "warnings": warnings,
        "scope": "repository structure and configured artifacts; not host behavior",
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
