"""Examine skill output sections and repository links."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

from scripts.validate_skills import markdown_lines_outside_fences


ROOT = Path(__file__).resolve().parents[1]


class SkillContractTests(unittest.TestCase):
    def test_all_skills_have_a_nonempty_output_section(self) -> None:
        for path in (ROOT / "skills").glob("*/SKILL.md"):
            with self.subTest(skill=path.parent.name):
                lines, unclosed = markdown_lines_outside_fences(path.read_text())
                self.assertFalse(unclosed)
                self.assertEqual(lines.count("## Exact output format"), 1)
                start = lines.index("## Exact output format") + 1
                section = []
                for line in lines[start:]:
                    if line.startswith("## "):
                        break
                    section.append(line)
                self.assertTrue("\n".join(section).strip(), "empty output instructions")

    def test_local_markdown_links_and_anchors_exist(self) -> None:
        for path in ROOT.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if "://" in target:
                    continue
                location, _, anchor = target.partition("#")
                destination = (path.parent / location).resolve() if location else path
                with self.subTest(source=path.relative_to(ROOT), target=target):
                    self.assertTrue(destination.is_file())
                    if anchor and destination.is_file():
                        lines, _ = markdown_lines_outside_fences(destination.read_text())
                        headings = [line.lstrip("# ") for line in lines if line.startswith("#")]
                        anchors = [re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-") for heading in headings]
                        self.assertIn(anchor, anchors)

    def test_coordinator_stage_names_exist(self) -> None:
        coordinator = (ROOT / "skills/execute-ticket/SKILL.md").read_text()
        names = re.findall(r"^\| [^|]+ \| `([a-z0-9-]+)` \|$", coordinator, re.MULTILINE)
        self.assertEqual(len(names), 4)
        for name in names:
            self.assertTrue((ROOT / "skills" / name / "SKILL.md").is_file(), name)


if __name__ == "__main__":
    unittest.main()
