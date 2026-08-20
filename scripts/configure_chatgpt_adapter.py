#!/usr/bin/env python3
"""Configure the ChatGPT adapter for a user-owned GitHub repository.

This command is deterministic and offline. It writes source configuration only;
it does not install the adapter, connect GitHub or claim behavioral activation.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "adapters" / "chatgpt" / "CUSTOM_INSTRUCTIONS.md"
OUTPUT = ROOT / "adapters" / "chatgpt" / "CUSTOM_INSTRUCTIONS_CONFIGURED.md"
INSTALL_MARKER = "## Complete text to install"
MAX_INSTALL_LENGTH = 1500
GITHUB_USER_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})$")
REPOSITORY_RE = re.compile(r"^[A-Za-z0-9_.-]+$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Configure the ChatGPT adapter without network or host effects."
    )
    parser.add_argument("--github-user", required=True)
    parser.add_argument("--repository", required=True)
    return parser.parse_args()


def validate_coordinate(value: str, pattern: re.Pattern[str], label: str) -> str:
    if not pattern.fullmatch(value):
        raise ValueError(f"invalid {label}: {value!r}")
    if value in {".", ".."}:
        raise ValueError(f"invalid {label}: {value!r}")
    return value


def install_text(document: str) -> str:
    if INSTALL_MARKER not in document:
        raise ValueError(f"template is missing {INSTALL_MARKER!r}")
    return document.split(INSTALL_MARKER, 1)[1].strip()


def configure(github_user: str, repository: str) -> dict[str, object]:
    github_user = validate_coordinate(github_user, GITHUB_USER_RE, "GitHub user")
    repository = validate_coordinate(repository, REPOSITORY_RE, "repository")

    template = TEMPLATE.read_text(encoding="utf-8")
    for placeholder in ("<YOUR_GITHUB_USER>", "<YOUR_REPOSITORY>"):
        if template.count(placeholder) != 2:
            raise ValueError(
                f"expected placeholder {placeholder!r} exactly twice in template"
            )

    configured = template.replace("<YOUR_GITHUB_USER>", github_user).replace(
        "<YOUR_REPOSITORY>", repository
    )
    configured_text = install_text(configured)
    configured_length = len(configured_text)
    if configured_length > MAX_INSTALL_LENGTH:
        raise ValueError(
            f"configured install text exceeds {MAX_INSTALL_LENGTH} characters: "
            f"{configured_length}"
        )

    header = (
        "# ChatGPT Adapter — Configured Fork Source\n\n"
        "Status: source_configured; installation and behavioral activation unverified\n\n"
    )
    configured_body = configured.split(INSTALL_MARKER, 1)[1].strip()
    OUTPUT.write_text(
        f"{header}{INSTALL_MARKER}\n\n{configured_body}\n", encoding="utf-8"
    )

    return {
        "schema": "meta-semantic-kernel.chatgpt-adapter-configuration.v0",
        "configured": True,
        "network_access": False,
        "host_installation": "not_performed",
        "behavioral_activation": "unverified",
        "repository_binding": f"{github_user}/{repository}",
        "output": OUTPUT.relative_to(ROOT).as_posix(),
        "install_text_length": configured_length,
        "install_text_limit": MAX_INSTALL_LENGTH,
    }


def main() -> int:
    try:
        result = configure(**vars(parse_args()))
    except (OSError, ValueError) as exc:
        print(json.dumps({"configured": False, "error": str(exc)}, ensure_ascii=False))
        return 1

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
