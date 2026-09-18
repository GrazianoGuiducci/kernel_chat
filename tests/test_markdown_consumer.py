"""Compare package Markdown navigation with an independent CommonMark consumer."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import unquote, urlsplit
import unittest

from markdown_it import MarkdownIt


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = MarkdownIt("commonmark")


def active_links(text: str) -> list[str]:
    links: list[str] = []

    def visit(tokens: list[object]) -> None:
        for token in tokens:
            token_type = getattr(token, "type", None)
            if token_type == "link_open":
                href = token.attrGet("href")
                if href is not None:
                    links.append(href)
            children = getattr(token, "children", None)
            if children:
                visit(children)

    visit(MARKDOWN.parse(text))
    return links


class MarkdownConsumerTests(unittest.TestCase):
    def test_package_local_links_resolve_on_consumer_surface(self) -> None:
        for path in sorted(ROOT.rglob("*.md")):
            if ".git" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            for href in active_links(text):
                parsed = urlsplit(href)
                if parsed.scheme or parsed.netloc or href.startswith("#"):
                    continue
                destination = unquote(parsed.path)
                if not destination:
                    continue
                target = (path.parent / destination).resolve()
                try:
                    target.relative_to(ROOT)
                except ValueError:
                    self.fail(f"{path.relative_to(ROOT)} link escapes package: {href}")
                self.assertTrue(
                    target.exists(),
                    f"{path.relative_to(ROOT)} has broken active local link: {href}",
                )

    def test_r1_commonmark_counterexamples_have_expected_active_links(self) -> None:
        cases = {
            "comment-markers-inside-code-spans": (
                "`<!--` [Broken](missing-owner.md) `-->`\n",
                True,
            ),
            "indented-paragraph-continuation": (
                "Paragraph\n    [Broken](missing-owner.md)\n",
                True,
            ),
            "invalid-backtick-fence-info": (
                "``` foo`bar\n[Broken](missing-owner.md)\n```\n",
                True,
            ),
            "blockquote-fenced-code": (
                "> ~~~\n> [Example](missing-owner.md)\n> ~~~\n",
                False,
            ),
            "escaped-backticks": (
                "\\`[Broken](missing-owner.md)\\`\n",
                True,
            ),
        }

        for name, (markdown, expected_active) in cases.items():
            with self.subTest(name=name):
                links = active_links(markdown)
                self.assertEqual(
                    "missing-owner.md" in links,
                    expected_active,
                    (name, links),
                )

    def test_constitutive_discovery_links_are_active_for_consumer(self) -> None:
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        links = set(active_links(agents))
        self.assertIn(
            "kernel/KERNEL.md#mobile-observation-without-losing-the-point",
            links,
        )
        self.assertIn(
            "kernel/EVOLUTION.md#converge-the-changed-resultant",
            links,
        )


if __name__ == "__main__":
    unittest.main()
