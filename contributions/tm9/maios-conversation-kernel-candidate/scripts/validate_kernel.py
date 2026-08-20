#!/usr/bin/env python3
"""Dependency-free structural validator for MAIOS Conversation Kernel."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "AGENTS.md",
    "CURRENT_STATE.md",
    "KERNEL.md",
    "capabilities/manifest.json",
    "schemas/capability-manifest.schema.json",
    "adapters/chatgpt/CUSTOM_INSTRUCTIONS.md",
    "adapters/chatgpt/adapter.json",
    "evals/cases.json",
    ".repokernel/meta/PROJECT_META_FACULTY.json",
    ".repokernel/orientation/PROBLEM_POSSIBILITY_SEED.json",
    ".repokernel/skills/maios-conversation-kernel-semantic-kernel/SKILL.md",
]

PRIVATE_RESIDUE = [
    r"C:" + r"\\PVSC\\ANTI_G",
    "/" + "opt/",
    "GRAZIANO_" + "GITHUB_TOKEN",
    "github_" + "pat_",
    "tm7" + "/chatgpt",
    "tm2" + "/anti-g-capability-field",
    "tm3" + "/tm2-relational-comparison",
]


def load_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    if errors:
        return finish(errors)

    capability = load_json("capabilities/manifest.json")
    if capability.get("world_model") != "open":
        errors.append("capability field must declare world_model=open")
    if capability.get("effect_authority") != "none_by_default":
        errors.append("capability field must keep effect authority separate")
    if not capability.get("extension_rule"):
        errors.append("capability field needs an extension rule")

    meta = load_json(".repokernel/meta/PROJECT_META_FACULTY.json")
    if meta.get("open_world") is not True:
        errors.append("generated Project Meta-Faculty must remain open_world")
    if meta.get("effect_authority") != "none":
        errors.append("generated Project Meta-Faculty must not gain effect authority")

    adapter = load_json("adapters/chatgpt/adapter.json")
    if adapter.get("behavioral_state") != "unverified":
        errors.append("source repository must not claim ChatGPT behavioral activation")

    adapter_doc = (ROOT / "adapters/chatgpt/CUSTOM_INSTRUCTIONS.md").read_text(encoding="utf-8")
    parts = adapter_doc.split("## Text to install", 1)
    if len(parts) != 2:
        errors.append("Custom Instructions install section missing")
    else:
        install_text = parts[1].strip()
        if len(install_text) > 1500:
            errors.append(f"Custom Instructions exceed portable target: {len(install_text)}")
        if "<YOUR_GITHUB_USER>" not in install_text:
            errors.append("Custom Instructions must retain the user-owned repository placeholder")

    evals = load_json("evals/cases.json")
    cases = evals.get("cases", [])
    kinds = {case.get("kind") for case in cases if isinstance(case, dict)}
    if len(cases) < 5:
        errors.append("behavioral eval set is too small")
    if not {"positive", "negative_verified_limit", "negative_authority"}.issubset(kinds):
        errors.append("behavioral evals must include positive and both negative classes")
    for case in cases:
        if not all(case.get(field) for field in ("id", "input", "discriminant", "failure")):
            errors.append(f"incomplete eval case: {case.get('id', '<unknown>')}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(ROOT).as_posix()
        for pattern in PRIVATE_RESIDUE:
            if re.search(pattern, text, flags=re.IGNORECASE):
                errors.append(f"private residue pattern {pattern!r} in {relative}")

    return finish(errors)


def finish(errors: list[str]) -> int:
    report = {
        "schema": "maios.conversation-kernel.validation.v1",
        "valid": not errors,
        "errors": sorted(set(errors)),
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
