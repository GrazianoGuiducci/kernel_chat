"""Exercise configuration effects in isolated copies, never in user state."""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
ADAPTER = "adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md"
CURRENT = "state/CURRENT.md"
SOURCES = "state/SOURCES.md"


class ConfigureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory(prefix="kernel-chat-test-")
        self.root = Path(self.directory.name).resolve()
        assert self.root.parent == Path(tempfile.gettempdir()).resolve()
        self.addCleanup(self.directory.cleanup)
        for name in ("scripts", "templates", "adapters"):
            shutil.copytree(
                ROOT / name, self.root / name,
                ignore=shutil.ignore_patterns("__pycache__", "CUSTOM_INSTRUCTIONS_CONFIGURED.md"),
            )

    def run_configure(self, *flags: str) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        return subprocess.run(
            [sys.executable, "-B", str(self.root / "scripts/configure.py"),
             "--github-user", "example-user", "--repository", "my-kernel",
             "--project-name", "Research", "--project-source", "https://example.org/project",
             *flags],
            cwd=self.root, env=env, capture_output=True, text=True, encoding="utf-8",
        )

    def owned_bytes(self) -> dict[str, bytes]:
        return {name: (self.root / name).read_bytes()
                for name in (ADAPTER, CURRENT, SOURCES) if (self.root / name).exists()}

    def customize(self) -> dict[str, bytes]:
        result = self.run_configure()
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in (ADAPTER, CURRENT, SOURCES):
            # Byte preservation includes local newline/customization choices.
            (self.root / name).write_bytes(f"Owner change in {name}\r\n".encode())
        return self.owned_bytes()

    def test_first_configuration_has_both_entry_paths_and_project_state(self) -> None:
        result = self.run_configure()
        self.assertEqual(result.returncode, 0, result.stderr)
        adapter = (self.root / ADAPTER).read_text(encoding="utf-8")
        self.assertIn("example-user/my-kernel", adapter)
        self.assertIn("state/CURRENT.md", adapter)
        self.assertIn("AGENTS.md", adapter)
        self.assertIn("seven days", adapter)
        self.assertIn("Evolution Feedback", adapter)
        self.assertIn("operator consent", adapter)
        self.assertNotIn("{{", adapter)
        self.assertIn("Research", (self.root / CURRENT).read_text(encoding="utf-8"))
        self.assertIn("https://example.org/project", (self.root / SOURCES).read_text(encoding="utf-8"))
        self.assertIn("HOST UI BOUNDARY", result.stdout)
        self.assertIn("NEXT OPERATOR ACTION FOR ADOPTION", result.stdout)
        self.assertIn(ADAPTER, result.stdout)
        self.assertIn("repository configured / host activation pending", result.stdout)

    def test_rerun_preserves_all_owned_bytes_even_with_new_arguments(self) -> None:
        before = self.customize()
        result = self.run_configure("--github-user", "another-user", "--project-name", "Changed")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.owned_bytes(), before)
        self.assertIn("status=kept", result.stdout)
        self.assertIn("Configured adapter preserved. No host update occurred.", result.stdout)
        self.assertNotIn("NEXT OPERATOR ACTION FOR HOST UPDATE", result.stdout)

    def test_replace_adapter_does_not_replace_state(self) -> None:
        before = self.customize()
        result = self.run_configure("--replace-adapter", "--github-user", "another-user")
        self.assertEqual(result.returncode, 0, result.stderr)
        after = self.owned_bytes()
        self.assertIn(b"another-user/my-kernel", after[ADAPTER])
        self.assertNotEqual(after[ADAPTER], before[ADAPTER])
        self.assertEqual(after[CURRENT], before[CURRENT])
        self.assertEqual(after[SOURCES], before[SOURCES])
        self.assertIn("NEXT OPERATOR ACTION FOR HOST UPDATE", result.stdout)
        self.assertIn("local adapter updated / host instructions unchanged", result.stdout)

    def test_replace_state_does_not_replace_adapter(self) -> None:
        before = self.customize()
        result = self.run_configure("--replace-state", "--project-name", "Changed")
        self.assertEqual(result.returncode, 0, result.stderr)
        after = self.owned_bytes()
        self.assertEqual(after[ADAPTER], before[ADAPTER])
        self.assertIn(b"Changed", after[CURRENT])
        self.assertNotEqual(after[SOURCES], before[SOURCES])

    def test_preview_on_new_installation_writes_nothing(self) -> None:
        result = self.run_configure("--preview-adapter")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("example-user/my-kernel", result.stdout)
        self.assertEqual(self.owned_bytes(), {})
        self.assertFalse((self.root / "state").exists())

    def test_preview_preserves_customizations_even_with_replacement_flags(self) -> None:
        before = self.customize()
        result = self.run_configure("--preview-adapter", "--replace-adapter", "--replace-state")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("example-user/my-kernel", result.stdout)
        self.assertEqual(self.owned_bytes(), before)

    def test_invalid_configuration_cannot_overwrite_owned_files(self) -> None:
        before = self.customize()
        result = self.run_configure("--github-user", "../bad", "--replace-adapter", "--replace-state")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.owned_bytes(), before)

    def test_unresolved_state_template_does_not_partially_replace_adapter(self) -> None:
        before = self.customize()
        template = self.root / "templates/state/SOURCES.md"
        template.write_text("{{UNKNOWN_FIELD}}", encoding="utf-8")
        result = self.run_configure("--replace-adapter", "--replace-state")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.owned_bytes(), before)


if __name__ == "__main__":
    unittest.main()
