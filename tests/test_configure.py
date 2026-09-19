"""Exercise configuration effects in isolated copies, never in user state."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
ADAPTER = "adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md"
INSTANCE = "state/INSTANCE.json"
CURRENT = "state/CURRENT.md"
SOURCES = "state/SOURCES.md"
LEGACY_FIXTURE = ROOT / "tests/fixtures/kernel_chat_0_5_3"


class ConfigureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory(prefix="kernel-chat-test-")
        self.root = Path(self.directory.name).resolve()
        assert self.root.parent == Path(tempfile.gettempdir()).resolve()
        self.addCleanup(self.directory.cleanup)
        for name in ("scripts", "templates", "adapters"):
            shutil.copytree(
                ROOT / name,
                self.root / name,
                ignore=shutil.ignore_patterns(
                    "__pycache__", "CUSTOM_INSTRUCTIONS_CONFIGURED.md"
                ),
            )
        shutil.copy2(ROOT / "VERSION", self.root / "VERSION")

    def run_configure(
        self, *flags: str, with_project: bool = True
    ) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        command = [
            sys.executable, "-B", str(self.root / "scripts/configure.py"),
            "--github-user", "example-user",
            "--repository", "my-kernel",
        ]
        if with_project:
            command.extend([
                "--project-name", "Research",
                "--project-source", "https://example.org/project",
            ])
        command.extend(flags)
        if (
            "--confirm-host-installation" in flags
            and "--expected-bridge-sha256" not in flags
        ):
            instance = json.loads((self.root / INSTANCE).read_text(encoding="utf-8"))
            command.extend(
                [
                    "--expected-bridge-sha256",
                    str(instance["configured_bridge_sha256"]),
                ]
            )
        return subprocess.run(
            command,
            cwd=self.root,
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

    def owned_bytes(self) -> dict[str, bytes]:
        return {
            name: (self.root / name).read_bytes()
            for name in (ADAPTER, INSTANCE, CURRENT, SOURCES)
            if (self.root / name).exists()
        }

    def package_version(self) -> str:
        return (self.root / "VERSION").read_text(encoding="utf-8").strip()

    def bridge_version(self) -> str:
        return (
            self.root / "adapters/conversational/VERSION"
        ).read_text(encoding="utf-8").strip()

    def test_configured_bridge_uses_portable_conversational_entry(self) -> None:
        result = self.run_configure(with_project=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        configured = (self.root / ADAPTER).read_text(encoding="utf-8")
        self.assertIn(
            "Kernel source: github:example-user/my-kernel.",
            configured,
        )
        self.assertIn("Kernel entry: AGENTS.md", configured)
        self.assertIn("Core logic: kernel/KERNEL.md", configured)
        self.assertIn("Competence field: kernel/COMPETENCE.md", configured)
        self.assertIn("In-flow correction: kernel/FDLA.md", configured)
        self.assertIn("Evolution and learning return: kernel/EVOLUTION.md", configured)
        self.assertIn("kernel/KERNEL.md#kernel-chat-competence-trace", configured)
        self.assertIn("actual competence participation", configured)
        self.assertNotIn("ChatGPT", configured)

    def test_instance_writer_lock_blocks_concurrent_mutation(self) -> None:
        configured = self.run_configure()
        self.assertEqual(configured.returncode, 0, configured.stderr)
        instance_path = self.root / INSTANCE
        before = instance_path.read_bytes()
        lock = self.root / "state/.INSTANCE.write.lock"
        lock.write_text('{"pid": 999, "created_at": "stale-test"}\n', encoding="utf-8")

        blocked = self.run_configure("--refresh-instance", with_project=False)
        self.assertNotEqual(blocked.returncode, 0)
        self.assertIn("INSTANCE write lock already exists", blocked.stderr)
        self.assertEqual(instance_path.read_bytes(), before)

        lock.unlink()
        recovered = self.run_configure("--refresh-instance", with_project=False)
        self.assertEqual(recovered.returncode, 0, recovered.stderr)

    def test_unknown_host_state_is_not_resurrected_by_identical_replacement(self) -> None:
        configured = self.run_configure()
        self.assertEqual(configured.returncode, 0, configured.stderr)
        confirmed = self.run_configure(
            "--confirm-host-installation", with_project=False
        )
        self.assertEqual(confirmed.returncode, 0, confirmed.stderr)

        instance_path = self.root / INSTANCE
        instance = json.loads(instance_path.read_text(encoding="utf-8"))
        instance["host_installation"]["state"] = "unknown"
        instance_path.write_text(json.dumps(instance, indent=2) + "\n", encoding="utf-8")

        replaced = self.run_configure("--replace-adapter", with_project=False)
        self.assertEqual(replaced.returncode, 0, replaced.stderr)
        updated = json.loads(instance_path.read_text(encoding="utf-8"))
        self.assertEqual(
            updated["host_installation"]["state"],
            "local_adapter_updated_host_unconfirmed",
        )

    def test_late_confirmation_cannot_confirm_a_newer_bridge(self) -> None:
        configured = self.run_configure()
        self.assertEqual(configured.returncode, 0, configured.stderr)
        instance_path = self.root / INSTANCE
        original = json.loads(instance_path.read_text(encoding="utf-8"))
        delivered_digest = original["configured_bridge_sha256"]

        template = self.root / "adapters/conversational/INSTRUCTIONS.template.md"
        template.write_text(
            template.read_text(encoding="utf-8") + "\nNew delivered relation.\n",
            encoding="utf-8",
        )
        (self.root / "adapters/conversational/VERSION").write_text("1.0.1\n", encoding="utf-8")
        replaced = self.run_configure("--replace-adapter", with_project=False)
        self.assertEqual(replaced.returncode, 0, replaced.stderr)

        late = self.run_configure(
            "--confirm-host-installation",
            "--expected-bridge-sha256",
            delivered_digest,
            with_project=False,
        )
        self.assertNotEqual(late.returncode, 0)
        self.assertIn("different bridge delivery", late.stderr)
        state = json.loads(instance_path.read_text(encoding="utf-8"))
        self.assertNotEqual(
            state["host_installation"]["state"],
            "installed_operator_confirmed",
        )

    def test_user_values_that_look_like_template_fields_remain_literal(self) -> None:
        result = self.run_configure(
            "--project-name",
            "Study {{DATE}}",
            "--project-source",
            "https://example.org/{{DATE}}",
            with_project=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        current = (self.root / CURRENT).read_text(encoding="utf-8")
        sources = (self.root / SOURCES).read_text(encoding="utf-8")
        self.assertIn("Study {{DATE}}", current)
        self.assertIn("https://example.org/{{DATE}}", sources)

    def test_unrecognized_custom_bridge_does_not_promote_example_identity(self) -> None:
        adapter = self.root / ADAPTER
        adapter.parent.mkdir(parents=True, exist_ok=True)
        adapter.write_text(
            "Work from the present.\n\n"
            "Continuity target: example-user/my-kernel.\n\n"
            "<!-- User-owned kernel instance: fake-user/fake-kernel. -->\n",
            encoding="utf-8",
        )

        result = self.run_configure(with_project=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        instance = json.loads((self.root / INSTANCE).read_text(encoding="utf-8"))
        self.assertEqual(instance["configured_bridge_repository"], "unknown")

    def test_first_configuration_with_project(self) -> None:
        result = self.run_configure()
        self.assertEqual(result.returncode, 0, result.stderr)

        adapter = (self.root / ADAPTER).read_text(encoding="utf-8")
        self.assertIn("example-user/my-kernel", adapter)
        self.assertIn("state/CURRENT.md", adapter)
        self.assertIn("AGENTS.md", adapter)
        self.assertIn("effect authority", adapter)
        self.assertNotIn("seven days", adapter)
        self.assertNotIn("Evolution Feedback", adapter)
        self.assertNotIn("{{", adapter)

        current = (self.root / CURRENT).read_text(encoding="utf-8")
        sources = (self.root / SOURCES).read_text(encoding="utf-8")
        self.assertIn("context_kind: project", current)
        self.assertIn("Research", current)
        self.assertIn("https://example.org/project", sources)

        instance = json.loads((self.root / INSTANCE).read_text(encoding="utf-8"))
        self.assertEqual(instance["schema"], "kernel_chat.instance.v1")
        self.assertEqual(instance["instance_repository"], "example-user/my-kernel")
        self.assertEqual(instance["package_source_version"], self.package_version())
        self.assertEqual(
            instance["available_bridge_template_version"], self.bridge_version()
        )
        self.assertEqual(
            instance["configured_bridge_template_version"], self.bridge_version()
        )
        self.assertEqual(
            instance["configured_bridge_repository"], "example-user/my-kernel"
        )
        self.assertEqual(
            instance["host_installation"]["state"], "pending_operator_confirmation"
        )
        self.assertIsNone(instance["host_installation"]["installed_bridge_sha256"])
        self.assertEqual(len(instance["configured_bridge_sha256"]), 64)

        self.assertIn("HOST UI BOUNDARY", result.stdout)
        self.assertIn("NEXT OPERATOR ACTION FOR ADOPTION", result.stdout)
        expected_confirmation_command = (
            "After that UI action, run:\n"
            "python scripts/configure.py \\\n"
            "  --github-user example-user \\\n"
            "  --repository my-kernel \\\n"
            "  --confirm-host-installation \\\n"
            f"  --expected-bridge-sha256 {instance['configured_bridge_sha256']}"
        )
        self.assertIn(expected_confirmation_command, result.stdout)
        self.assertIn(
            f"confirmation_bridge_sha256={instance['configured_bridge_sha256']}",
            result.stdout,
        )
        self.assertIn("repository configured / host activation pending", result.stdout)

    def test_no_project_configuration(self) -> None:
        result = self.run_configure(with_project=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        current = (self.root / CURRENT).read_text(encoding="utf-8")
        sources = (self.root / SOURCES).read_text(encoding="utf-8")
        self.assertIn("context_kind: none_selected", current)
        self.assertIn("context_name: none selected", current)
        self.assertIn("No initial project or domain source was selected", sources)
        self.assertNotIn("https://example.org/project", sources)

    def test_real_0_5_3_shape_migrates_without_rewriting_user_state(self) -> None:
        adapter_path = self.root / ADAPTER
        adapter_path.parent.mkdir(parents=True, exist_ok=True)
        legacy_bridge = (LEGACY_FIXTURE / "CUSTOM_INSTRUCTIONS_CONFIGURED.md").read_bytes()
        adapter_path.write_bytes(legacy_bridge)

        state_dir = self.root / "state"
        state_dir.mkdir(parents=True, exist_ok=True)
        legacy_current = (LEGACY_FIXTURE / "CURRENT.md").read_bytes()
        legacy_sources = (LEGACY_FIXTURE / "SOURCES.md").read_bytes()
        (self.root / CURRENT).write_bytes(legacy_current)
        (self.root / SOURCES).write_bytes(legacy_sources)

        result = self.run_configure(with_project=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(adapter_path.read_bytes(), legacy_bridge)
        self.assertEqual((self.root / CURRENT).read_bytes(), legacy_current)
        self.assertEqual((self.root / SOURCES).read_bytes(), legacy_sources)

        instance = json.loads((self.root / INSTANCE).read_text(encoding="utf-8"))
        self.assertEqual(instance["package_source_version"], self.package_version())
        self.assertEqual(instance["instance_repository"], "example-user/my-kernel")
        self.assertEqual(
            instance["available_bridge_template_version"], self.bridge_version()
        )
        self.assertEqual(instance["configured_bridge_template_version"], "unknown")
        self.assertEqual(
            instance["configured_bridge_repository"], "example-user/my-kernel"
        )
        self.assertEqual(
            instance["configured_bridge_sha256"],
            hashlib.sha256(legacy_bridge).hexdigest(),
        )
        self.assertEqual(instance["host_installation"]["state"], "unknown")
        self.assertIsNone(instance["host_installation"]["installed_bridge_sha256"])
        self.assertIn("Configured adapter preserved. No host update occurred.", result.stdout)

    def test_real_0_5_3_repository_mismatch_fails_before_writes(self) -> None:
        legacy_bridge = (LEGACY_FIXTURE / "CUSTOM_INSTRUCTIONS_CONFIGURED.md").read_bytes()
        legacy_bridge = legacy_bridge.replace(
            b"example-user/my-kernel", b"other-user/other-kernel"
        )
        adapter_path = self.root / ADAPTER
        adapter_path.parent.mkdir(parents=True, exist_ok=True)
        adapter_path.write_bytes(legacy_bridge)

        state_dir = self.root / "state"
        state_dir.mkdir(parents=True, exist_ok=True)
        legacy_current = (LEGACY_FIXTURE / "CURRENT.md").read_bytes()
        legacy_sources = (LEGACY_FIXTURE / "SOURCES.md").read_bytes()
        (self.root / CURRENT).write_bytes(legacy_current)
        (self.root / SOURCES).write_bytes(legacy_sources)

        before_adapter = adapter_path.read_bytes()
        before_current = (self.root / CURRENT).read_bytes()
        before_sources = (self.root / SOURCES).read_bytes()

        result = self.run_configure(with_project=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("different user-owned repository", result.stderr)
        self.assertFalse((self.root / INSTANCE).exists())
        self.assertEqual(adapter_path.read_bytes(), before_adapter)
        self.assertEqual((self.root / CURRENT).read_bytes(), before_current)
        self.assertEqual((self.root / SOURCES).read_bytes(), before_sources)

    def test_legacy_custom_bridge_without_observable_target_keeps_unknown_identity(self) -> None:
        adapter_path = self.root / ADAPTER
        adapter_path.parent.mkdir(parents=True, exist_ok=True)
        legacy_bridge = b"Custom legacy bridge without repository identity.\n"
        adapter_path.write_bytes(legacy_bridge)

        state_dir = self.root / "state"
        state_dir.mkdir(parents=True, exist_ok=True)
        (self.root / CURRENT).write_text("Legacy current state.\n", encoding="utf-8")
        (self.root / SOURCES).write_text("Legacy sources.\n", encoding="utf-8")

        result = self.run_configure(with_project=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        instance = json.loads((self.root / INSTANCE).read_text(encoding="utf-8"))
        self.assertEqual(instance["configured_bridge_template_version"], "unknown")
        self.assertEqual(instance["configured_bridge_repository"], "unknown")
        self.assertEqual(
            instance["configured_bridge_sha256"],
            hashlib.sha256(legacy_bridge).hexdigest(),
        )

    def test_real_0_5_3_mismatch_can_be_replaced_before_instance_exists(self) -> None:
        legacy_bridge = (LEGACY_FIXTURE / "CUSTOM_INSTRUCTIONS_CONFIGURED.md").read_bytes()
        legacy_bridge = legacy_bridge.replace(
            b"example-user/my-kernel", b"other-user/other-kernel"
        )
        adapter_path = self.root / ADAPTER
        adapter_path.parent.mkdir(parents=True, exist_ok=True)
        adapter_path.write_bytes(legacy_bridge)

        state_dir = self.root / "state"
        state_dir.mkdir(parents=True, exist_ok=True)
        (self.root / CURRENT).write_bytes((LEGACY_FIXTURE / "CURRENT.md").read_bytes())
        (self.root / SOURCES).write_bytes((LEGACY_FIXTURE / "SOURCES.md").read_bytes())

        result = self.run_configure("--replace-adapter", with_project=False)
        self.assertEqual(result.returncode, 0, result.stderr)

        instance = json.loads((self.root / INSTANCE).read_text(encoding="utf-8"))
        self.assertEqual(instance["instance_repository"], "example-user/my-kernel")
        self.assertEqual(instance["configured_bridge_repository"], "example-user/my-kernel")
        self.assertEqual(
            instance["configured_bridge_template_version"], self.bridge_version()
        )
        self.assertEqual(
            instance["host_installation"]["state"],
            "local_adapter_updated_host_unconfirmed",
        )
        configured = adapter_path.read_text(encoding="utf-8")
        self.assertIn("example-user/my-kernel", configured)
        self.assertNotIn("other-user/other-kernel", configured)

    def test_host_confirmation_binds_exact_configured_bridge_digest(self) -> None:
        first = self.run_configure(with_project=False)
        self.assertEqual(first.returncode, 0, first.stderr)

        adapter_before = (self.root / ADAPTER).read_bytes()
        current_before = (self.root / CURRENT).read_bytes()
        sources_before = (self.root / SOURCES).read_bytes()

        result = self.run_configure("--confirm-host-installation", with_project=False)
        self.assertEqual(result.returncode, 0, result.stderr)

        instance = json.loads((self.root / INSTANCE).read_text(encoding="utf-8"))
        expected_digest = hashlib.sha256(adapter_before).hexdigest()
        self.assertEqual(
            instance["host_installation"]["state"], "installed_operator_confirmed"
        )
        self.assertIsNotNone(instance["host_installation"]["confirmed_at"])
        self.assertEqual(
            instance["host_installation"]["installed_bridge_sha256"], expected_digest
        )
        self.assertEqual(
            instance["host_installation"]["installed_bridge_repository"],
            "example-user/my-kernel",
        )
        self.assertEqual(
            instance["host_installation"]["installed_bridge_template_version"],
            self.bridge_version(),
        )
        self.assertIn("+00:00", instance["host_installation"]["confirmed_at"])
        self.assertEqual(instance["configured_bridge_sha256"], expected_digest)
        self.assertEqual((self.root / ADAPTER).read_bytes(), adapter_before)
        self.assertEqual((self.root / CURRENT).read_bytes(), current_before)
        self.assertEqual((self.root / SOURCES).read_bytes(), sources_before)
        self.assertIn("state/INSTANCE.json=host-confirmed", result.stdout)
        self.assertIn("HOST INSTALLATION RECEIPT", result.stdout)

    def test_one_sided_project_arguments_fail_without_writes(self) -> None:
        result = self.run_configure(
            "--project-name", "Research", with_project=False
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must be supplied together", result.stderr)
        self.assertEqual(self.owned_bytes(), {})

    def test_rerun_preserves_owned_bytes(self) -> None:
        first = self.run_configure()
        self.assertEqual(first.returncode, 0, first.stderr)
        before = self.owned_bytes()
        result = self.run_configure(
            "--project-name", "Changed",
            "--project-source", "https://example.org/changed",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.owned_bytes(), before)
        self.assertIn("status=kept", result.stdout)
        self.assertIn("Configured adapter preserved. No host update occurred.", result.stdout)

    def test_replace_adapter_updates_bounded_instance_fields_only(self) -> None:
        first = self.run_configure()
        self.assertEqual(first.returncode, 0, first.stderr)
        confirmed = self.run_configure(
            "--confirm-host-installation", with_project=False
        )
        self.assertEqual(confirmed.returncode, 0, confirmed.stderr)

        current_before = (self.root / CURRENT).read_bytes()
        sources_before = (self.root / SOURCES).read_bytes()

        instance_path = self.root / INSTANCE
        instance = json.loads(instance_path.read_text(encoding="utf-8"))
        installed_digest_before = instance["host_installation"]["installed_bridge_sha256"]
        installed_repository_before = instance["host_installation"]["installed_bridge_repository"]
        installed_template_before = instance["host_installation"]["installed_bridge_template_version"]
        confirmed_at_before = instance["host_installation"]["confirmed_at"]
        instance["source_contact"]["last_observed_revision"] = "abc123"
        instance["source_contact"]["last_observed_at"] = "2026-09-17"
        instance["extension_field"] = {"keep": True}
        instance_path.write_text(json.dumps(instance, indent=2) + "\n", encoding="utf-8")

        template_path = self.root / "adapters/conversational/INSTRUCTIONS.template.md"
        template_path.write_text(
            template_path.read_text(encoding="utf-8") + "\nNew bridge-template relation.\n",
            encoding="utf-8",
        )
        (self.root / "adapters/conversational/VERSION").write_text("1.0.1\n", encoding="utf-8")

        result = self.run_configure(
            "--replace-adapter",
            with_project=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

        self.assertEqual((self.root / CURRENT).read_bytes(), current_before)
        self.assertEqual((self.root / SOURCES).read_bytes(), sources_before)

        updated = json.loads(instance_path.read_text(encoding="utf-8"))
        self.assertEqual(updated["instance_repository"], "example-user/my-kernel")
        self.assertEqual(
            updated["available_bridge_template_version"], self.bridge_version()
        )
        self.assertEqual(
            updated["configured_bridge_template_version"], self.bridge_version()
        )
        self.assertEqual(
            updated["host_installation"]["state"],
            "local_adapter_updated_host_unconfirmed",
        )
        self.assertEqual(
            updated["host_installation"]["installed_bridge_sha256"],
            installed_digest_before,
        )
        self.assertEqual(
            updated["host_installation"]["installed_bridge_repository"],
            installed_repository_before,
        )
        self.assertEqual(
            updated["host_installation"]["installed_bridge_template_version"],
            installed_template_before,
        )
        self.assertEqual(
            updated["host_installation"]["confirmed_at"], confirmed_at_before
        )
        self.assertNotEqual(
            updated["configured_bridge_sha256"], installed_digest_before
        )
        self.assertEqual(
            updated["source_contact"]["last_observed_revision"], "abc123"
        )
        self.assertEqual(updated["extension_field"], {"keep": True})
        self.assertIn("NEXT OPERATOR ACTION FOR HOST UPDATE", result.stdout)
        self.assertIn("local adapter updated / host instructions unchanged", result.stdout)
        expected_confirmation_command = (
            "After that UI action, run:\n"
            "python scripts/configure.py \\\n"
            "  --github-user example-user \\\n"
            "  --repository my-kernel \\\n"
            "  --confirm-host-installation \\\n"
            f"  --expected-bridge-sha256 {updated['configured_bridge_sha256']}"
        )
        self.assertIn(expected_confirmation_command, result.stdout)
        self.assertIn(
            f"confirmation_bridge_sha256={updated['configured_bridge_sha256']}",
            result.stdout,
        )

    def test_replace_adapter_no_change_preserves_confirmed_host_receipt(self) -> None:
        first = self.run_configure(with_project=False)
        self.assertEqual(first.returncode, 0, first.stderr)
        confirmed = self.run_configure("--confirm-host-installation", with_project=False)
        self.assertEqual(confirmed.returncode, 0, confirmed.stderr)

        instance_path = self.root / INSTANCE
        before = json.loads(instance_path.read_text(encoding="utf-8"))
        result = self.run_configure("--replace-adapter", with_project=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        after = json.loads(instance_path.read_text(encoding="utf-8"))

        self.assertEqual(
            after["configured_bridge_sha256"],
            before["configured_bridge_sha256"],
        )
        self.assertEqual(
            after["host_installation"]["state"], "installed_operator_confirmed"
        )
        self.assertEqual(
            after["host_installation"]["installed_bridge_sha256"],
            before["host_installation"]["installed_bridge_sha256"],
        )
        self.assertEqual(
            after["host_installation"]["confirmed_at"],
            before["host_installation"]["confirmed_at"],
        )
        self.assertIn(
            "No ChatGPT UI update is required.",
            result.stdout,
        )
        self.assertNotIn("NEXT OPERATOR ACTION FOR HOST UPDATE", result.stdout)

    def test_refresh_instance_requires_existing_instance(self) -> None:
        result = self.run_configure("--refresh-instance", with_project=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("requires an existing state/INSTANCE.json", result.stderr)
        self.assertEqual(self.owned_bytes(), {})

    def test_existing_instance_missing_adapter_is_not_implicitly_regenerated(self) -> None:
        first = self.run_configure(with_project=False)
        self.assertEqual(first.returncode, 0, first.stderr)
        adapter_path = self.root / ADAPTER
        adapter_path.unlink()

        instance_path = self.root / INSTANCE
        before = json.loads(instance_path.read_text(encoding="utf-8"))
        result = self.run_configure("--refresh-instance", with_project=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(adapter_path.exists())
        after = json.loads(instance_path.read_text(encoding="utf-8"))
        self.assertEqual(
            after["configured_bridge_sha256"], before["configured_bridge_sha256"]
        )
        self.assertEqual(
            after["configured_bridge_repository"], before["configured_bridge_repository"]
        )
        self.assertIn("status=missing-preserved", result.stdout)
        self.assertIn("without regenerating it", result.stdout)

        replacement = self.run_configure("--replace-adapter", with_project=False)
        self.assertEqual(replacement.returncode, 0, replacement.stderr)
        self.assertTrue(adapter_path.exists())

    def test_replace_adapter_does_not_preserve_inconsistent_installed_target(self) -> None:
        first = self.run_configure(with_project=False)
        self.assertEqual(first.returncode, 0, first.stderr)
        confirmed = self.run_configure("--confirm-host-installation", with_project=False)
        self.assertEqual(confirmed.returncode, 0, confirmed.stderr)

        instance_path = self.root / INSTANCE
        instance = json.loads(instance_path.read_text(encoding="utf-8"))
        instance["host_installation"]["installed_bridge_repository"] = "other-user/other-kernel"
        instance_path.write_text(json.dumps(instance, indent=2) + "\n", encoding="utf-8")

        result = self.run_configure("--replace-adapter", with_project=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        updated = json.loads(instance_path.read_text(encoding="utf-8"))
        self.assertEqual(
            updated["host_installation"]["state"],
            "local_adapter_updated_host_unconfirmed",
        )

    def test_existing_instance_rejects_mismatched_command_repository(self) -> None:
        first = self.run_configure(with_project=False)
        self.assertEqual(first.returncode, 0, first.stderr)
        before = self.owned_bytes()

        result = self.run_configure(
            "--github-user", "another-user",
            with_project=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(
            "Command repository identity does not match INSTANCE.instance_repository",
            result.stderr,
        )
        self.assertEqual(self.owned_bytes(), before)

    def test_preview_can_inspect_another_repository_without_rebinding_instance(self) -> None:
        first = self.run_configure(with_project=False)
        self.assertEqual(first.returncode, 0, first.stderr)
        before = self.owned_bytes()

        result = self.run_configure(
            "--preview-adapter",
            "--github-user", "another-user",
            with_project=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("another-user/my-kernel", result.stdout)
        self.assertEqual(self.owned_bytes(), before)

    def test_replace_adapter_cannot_rebind_existing_instance_repository(self) -> None:
        first = self.run_configure()
        self.assertEqual(first.returncode, 0, first.stderr)
        before = self.owned_bytes()

        result = self.run_configure(
            "--replace-adapter",
            "--github-user", "another-user",
            with_project=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(
            "Command repository identity does not match INSTANCE.instance_repository",
            result.stderr,
        )
        self.assertEqual(self.owned_bytes(), before)

    def test_refresh_instance_preserves_configured_provenance_and_observations(self) -> None:
        first = self.run_configure()
        self.assertEqual(first.returncode, 0, first.stderr)
        instance_path = self.root / INSTANCE
        instance = json.loads(instance_path.read_text(encoding="utf-8"))
        instance["source_contact"]["last_observed_revision"] = "abc123"
        instance["configured_bridge_template_version"] = "0.9.0"
        instance_path.write_text(json.dumps(instance, indent=2) + "\n", encoding="utf-8")

        result = self.run_configure(
            "--refresh-instance",
            with_project=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        updated = json.loads(instance_path.read_text(encoding="utf-8"))
        self.assertEqual(updated["instance_repository"], "example-user/my-kernel")
        self.assertEqual(
            updated["source_contact"]["last_observed_revision"], "abc123"
        )
        self.assertEqual(
            updated["available_bridge_template_version"], self.bridge_version()
        )
        self.assertEqual(updated["configured_bridge_template_version"], "0.9.0")
        self.assertEqual(
            updated["host_installation"]["state"], "pending_operator_confirmation"
        )
        self.assertIsNone(updated["host_installation"]["installed_bridge_sha256"])
        self.assertIn("state/INSTANCE.json=refreshed", result.stdout)

    def test_refresh_instance_does_not_accept_manual_bridge_drift(self) -> None:
        first = self.run_configure(with_project=False)
        self.assertEqual(first.returncode, 0, first.stderr)

        instance_path = self.root / INSTANCE
        before = json.loads(instance_path.read_text(encoding="utf-8"))
        adapter_path = self.root / ADAPTER
        adapter_path.write_bytes(
            adapter_path.read_bytes() + b"\nManual local customization.\n"
        )

        result = self.run_configure("--refresh-instance", with_project=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        after = json.loads(instance_path.read_text(encoding="utf-8"))
        self.assertEqual(
            after["configured_bridge_sha256"], before["configured_bridge_sha256"]
        )
        self.assertEqual(
            after["configured_bridge_template_version"],
            before["configured_bridge_template_version"],
        )
        self.assertEqual(
            after["configured_bridge_repository"],
            before["configured_bridge_repository"],
        )
        observed_digest = hashlib.sha256(adapter_path.read_bytes()).hexdigest()
        self.assertIn(
            f"observed_local_bridge_sha256={observed_digest}",
            result.stdout,
        )
        self.assertNotIn("confirmation_bridge_sha256=", result.stdout)
        self.assertIn("LOCAL BRIDGE DRIFT", result.stdout)
        self.assertIn("HOST DELIVERY BLOCKED", result.stdout)
        self.assertNotIn("may copy the reconciled", result.stdout)

    def test_host_confirmation_refuses_unreconciled_local_bridge_drift(self) -> None:
        first = self.run_configure(with_project=False)
        self.assertEqual(first.returncode, 0, first.stderr)

        instance_path = self.root / INSTANCE
        instance_before = instance_path.read_bytes()
        adapter_path = self.root / ADAPTER
        adapter_path.write_bytes(
            adapter_path.read_bytes() + b"\nManual local customization.\n"
        )

        result = self.run_configure("--confirm-host-installation", with_project=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cannot reconcile local artifact drift", result.stderr)
        self.assertEqual(instance_path.read_bytes(), instance_before)

    def test_replace_state_does_not_replace_adapter_or_instance(self) -> None:
        first = self.run_configure()
        self.assertEqual(first.returncode, 0, first.stderr)
        adapter_before = (self.root / ADAPTER).read_bytes()
        instance_before = (self.root / INSTANCE).read_bytes()

        result = self.run_configure(
            "--replace-state",
            "--project-name", "Changed",
            "--project-source", "https://example.org/changed",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.root / ADAPTER).read_bytes(), adapter_before)
        self.assertEqual((self.root / INSTANCE).read_bytes(), instance_before)
        self.assertIn(b"Changed", (self.root / CURRENT).read_bytes())
        self.assertIn(b"https://example.org/changed", (self.root / SOURCES).read_bytes())

    def test_preview_writes_nothing(self) -> None:
        result = self.run_configure("--preview-adapter", with_project=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("example-user/my-kernel", result.stdout)
        self.assertEqual(self.owned_bytes(), {})

    def test_invalid_configuration_cannot_overwrite_owned_files(self) -> None:
        first = self.run_configure()
        self.assertEqual(first.returncode, 0, first.stderr)
        before = self.owned_bytes()
        result = self.run_configure(
            "--github-user", "../bad",
            "--replace-adapter",
            "--replace-state",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.owned_bytes(), before)

    def test_invalid_instance_blocks_adapter_replacement_before_writes(self) -> None:
        first = self.run_configure()
        self.assertEqual(first.returncode, 0, first.stderr)
        before_adapter = (self.root / ADAPTER).read_bytes()
        (self.root / INSTANCE).write_text("{bad json", encoding="utf-8")

        result = self.run_configure(
            "--replace-adapter",
            "--github-user", "another-user",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((self.root / ADAPTER).read_bytes(), before_adapter)

    def test_unresolved_state_template_does_not_partially_replace_adapter(self) -> None:
        first = self.run_configure()
        self.assertEqual(first.returncode, 0, first.stderr)
        before = self.owned_bytes()
        template = self.root / "templates/state/SOURCES.md"
        template.write_text("{{UNKNOWN_FIELD}}", encoding="utf-8")
        result = self.run_configure("--replace-adapter", "--replace-state")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.owned_bytes(), before)


    def configure_module(self):
        spec = importlib.util.spec_from_file_location(
            "kernel_chat_configure_under_test",
            self.root / "scripts/configure.py",
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_atomic_write_replace_failure_preserves_existing_file(self) -> None:
        module = self.configure_module()
        target = self.root / INSTANCE
        target.parent.mkdir(parents=True, exist_ok=True)
        original = b'{"receipt":"preserve-me"}\n'
        target.write_bytes(original)

        with mock.patch.object(module.os, "replace", side_effect=OSError("replace failed")):
            with self.assertRaises(OSError):
                module.atomic_write_text(target, '{"receipt":"new"}\n')

        self.assertEqual(target.read_bytes(), original)
        leftovers = list(target.parent.glob(f".{target.name}.*.tmp"))
        self.assertEqual(leftovers, [])

    def test_refresh_rejects_unsupported_instance_schema_before_writes(self) -> None:
        first = self.run_configure(with_project=False)
        self.assertEqual(first.returncode, 0, first.stderr)

        instance_path = self.root / INSTANCE
        instance = json.loads(instance_path.read_text(encoding="utf-8"))
        instance["schema"] = "kernel_chat.instance.v2"
        instance["host_adapter"] = "future-host"
        instance["host_installation"] = ["opaque-future-shape"]
        instance["source_contact"] = "opaque-future-shape"
        instance_path.write_text(json.dumps(instance, indent=2) + "\n", encoding="utf-8")
        before = self.owned_bytes()

        result = self.run_configure("--refresh-instance", with_project=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Unsupported instance schema", result.stderr)
        self.assertEqual(self.owned_bytes(), before)

    def test_replace_adapter_return_to_confirmed_identity_restores_confirmation(self) -> None:
        first = self.run_configure(with_project=False)
        self.assertEqual(first.returncode, 0, first.stderr)
        confirmed = self.run_configure("--confirm-host-installation", with_project=False)
        self.assertEqual(confirmed.returncode, 0, confirmed.stderr)

        instance_path = self.root / INSTANCE
        confirmed_instance = json.loads(instance_path.read_text(encoding="utf-8"))
        confirmed_at = confirmed_instance["host_installation"]["confirmed_at"]
        installed_digest = confirmed_instance["host_installation"]["installed_bridge_sha256"]

        template_path = self.root / "adapters/conversational/INSTRUCTIONS.template.md"
        version_path = self.root / "adapters/conversational/VERSION"
        template_a = template_path.read_bytes()
        version_a = version_path.read_bytes()

        template_path.write_bytes(template_a + b"\nTemporary B relation.\n")
        version_path.write_text("1.0.1\n", encoding="utf-8")
        to_b = self.run_configure("--replace-adapter", with_project=False)
        self.assertEqual(to_b.returncode, 0, to_b.stderr)
        middle = json.loads(instance_path.read_text(encoding="utf-8"))
        self.assertEqual(
            middle["host_installation"]["state"],
            "local_adapter_updated_host_unconfirmed",
        )

        template_path.write_bytes(template_a)
        version_path.write_bytes(version_a)
        back_to_a = self.run_configure("--replace-adapter", with_project=False)
        self.assertEqual(back_to_a.returncode, 0, back_to_a.stderr)

        final = json.loads(instance_path.read_text(encoding="utf-8"))
        self.assertEqual(
            final["configured_bridge_sha256"],
            installed_digest,
        )
        self.assertEqual(
            final["host_installation"]["state"],
            "installed_operator_confirmed",
        )
        self.assertEqual(
            final["host_installation"]["confirmed_at"],
            confirmed_at,
        )
        self.assertIn("No ChatGPT UI update is required.", back_to_a.stdout)
        self.assertNotIn("NEXT OPERATOR ACTION FOR HOST UPDATE", back_to_a.stdout)

    def test_preview_is_not_blocked_by_mismatched_existing_bridge(self) -> None:
        first = self.run_configure(with_project=False)
        self.assertEqual(first.returncode, 0, first.stderr)

        adapter = self.root / ADAPTER
        adapter.write_text(
            adapter.read_text(encoding="utf-8").replace(
                "example-user/my-kernel",
                "other-user/other-kernel",
            ),
            encoding="utf-8",
        )
        before = self.owned_bytes()

        result = self.run_configure("--preview-adapter", with_project=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("example-user/my-kernel", result.stdout)
        self.assertEqual(self.owned_bytes(), before)

    def test_preview_is_not_blocked_by_non_utf8_existing_bridge(self) -> None:
        first = self.run_configure(with_project=False)
        self.assertEqual(first.returncode, 0, first.stderr)

        adapter = self.root / ADAPTER
        adapter.write_bytes(b"\xff\xfeinvalid legacy bytes")
        before = self.owned_bytes()

        result = self.run_configure("--preview-adapter", with_project=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("example-user/my-kernel", result.stdout)
        self.assertEqual(self.owned_bytes(), before)

    def test_github_repository_identity_is_case_insensitive(self) -> None:
        first = self.run_configure(with_project=False)
        self.assertEqual(first.returncode, 0, first.stderr)

        refreshed = self.run_configure(
            "--refresh-instance",
            "--github-user", "Example-User",
            "--repository", "My-Kernel",
            with_project=False,
        )
        self.assertEqual(refreshed.returncode, 0, refreshed.stderr)

        confirmed = self.run_configure(
            "--confirm-host-installation",
            "--github-user", "EXAMPLE-USER",
            "--repository", "MY-KERNEL",
            with_project=False,
        )
        self.assertEqual(confirmed.returncode, 0, confirmed.stderr)

    def test_refresh_preserves_missing_user_state_until_explicit_replacement(self) -> None:
        first = self.run_configure()
        self.assertEqual(first.returncode, 0, first.stderr)

        (self.root / CURRENT).unlink()
        (self.root / SOURCES).unlink()

        refreshed = self.run_configure("--refresh-instance", with_project=False)
        self.assertEqual(refreshed.returncode, 0, refreshed.stderr)
        self.assertFalse((self.root / CURRENT).exists())
        self.assertFalse((self.root / SOURCES).exists())
        self.assertIn("state/CURRENT.md=missing-preserved", refreshed.stdout)
        self.assertIn("state/SOURCES.md=missing-preserved", refreshed.stdout)

        restored = self.run_configure("--replace-state", with_project=False)
        self.assertEqual(restored.returncode, 0, restored.stderr)
        self.assertTrue((self.root / CURRENT).exists())
        self.assertTrue((self.root / SOURCES).exists())
        self.assertIn("context_kind: none_selected", (self.root / CURRENT).read_text(encoding="utf-8"))

    def test_preview_ignores_unsupported_instance_schema(self) -> None:
        first = self.run_configure(with_project=False)
        self.assertEqual(first.returncode, 0, first.stderr)

        instance_path = self.root / INSTANCE
        instance = json.loads(instance_path.read_text(encoding="utf-8"))
        instance["schema"] = "kernel_chat.instance.v2"
        instance["host_adapter"] = "future-host"
        instance_path.write_text(json.dumps(instance, indent=2) + "\n", encoding="utf-8")
        before = self.owned_bytes()

        result = self.run_configure(
            "--preview-adapter",
            "--github-user", "another-user",
            "--repository", "another-kernel",
            with_project=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("another-user/another-kernel", result.stdout)
        self.assertEqual(self.owned_bytes(), before)


if __name__ == "__main__":
    unittest.main()
