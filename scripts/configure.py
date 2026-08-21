#!/usr/bin/env python3
"""Configure the ChatGPT adapter and initialize user-owned project state."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = re.compile(r"^[A-Za-z0-9_.-]+$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Configure kernel_chat for a GitHub fork and first project."
    )
    parser.add_argument("--github-user", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--project-name", required=True)
    parser.add_argument("--project-source", required=True)
    parser.add_argument(
        "--replace-state",
        action="store_true",
        help="Replace state/CURRENT.md and state/SOURCES.md if they exist.",
    )
    return parser.parse_args()


def validate_slug(value: str, label: str) -> None:
    if not SLUG.fullmatch(value):
        raise SystemExit(f"{label} contains unsupported characters: {value!r}")


def render(path: Path, replacements: dict[str, str]) -> str:
    text = path.read_text(encoding="utf-8")
    for key, value in replacements.items():
        text = text.replace("{{" + key + "}}", value)
    unresolved = sorted(set(re.findall(r"{{[A-Z_]+}}", text)))
    if unresolved:
        raise SystemExit(f"Unresolved template fields in {path}: {unresolved}")
    return text


def write_state(path: Path, content: str, replace: bool) -> str:
    if path.exists() and not replace:
        return "kept"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    return "written"


def main() -> int:
    args = parse_args()
    validate_slug(args.github_user, "--github-user")
    validate_slug(args.repository, "--repository")

    replacements = {
        "GITHUB_USER": args.github_user,
        "REPOSITORY": args.repository,
        "PROJECT_NAME": args.project_name.strip(),
        "PROJECT_SOURCE": args.project_source.strip(),
        "DATE": date.today().isoformat(),
    }
    if not replacements["PROJECT_NAME"] or not replacements["PROJECT_SOURCE"]:
        raise SystemExit("Project name and source must not be empty.")

    adapter_template = ROOT / "adapters/chatgpt/CUSTOM_INSTRUCTIONS.template.md"
    adapter_output = ROOT / "adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md"
    current_template = ROOT / "templates/state/CURRENT.md"
    sources_template = ROOT / "templates/state/SOURCES.md"

    adapter = render(adapter_template, replacements)
    adapter_output.write_text(adapter, encoding="utf-8", newline="\n")

    current_status = write_state(
        ROOT / "state/CURRENT.md",
        render(current_template, replacements),
        args.replace_state,
    )
    sources_status = write_state(
        ROOT / "state/SOURCES.md",
        render(sources_template, replacements),
        args.replace_state,
    )

    print(f"adapter={adapter_output.relative_to(ROOT)} chars={len(adapter)}")
    print(f"state/CURRENT.md={current_status}")
    print(f"state/SOURCES.md={sources_status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
