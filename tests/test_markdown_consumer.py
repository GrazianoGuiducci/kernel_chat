"""Compare package Markdown navigation with an independent CommonMark consumer."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import unittest

from markdown_it import MarkdownIt


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = MarkdownIt("commonmark")


class ConsumerSurfaceParser(HTMLParser):
    """Observe rendered links and headings instead of Markdown token shortcuts."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.anchors: list[str] = []
        self.headings: list[str] = []
        self.owner_events: list[tuple[str, str]] = []
        self._heading_tag: str | None = None
        self._heading_text: list[str] = []

    def _capture_link(self, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name == "href" and value is not None:
                self.links.append(value)
                return

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag == "a":
            self._capture_link(attrs)
            for name, value in attrs:
                if name in ("name", "id") and value is not None:
                    self.anchors.append(value)
                    self.owner_events.append(("anchor", value))
        if re.fullmatch(r"h[1-6]", tag):
            self._heading_tag = tag
            self._heading_text = []

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag == "a":
            self._capture_link(attrs)
            for name, value in attrs:
                if name in ("name", "id") and value is not None:
                    self.anchors.append(value)
                    self.owner_events.append(("anchor", value))

    def handle_data(self, data: str) -> None:
        if self._heading_tag is not None:
            self._heading_text.append(data)
        elif data.strip():
            self.owner_events.append(("content", data.strip()))

    def handle_endtag(self, tag: str) -> None:
        if self._heading_tag == tag:
            heading = "".join(self._heading_text).strip()
            self.headings.append(heading)
            self.owner_events.append(("heading", heading))
            self._heading_tag = None
            self._heading_text = []


def consumer_surface(text: str) -> ConsumerSurfaceParser:
    parser = ConsumerSurfaceParser()
    parser.feed(MARKDOWN.render(text))
    parser.close()
    return parser


def active_links(text: str) -> list[str]:
    return consumer_surface(text).links


def active_anchors(text: str) -> list[str]:
    return consumer_surface(text).anchors


def active_anchor_owner_pairs(text: str) -> list[tuple[str, str]]:
    """Observe active anchor -> next rendered heading on one consumer surface."""

    events = consumer_surface(text).owner_events
    pairs: list[tuple[str, str]] = []
    for index, event in enumerate(events):
        if event[0] != "anchor":
            continue
        if index + 1 >= len(events):
            continue
        next_event = events[index + 1]
        if next_event[0] == "heading":
            pairs.append((event[1], next_event[1]))
    return pairs

def active_headings(text: str) -> list[str]:
    """Return real Markdown headings that can own the constitutive fragment."""
    tokens = MARKDOWN.parse(text)
    headings: list[str] = []
    for index, token in enumerate(tokens):
        if token.type != "heading_open":
            continue
        if index + 1 >= len(tokens) or tokens[index + 1].type != "inline":
            continue
        headings.append(tokens[index + 1].content.strip())
    return headings


def constitutive_fragment(heading: str) -> str:
    """Map deliberately simple ASCII owner headings to their stable route fragment."""
    if re.fullmatch(r"[A-Za-z0-9]+(?: [A-Za-z0-9]+)*", heading) is None:
        raise AssertionError(
            "Constitutive discovery headings must keep a simple ASCII shape "
            "or gain an explicit fragment contract."
        )
    return heading.lower().replace(" ", "-")


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
            "raw-html-anchor": (
                '<a href="missing-owner.md">Broken</a>\n',
                True,
            ),
            "raw-html-anchor-in-fence": (
                '```html\n<a href="missing-owner.md">Example</a>\n```\n',
                False,
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
        contracts = {
            "kernel/KERNEL.md#kernel-chat-mobile-observation": (
                ROOT / "kernel/KERNEL.md",
                "kernel-chat-mobile-observation",
                "Mobile observation without losing the point",
            ),
            "kernel/EVOLUTION.md#kernel-chat-converge-resultant": (
                ROOT / "kernel/EVOLUTION.md",
                "kernel-chat-converge-resultant",
                "Converge the changed resultant",
            ),
            "INSTALL.md#receipt-publication-and-fresh-readback": (
                ROOT / "INSTALL.md",
                "receipt-publication-and-fresh-readback",
                "Receipt publication and fresh remote readback",
            ),
        }

        for route, (target, anchor, heading) in contracts.items():
            with self.subTest(route=route):
                self.assertIn(route, links)
                target_text = target.read_text(encoding="utf-8")
                self.assertEqual(
                    active_anchors(target_text).count(anchor),
                    1,
                    f"{route} must resolve to one explicit consumer anchor",
                )
                self.assertIn(
                    (anchor, heading),
                    active_anchor_owner_pairs(target_text),
                    f"{route} must reach the intended rendered owner heading",
                )

        wrong_active_with_fenced_decoy = (
            '<a name="kernel-chat-mobile-observation"></a>\n\n'
            "## Wrong owner\n\n"
            "```markdown\n"
            '<a name="kernel-chat-mobile-observation"></a>\n\n'
            "## Mobile observation without losing the point\n"
            "```\n"
        )
        self.assertEqual(
            active_anchors(wrong_active_with_fenced_decoy),
            ["kernel-chat-mobile-observation"],
        )
        self.assertNotIn(
            (
                "kernel-chat-mobile-observation",
                "Mobile observation without losing the point",
            ),
            active_anchor_owner_pairs(wrong_active_with_fenced_decoy),
        )
        self.assertIn(
            ("kernel-chat-mobile-observation", "Wrong owner"),
            active_anchor_owner_pairs(wrong_active_with_fenced_decoy),
        )

        intervening_rendered_content = (
            '<a name="kernel-chat-mobile-observation"></a>\n\n'
            "Wrong owner content.\n\n"
            "## Mobile observation without losing the point\n"
        )
        self.assertEqual(
            active_anchors(intervening_rendered_content),
            ["kernel-chat-mobile-observation"],
        )
        self.assertNotIn(
            (
                "kernel-chat-mobile-observation",
                "Mobile observation without losing the point",
            ),
            active_anchor_owner_pairs(intervening_rendered_content),
        )

if __name__ == "__main__":
    unittest.main()
