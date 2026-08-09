"""Contract tests for the repository's agent-facing skill artifacts."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

from scripts.validate_skills import markdown_lines_outside_fences


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_HEADINGS = {
    "code-review": [
        "## Decision",
        "## Scope and intent",
        "## Validation",
        "## Coverage",
        "## Findings",
        "## Hypotheses and follow-ups",
        "## Strengths",
        "## Residual risk and approval gate",
    ],
    "agent-usage-review": [
        "## Executive summary",
        "## System map",
        "## Control coverage",
        "## Prioritized findings",
        "## Prioritized improvement plan",
        "## Verification plan",
        "## Open questions and assumptions",
        "## Stopping decision",
    ],
    "service-improvement": [
        "## 1. Executive summary",
        "## 2. Context and topology",
        "## 3. Workload and objectives",
        "## 4. Baseline evidence",
        "## 5. Findings",
        "## 6. Prioritized improvement plan",
        "## 7. Verification record",
        "## 8. Files, commands, and sources",
        "## 9. Decision and follow-up",
    ],
}


def output_template_headings(text: str) -> list[str]:
    section = text.split("## Exact output format", 1)[1]
    match = re.search(r"```(?:markdown)?\n(.*?)\n```", section, re.DOTALL)
    if match is None:
        return []
    return [line for line in match.group(1).splitlines() if line.startswith("## ")]


class SkillContractTests(unittest.TestCase):
    def test_each_skill_has_one_real_output_contract(self) -> None:
        for skill_name, required_headings in REQUIRED_HEADINGS.items():
            skill_file = ROOT / "skills" / skill_name / "SKILL.md"
            text = skill_file.read_text(encoding="utf-8")
            headings, unclosed = markdown_lines_outside_fences(text)
            self.assertFalse(unclosed, skill_name)
            self.assertEqual(
                headings.count("## Exact output format"),
                1,
                skill_name,
            )
            template_headings = output_template_headings(text)
            for heading in required_headings:
                self.assertIn(
                    heading,
                    template_headings,
                    f"{skill_name}: {heading}",
                )

    def test_primary_routing_rows_reference_known_skills(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        routing = readme.split("## Routing and composition", 1)[1].split(
            "Use the companion", 1
        )[0]
        rows = re.findall(
            r"^\| [^|]+ \| \[`([a-z0-9-]+)`\]\(skills/([a-z0-9-]+)/SKILL\.md\) \|",
            routing,
            re.MULTILINE,
        )
        self.assertEqual(
            {name for name, path_name in rows},
            {path_name for name, path_name in rows},
        )
        self.assertEqual(
            {name for name, _ in rows},
            set(REQUIRED_HEADINGS),
        )


if __name__ == "__main__":
    unittest.main()
