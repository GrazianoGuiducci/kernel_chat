#!/usr/bin/env python3
"""Dependency-free structural validator for the portable working incarnation.

This validator proves source structure and claim boundaries only.
It does not prove host installation, behavioral activation, assimilation or portability.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "kernel/KERNEL.md",
    "kernel/ROUTING.md",
    "kernel/COMPETENCE.md",
    "state/CURRENT_PRESENT.md",
    "state/ACTIVE.md",
    "operations/CURRENT_STATE.md",
    "operations/flows/README.md",
    "operations/requests/README.md",
    "operations/receipts/README.md",
    "operations/RECOVERY.md",
    "evolution/EVOLUTION.md",
    "evolution/CRYSTALLIZATION.md",
    "adapters/chatgpt/CUSTOM_INSTRUCTIONS.md",
    "adapters/chatgpt/adapter.json",
    "adapters/chatgpt/INSTALLATION_STATE.md",
    "evals/cases.json",
]

PORTABLE_ROOTS = [
    "kernel",
    "state",
    "operations",
    "evolution",
    "adapters",
    "evals",
]

# Build strings in pieces so the validator does not flag its own source.
PRIVATE_RESIDUE_PATTERNS = [
    "Graziano" + "Guiducci/",
    "tm7" + "/chatgpt",
    "chatgpt-" + "operational-environment",
    "C:" + r"\\PVSC\\ANTI_G",
    "/" + "opt/",
    "github_" + "pat_",
    "GRAZIANO_" + "GITHUB_TOKEN",
]


def read_text(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def load_json(relative: str) -> dict:
    return json.loads(read_text(relative))


def portable_files() -> list[Path]:
    files: list[Path] = []
    for relative in PORTABLE_ROOTS:
        base = ROOT / relative
        if not base.exists():
            continue
        files.extend(path for path in base.rglob("*") if path.is_file())
    return files


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required portable file: {relative}")

    if errors:
        return finish(errors, warnings)

    try:
        adapter = load_json("adapters/chatgpt/adapter.json")
    except Exception as exc:  # deterministic human-readable failure
        errors.append(f"invalid adapter json: {exc}")
        adapter = {}

    if adapter.get("behavioral_state") != "unverified":
        errors.append("adapter source must not claim behavioral activation")
    if adapter.get("effect_authority") != "none_by_default":
        errors.append("adapter must keep effect authority none_by_default")
    if adapter.get("persistent_runtime_assumed") is not False:
        errors.append("ChatGPT adapter must not assume a persistent runtime")

    try:
        evals = load_json("evals/cases.json")
    except Exception as exc:
        errors.append(f"invalid eval json: {exc}")
        evals = {}

    cases = evals.get("cases", []) if isinstance(evals, dict) else []
    if len(cases) < 10:
        errors.append("eval set must cover more than a minimal cognitive-only sample")
    kinds = {case.get("kind") for case in cases if isinstance(case, dict)}
    if not any(kind and kind.startswith("operational") for kind in kinds):
        errors.append("eval set must include operational continuity cases")
    if not any(kind and kind.startswith("portability") for kind in kinds):
        errors.append("eval set must include portability cases")
    for case in cases:
        if not isinstance(case, dict):
            errors.append("eval case is not an object")
            continue
        for field in ("id", "kind", "discriminant", "failure", "status"):
            if not case.get(field):
                errors.append(f"incomplete eval case {case.get('id', '<unknown>')}: missing {field}")
        if case.get("status") not in {"not_run", "bound", "superseded"}:
            warnings.append(f"nonstandard eval status in {case.get('id', '<unknown>')}: {case.get('status')}")

    adapter_doc = read_text("adapters/chatgpt/CUSTOM_INSTRUCTIONS.md")
    marker = "## Complete text to install"
    if marker not in adapter_doc:
        errors.append("ChatGPT adapter install section missing")
    else:
        install_text = adapter_doc.split(marker, 1)[1].strip()
        if len(install_text) > 1500:
            errors.append(f"ChatGPT Custom Instructions exceed 1500 characters: {len(install_text)}")
        for placeholder in ("<YOUR_GITHUB_USER>", "<YOUR_REPOSITORY>"):
            if placeholder not in install_text:
                errors.append(f"ChatGPT adapter missing user-owned placeholder: {placeholder}")

    operational_state = read_text("operations/CURRENT_STATE.md")
    if "installed_schedules: none_attested" not in operational_state:
        warnings.append("default operational state does not explicitly keep schedules unattested")
    if "active_flows: none" not in operational_state:
        warnings.append("default operational state contains an active-flow claim; verify it is intentional")

    for path in portable_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(ROOT).as_posix()
        for pattern in PRIVATE_RESIDUE_PATTERNS:
            if re.search(re.escape(pattern), text, flags=re.IGNORECASE):
                errors.append(f"private/origin residue {pattern!r} in portable file {relative}")

    # Claims that source presence must never make automatically.
    forbidden_claims = [
        "behavioral_activation: verified",
        "portability: verified",
        "assimilation: verified",
        "effect_authority: granted_by_default",
    ]
    for path in portable_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(ROOT).as_posix()
        for claim in forbidden_claims:
            if claim.lower() in text.lower():
                errors.append(f"unsupported automatic claim {claim!r} in {relative}")

    return finish(errors, warnings)


def finish(errors: list[str], warnings: list[str]) -> int:
    report = {
        "schema": "meta-semantic-kernel.structural-validation.v0",
        "valid": not errors,
        "proof_scope": "source_structure_and_claim_boundaries_only",
        "behavior_verified": False,
        "portability_verified": False,
        "errors": sorted(set(errors)),
        "warnings": sorted(set(warnings)),
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
