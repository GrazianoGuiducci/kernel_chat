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
        "--replace-adapter",
        action="store_true",
        help="Replace the local configured adapter; does not change installed host instructions.",
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


def write_owned_file(path: Path, content: str, replace: bool) -> str:
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
    if args.preview_adapter:
        print(adapter, end="")
        return 0

    # Resolve all inputs before changing any owned file.
    current = render(current_template, replacements)
    sources = render(sources_template, replacements)
    adapter_preexisting = adapter_output.exists()
    adapter_status = write_owned_file(adapter_output, adapter, args.replace_adapter)
    current_status = write_owned_file(
        ROOT / "state/CURRENT.md",
        current,
        args.replace_state,
    )
    sources_status = write_owned_file(
        ROOT / "state/SOURCES.md",
        sources,
        args.replace_state,
    )

    actual_chars = len(adapter_output.read_text(encoding="utf-8"))
    relative_adapter = adapter_output.relative_to(ROOT).as_posix()
    print(f"adapter={relative_adapter} status={adapter_status} chars={actual_chars}")
    print("HOST UI BOUNDARY: this script does not install or update ChatGPT Custom Instructions.")

    if not adapter_preexisting:
        print(
            "NEXT OPERATOR ACTION FOR ADOPTION: copy the complete text from "
            f"{relative_adapter} into ChatGPT Custom Instructions through the "
            "ChatGPT UI and save it."
        )
        print(
            "Until the operator confirms that UI action, report: "
            "repository configured / host activation pending."
        )
    elif args.replace_adapter:
        print(
            "NEXT OPERATOR ACTION FOR HOST UPDATE: the local configured adapter was "
            f"replaced. To update ChatGPT, copy the complete text from {relative_adapter} "
            "into ChatGPT Custom Instructions through the ChatGPT UI and save it."
        )
        print(
            "Until the operator confirms that UI action, report: "
            "local adapter updated / host instructions unchanged."
        )
    else:
        print("Configured adapter preserved. No host update occurred.")
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
