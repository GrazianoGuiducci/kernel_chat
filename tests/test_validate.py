"""Exercise package validation and instance-drift reporting in isolated copies."""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ValidateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory(prefix="kernel-chat-validate-")
        self.root = Path(self.directory.name).resolve()
        self.addCleanup(self.directory.cleanup)
        shutil.copytree(
            ROOT,
            self.root,
            dirs_exist_ok=True,
            ignore=shutil.ignore_patterns(
                ".git",
                "__pycache__",
                "CUSTOM_INSTRUCTIONS_CONFIGURED.md",
            ),
        )

        # A source-package test copy must retain templates with these names.
        # Remove only configured user state if such files happen to be present
        # in the working checkout.
        for relative in (
            "state/CURRENT.md",
            "state/SOURCES.md",
            "state/INSTANCE.json",
        ):
            path = self.root / relative
            if path.exists():
                path.unlink()

    def run_python(self, *command: str) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        return subprocess.run(
            [sys.executable, "-B", *command],
            cwd=self.root,
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

    def validate(self) -> tuple[subprocess.CompletedProcess[str], dict[str, object]]:
        result = self.run_python("scripts/validate.py")
        payload = json.loads(result.stdout)
        return result, payload

    def configure(self) -> subprocess.CompletedProcess[str]:
        return self.run_python(
            "scripts/configure.py",
            "--github-user", "example-user",
            "--repository", "example-kernel",
        )

    def confirm_host(self) -> subprocess.CompletedProcess[str]:
        return self.run_python(
            "scripts/configure.py",
            "--github-user", "example-user",
            "--repository", "example-kernel",
            "--confirm-host-installation",
        )

    def test_clean_package_is_valid(self) -> None:
        result, payload = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(payload["valid"])
        self.assertEqual(payload["errors"], [])

    def test_adoption_guide_is_part_of_package_contract(self) -> None:
        (self.root / "docs/ADOPTION_GUIDE.md").unlink()
        result, payload = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(
            "missing required file: docs/ADOPTION_GUIDE.md",
            payload["errors"],
        )

    def test_malformed_multiline_markdown_inline_link_is_invalid(self) -> None:
        agents = self.root / "AGENTS.md"
        agents.write_text(
            agents.read_text(encoding="utf-8")
            + "\n[Broken local owner link]\n(kernel/EVOLUTION.md#sense-incongruence-before-closure)\n",
            encoding="utf-8",
        )

        result, payload = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(payload["valid"])
        self.assertIn(
            "malformed multiline Markdown inline link in AGENTS.md",
            payload["errors"],
        )

    def test_markdown_link_validation_ignores_code_examples(self) -> None:
        agents = self.root / "AGENTS.md"
        agents.write_text(
            agents.read_text(encoding="utf-8")
            + "\n```text\n[Example only]\n(missing/example.md)\n```\n"
            + "\nInline syntax example: `](...)`.\n",
            encoding="utf-8",
        )

        result, payload = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(payload["valid"])

    def test_agents_must_keep_mobile_observation_discovery_route(self) -> None:
        agents = self.root / "AGENTS.md"
        text = agents.read_text(encoding="utf-8")
        text = text.replace(
            "kernel/KERNEL.md#mobile-observation-without-losing-the-point",
            "kernel/KERNEL.md",
        )
        agents.write_text(text, encoding="utf-8")

        result, payload = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(payload["valid"])
        self.assertIn(
            "AGENTS.md missing operating discovery route: "
            "kernel/KERNEL.md#mobile-observation-without-losing-the-point",
            payload["errors"],
        )

    def test_missing_local_adapter_is_visible_without_invalidating_instance(self) -> None:
        configured = self.configure()
        self.assertEqual(configured.returncode, 0, configured.stderr)

        adapter = self.root / "adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md"
        adapter.unlink()

        result, payload = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(payload["valid"])
        warnings = "\n".join(payload["warnings"])
        self.assertIn("configured adapter is absent locally", warnings)

    def test_instance_drift_is_reported_without_invalidating_package(self) -> None:
        configured = self.configure()
        self.assertEqual(configured.returncode, 0, configured.stderr)

        # Simulate an adopted instance whose package receipt is now behind the
        # repository and whose configured bridge changed outside the receipt.
        (self.root / "VERSION").write_text("9.9.9\n", encoding="utf-8")
        adapter = self.root / "adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md"
        adapter.write_text(
            adapter.read_text(encoding="utf-8") + "\nOwner customization.\n",
            encoding="utf-8",
        )

        result, payload = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(payload["valid"])
        warnings = "\n".join(payload["warnings"])
        self.assertIn("instance package source differs", warnings)
        self.assertIn("configured bridge digest differs", warnings)

    def test_crlf_only_bridge_change_is_byte_drift(self) -> None:
        configured = self.configure()
        self.assertEqual(configured.returncode, 0, configured.stderr)

        adapter = self.root / "adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md"
        lf_bytes = adapter.read_bytes()
        self.assertIn(b"\n", lf_bytes)
        crlf_bytes = lf_bytes.replace(b"\n", b"\r\n")
        self.assertNotEqual(lf_bytes, crlf_bytes)
        adapter.write_bytes(crlf_bytes)

        result, payload = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(payload["valid"])
        warnings = "\n".join(payload["warnings"])
        self.assertIn("configured bridge digest differs", warnings)

    def test_legacy_v1_receipt_without_new_optional_identity_fields_remains_valid(self) -> None:
        configured = self.configure()
        self.assertEqual(configured.returncode, 0, configured.stderr)

        instance_path = self.root / "state/INSTANCE.json"
        instance = json.loads(instance_path.read_text(encoding="utf-8"))
        instance.pop("configured_bridge_repository", None)
        host = instance["host_installation"]
        host.pop("installed_bridge_repository", None)
        host.pop("installed_bridge_template_version", None)
        instance_path.write_text(json.dumps(instance, indent=2) + "\n", encoding="utf-8")

        result, payload = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(payload["valid"])
        warnings = "\n".join(payload["warnings"])
        self.assertIn("legacy INSTANCE receipt has no configured bridge repository field", warnings)

    def test_unknown_configured_bridge_provenance_is_warning(self) -> None:
        configured = self.configure()
        self.assertEqual(configured.returncode, 0, configured.stderr)

        instance_path = self.root / "state/INSTANCE.json"
        instance = json.loads(instance_path.read_text(encoding="utf-8"))
        instance["configured_bridge_template_version"] = "unknown"
        instance_path.write_text(json.dumps(instance, indent=2) + "\n", encoding="utf-8")

        result, payload = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(payload["valid"])
        warnings = "\n".join(payload["warnings"])
        self.assertIn("configured bridge template provenance is unknown", warnings)

    def test_persisted_configured_repository_mismatch_is_invalid_even_without_bridge(self) -> None:
        configured = self.configure()
        self.assertEqual(configured.returncode, 0, configured.stderr)

        instance_path = self.root / "state/INSTANCE.json"
        instance = json.loads(instance_path.read_text(encoding="utf-8"))
        instance["configured_bridge_repository"] = "other-user/other-kernel"
        instance_path.write_text(json.dumps(instance, indent=2) + "\n", encoding="utf-8")
        (self.root / "adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md").unlink()

        result, payload = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(payload["valid"])
        self.assertIn(
            "state/INSTANCE.json configured_bridge_repository must match instance_repository when its target is known",
            payload["errors"],
        )

    def test_configured_bridge_repository_mismatch_is_warning(self) -> None:
        configured = self.configure()
        self.assertEqual(configured.returncode, 0, configured.stderr)

        adapter = self.root / "adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md"
        text = adapter.read_text(encoding="utf-8")
        text = text.replace(
            "User-owned kernel instance: example-user/example-kernel.",
            "User-owned kernel instance: other-user/other-kernel.",
        )
        adapter.write_text(text, encoding="utf-8")

        result, payload = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(payload["valid"])
        warnings = "\n".join(payload["warnings"])
        self.assertIn("different user-owned repository", warnings)

    def test_confirmed_host_digest_drift_is_warning(self) -> None:
        configured = self.configure()
        self.assertEqual(configured.returncode, 0, configured.stderr)
        confirmed = self.confirm_host()
        self.assertEqual(confirmed.returncode, 0, confirmed.stderr)

        adapter = self.root / "adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md"
        adapter.write_text(
            adapter.read_text(encoding="utf-8") + "\nLocal bridge changed later.\n",
            encoding="utf-8",
        )

        result, payload = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(payload["valid"])
        warnings = "\n".join(payload["warnings"])
        self.assertIn("last operator-confirmed installed bridge digest", warnings)


if __name__ == "__main__":
    unittest.main()
