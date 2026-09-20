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
        instance = json.loads(
            (self.root / "state/INSTANCE.json").read_text(encoding="utf-8")
        )
        return self.run_python(
            "scripts/configure.py",
            "--github-user", "example-user",
            "--repository", "example-kernel",
            "--confirm-host-installation",
            "--expected-bridge-sha256",
            str(instance["configured_bridge_sha256"]),
        )

    def test_clean_package_is_valid(self) -> None:
        result, payload = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(payload["valid"])
        self.assertEqual(payload["errors"], [])

    def test_portable_instruction_source_is_required(self) -> None:
        (self.root / "adapters/portable/INSTRUCTIONS.template.md").unlink()
        result, payload = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(
            "missing required file: adapters/portable/INSTRUCTIONS.template.md",
            payload["errors"],
        )

    def test_adoption_guide_is_part_of_package_contract(self) -> None:
        (self.root / "docs/ADOPTION_GUIDE.md").unlink()
        result, payload = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(
            "missing required file: docs/ADOPTION_GUIDE.md",
            payload["errors"],
        )

    def test_agents_must_keep_mobile_observation_discovery_route(self) -> None:
        agents = self.root / "AGENTS.md"
        text = agents.read_text(encoding="utf-8")
        route = "kernel/KERNEL.md#kernel-chat-mobile-observation"
        text = text.replace(
            f"- `{route}`",
            "- `kernel/KERNEL.md`",
        )
        agents.write_text(text, encoding="utf-8")

        result, payload = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(payload["valid"])
        self.assertIn(
            "AGENTS.md missing structural discovery route: "
            "kernel/KERNEL.md#kernel-chat-mobile-observation",
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
            "Kernel source: github:example-user/example-kernel.",
            "Kernel source: github:other-user/other-kernel.",
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

    def test_confirmed_receipt_same_digest_conflicting_target_is_invalid_without_bridge(self) -> None:
        configured = self.configure()
        self.assertEqual(configured.returncode, 0, configured.stderr)
        confirmed = self.confirm_host()
        self.assertEqual(confirmed.returncode, 0, confirmed.stderr)

        instance_path = self.root / "state/INSTANCE.json"
        instance = json.loads(instance_path.read_text(encoding="utf-8"))
        instance["host_installation"]["installed_bridge_repository"] = "other-user/other-kernel"
        instance_path.write_text(json.dumps(instance, indent=2) + "\n", encoding="utf-8")
        (self.root / "adapters/chatgpt/CUSTOM_INSTRUCTIONS_CONFIGURED.md").unlink()

        result, payload = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(payload["valid"])
        self.assertIn(
            "state/INSTANCE.json same bridge digest has conflicting configured/installed repository identities",
            payload["errors"],
        )

    def test_confirmed_receipt_requires_confirmation_time(self) -> None:
        configured = self.configure()
        self.assertEqual(configured.returncode, 0, configured.stderr)
        confirmed = self.confirm_host()
        self.assertEqual(confirmed.returncode, 0, confirmed.stderr)

        instance_path = self.root / "state/INSTANCE.json"
        instance = json.loads(instance_path.read_text(encoding="utf-8"))
        instance["host_installation"]["confirmed_at"] = None
        instance_path.write_text(json.dumps(instance, indent=2) + "\n", encoding="utf-8")

        result, payload = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(payload["valid"])
        self.assertIn(
            "state/INSTANCE.json installed_operator_confirmed requires confirmed_at",
            payload["errors"],
        )

    def test_discovery_route_requires_destination_anchor(self) -> None:
        core = self.root / "kernel/KERNEL.md"
        core.write_text(
            core.read_text(encoding="utf-8").replace(
                '<a name="kernel-chat-mobile-observation"></a>',
                '<a name="kernel-chat-mobile-observation-moved"></a>',
            ),
            encoding="utf-8",
        )

        result, payload = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(payload["valid"])
        self.assertIn(
            "AGENTS.md discovery route owner marker is missing: "
            "kernel/KERNEL.md#kernel-chat-mobile-observation",
            payload["errors"],
        )

    def test_discovery_route_inside_html_comment_does_not_count(self) -> None:
        agents = self.root / "AGENTS.md"
        text_value = agents.read_text(encoding="utf-8")
        route = "kernel/KERNEL.md#kernel-chat-mobile-observation"
        text_value = text_value.replace(f"- `{route}`", "")
        text_value += f"\n<!-- - `{route}` -->\n"
        agents.write_text(text_value, encoding="utf-8")

        result, payload = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(payload["valid"])
        self.assertIn(
            "AGENTS.md missing structural discovery route: " + route,
            payload["errors"],
        )

    def test_public_readme_routes_setup_and_first_use(self) -> None:
        # Public navigation is checked on active Markdown links. Headings and
        # explanatory wording can evolve without becoming product invariants.
        from markdown_it import MarkdownIt

        def links(text: str) -> set[str]:
            return {
                str(child.attrGet("href"))
                for token in MarkdownIt("commonmark").parse(text)
                for child in (token.children or [])
                if child.type == "link_open"
            }

        readme = (self.root / "README.md").read_text(encoding="utf-8")
        readme_links = links(readme)
        for target in (
            "docs/SETUP.md", "docs/ADOPTION_GUIDE.md", "docs/USER_GUIDE.md",
            "kernel/KERNEL.md", "INSTALL.md", "adapters/chatgpt/README.md",
            "adapters/portable/INSTRUCTIONS.template.md",
            "https://github.com/GrazianoGuiducci/maios-project-kernel",
        ):
            with self.subTest(target=target):
                self.assertIn(target, readme_links)

        value_position = readme.index("## What you get")
        example_position = readme.index("## A small before / after")
        capability_position = readme.index("## Capabilities and where to verify them")
        clarification_position = readme.index("## Useful clarifications")
        check_position = readme.index("## Check it directly")
        setup_position = readme.index("## Start using it")
        deep_position = readme.index("## Go deeper")
        reading_position = readme.index("## Reading path")

        self.assertLess(value_position, example_position)
        self.assertLess(example_position, capability_position)
        self.assertLess(capability_position, clarification_position)
        self.assertLess(clarification_position, check_position)
        self.assertLess(check_position, setup_position)
        self.assertLess(setup_position, deep_position)
        self.assertLess(deep_position, reading_position)

        opening = readme[:capability_position]
        self.assertIn("carry forward the ways of working it", opening)
        self.assertIn("Experience can become capability.", opening)
        self.assertIn("including a chat", opening)
        self.assertIn("GitHub, MCP", opening)
        self.assertIn("system-level properties often implemented in agentic", opening)
        self.assertIn("changed handling of task B", opening)
        for provider_name in ("ChatGPT", "Claude", "Codex", "OpenCode"):
            with self.subTest(provider_name=provider_name):
                self.assertNotIn(provider_name, opening)

        verification_surface = readme[capability_position:setup_position]
        for marker in (
            "Present-first continuity",
            "Selective source reentry",
            "Situated competences",
            "Learning return",
            "Revision through later use",
            "Source / inference distinction",
            "In-flow correction",
            "Competence trace",
            "Provider-neutral portable entry",
            "Receiver-relative adoption",
            "Current package evidence",
            "The deeper terminology is optional for normal use",
            "## Check it directly",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, verification_surface)

        portable = (self.root / "adapters/portable/README.md").read_text(encoding="utf-8")
        self.assertIn("A chat is one possible receiving environment", portable)
        self.assertIn("GitHub, MCP", portable)

        setup = (self.root / "docs/SETUP.md").read_text(encoding="utf-8")
        self.assertIn("A host-specific adapter is optional.", setup)
        setup_links = links(setup)
        for target in (
            "../AGENTS.md", "../kernel/KERNEL.md", "../kernel/COMPETENCE.md",
            "../kernel/EVOLUTION.md", "../kernel/FDLA.md", "../INSTALL.md",
            "../adapters/portable/INSTRUCTIONS.template.md",
            "../templates/state/CURRENT.md", "../templates/state/SOURCES.md",
            "USER_GUIDE.md", "ADOPTION_GUIDE.md",
        ):
            with self.subTest(setup_target=target):
                self.assertIn(target, setup_links)
                self.assertTrue((self.root / "docs" / target).is_file())

        agents_text = (self.root / "AGENTS.md").read_text(encoding="utf-8")
        agents_links = links(agents_text)
        self.assertIn("docs/SETUP.md", agents_links)

        portable_entry = (
            self.root / "adapters/portable/INSTRUCTIONS.template.md"
        ).read_text(encoding="utf-8")
        for surface in (readme, agents_text, portable_entry):
            self.assertIn("Do not presume", surface)
            self.assertIn("without narrowing the field", surface)

        competence_text = (self.root / "kernel/COMPETENCE.md").read_text(encoding="utf-8")
        self.assertIn("reusable capacity to understand and do", competence_text)
        user_guide = (self.root / "docs/USER_GUIDE.md").read_text(encoding="utf-8")
        self.assertIn("A competence is learned capacity", user_guide)

        adoption_text = (self.root / "docs/ADOPTION_GUIDE.md").read_text(encoding="utf-8")
        self.assertIn(
            "does not require a host-specific adapter",
            adoption_text,
        )
        adoption_links = links(adoption_text)
        self.assertIn("SETUP.md", adoption_links)

        legacy_chat_setup = (self.root / "docs/CHAT_SETUP.md").read_text(encoding="utf-8")
        self.assertIn("[Portable setup](SETUP.md)", legacy_chat_setup)
        legacy_conversational = (
            self.root / "adapters/conversational/README.md"
        ).read_text(encoding="utf-8")
        self.assertIn("../portable/README.md", legacy_conversational)

    def test_public_kernel_does_not_reintroduce_nonportable_or_future_ceiling_frames(self) -> None:
        public_owners = {
            "adapters/portable/INSTRUCTIONS.template.md": (
                "Follow KA",
                "Meta_Skill",
            ),
            "kernel/COMPETENCE.md": (
                "Meta_Skill",
            ),
            "kernel/FDLA.md": (
                "Stiamo seguendo i principi di KA",
            ),
            "docs/LINEAGE.md": (
                "Deliberately not inherited",
                "support for providers without an implemented adapter",
            ),
            "docs/EXTERNAL_REVIEW_0_6_0.md": (
                "autonomous self-evolution",
                "subjective awareness",
            ),
            "kernel/KERNEL.md": (
                "does not assume shell access",
                "autonomous continuation",
            ),
            "adapters/chatgpt/README.md": (
                "does not simulate an agent runtime",
                "autonomous continuation",
            ),
        }
        for relative, stale_markers in public_owners.items():
            with self.subTest(relative=relative):
                text_value = (self.root / relative).read_text(encoding="utf-8")
                for marker in stale_markers:
                    self.assertNotIn(marker, text_value)

        lineage = (self.root / "docs/LINEAGE.md").read_text(encoding="utf-8")
        self.assertIn("The capability field remains open.", lineage)

        evolution_guide = (self.root / "docs/EVOLUTION_GUIDE.md").read_text(encoding="utf-8")
        self.assertIn(
            "Those relations are now owned\nby the public kernel sources in this repository.",
            evolution_guide,
        )
        portable_readme = (
            self.root / "adapters/portable/README.md"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "constitutive operating owners named by the entry live in the selected\nkernel source",
            portable_readme,
        )

        review = (self.root / "docs/EXTERNAL_REVIEW_0_6_0.md").read_text(encoding="utf-8")
        self.assertIn(
            "it neither establishes nor rules\nout capabilities outside that surface",
            review,
        )

        core = (self.root / "kernel/KERNEL.md").read_text(encoding="utf-8")
        self.assertIn(
            "one host's current topology does not\nbecome a permanent requirement or ceiling",
            core,
        )

    def test_host_confirmation_docs_publish_receipt_before_remote_reentry(self) -> None:
        cases = {
            "INSTALL.md": (
                "confirmation_bridge_sha256",
                "## 5. Verify reachability",
            ),
            "adapters/chatgpt/README.md": (
                "confirmation_bridge_sha256",
                "## Reachability and evidence",
            ),
        }
        ordered = (
            "--confirm-host-installation",
            "git add state/INSTANCE.json",
            'git commit -m "Record ChatGPT host installation receipt"',
            "git rev-parse HEAD",
            "git push",
            "git fetch --no-tags origin",
            "git rev-parse FETCH_HEAD",
            "git show FETCH_HEAD:state/INSTANCE.json",
        )
        for relative, (start_marker, reentry_marker) in cases.items():
            with self.subTest(relative=relative):
                text_value = (self.root / relative).read_text(encoding="utf-8")
                start = text_value.find(start_marker)
                self.assertGreaterEqual(start, 0, relative)
                positions = []
                cursor = start
                for marker in ordered:
                    position = text_value.find(marker, cursor)
                    self.assertGreaterEqual(position, 0, (relative, marker))
                    positions.append(position)
                    cursor = position + len(marker)
                reentry = text_value.find(reentry_marker, cursor)
                self.assertGreaterEqual(reentry, 0, (relative, reentry_marker))
                self.assertEqual(positions, sorted(positions), relative)

        agents = (self.root / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("[INSTALL.md](INSTALL.md)", agents)
        self.assertIn(
            "[ChatGPT adapter guide](adapters/chatgpt/README.md)",
            agents,
        )
        self.assertNotIn("--confirm-host-installation", agents)
        self.assertNotIn("confirmation_bridge_sha256", agents)
        install = (self.root / "INSTALL.md").read_text(encoding="utf-8")
        self.assertIn(
            '<a name="receipt-publication-and-fresh-readback"></a>',
            install,
        )

    def test_github_repository_identity_case_differences_are_not_drift(self) -> None:
        configured = self.configure()
        self.assertEqual(configured.returncode, 0, configured.stderr)
        confirmed = self.confirm_host()
        self.assertEqual(confirmed.returncode, 0, confirmed.stderr)

        instance_path = self.root / "state/INSTANCE.json"
        instance = json.loads(instance_path.read_text(encoding="utf-8"))
        instance["instance_repository"] = "Example-User/Example-Kernel"
        instance["configured_bridge_repository"] = "EXAMPLE-USER/example-kernel"
        instance["host_installation"]["installed_bridge_repository"] = "example-user/EXAMPLE-KERNEL"
        instance_path.write_text(json.dumps(instance, indent=2) + "\n", encoding="utf-8")

        result, payload = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(payload["valid"])
        warnings = "\n".join(payload["warnings"])
        self.assertNotIn("different user-owned repository", warnings)
        self.assertNotIn("repository differs", warnings)


if __name__ == "__main__":
    unittest.main()
