"""Regression tests for the dependency-free collection validator."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_skills.py"


def write_fixture(
    root: Path,
    *,
    indexed: bool = True,
    malformed: bool = False,
    malformed_metadata: bool = False,
    null_frontmatter: bool = False,
) -> None:
    skill_dir = root / "skills" / "sample-skill" / "agents"
    skill_dir.mkdir(parents=True)
    skill_file = root / "skills" / "sample-skill" / "SKILL.md"
    fenced_body = "```text\nexample\n```\n" if not malformed else "```text\nexample\n"
    description = "description: null # comment\n" if null_frontmatter else "description: Review a sample skill for structural correctness.\n"
    skill_file.write_text(
        "---\n"
        + "name: sample-skill\n"
        + description
        + "---\n\n"
        + "# Sample\n\n"
        + "## Exact output format\n\n"
        + fenced_body,
        encoding="utf-8",
    )
    metadata = (
        "interface:\n"
        '  display_name: "Sample Skill"\n'
        '  short_description: "Validate a sample skill structure"\n'
        '  default_prompt: "Use $sample-skill to validate this sample."\n'
    )
    if malformed_metadata:
        metadata = metadata.replace('  display_name:', '    display_name:')
    (skill_dir / "openai.yaml").write_text(
        metadata,
        encoding="utf-8",
    )
    link = "- [sample](skills/sample-skill/SKILL.md)\n" if indexed else ""
    (root / "README.md").write_text(f"# Skills\n\n{link}", encoding="utf-8")


class ValidatorTests(unittest.TestCase):
    def run_validator(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VALIDATOR), "--root", str(root)],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_valid_fixture_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root)
            result = self.run_validator(root)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_unindexed_skill_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, indexed=False)
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("not indexed", result.stderr)

    def test_unbalanced_markdown_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, malformed=True)
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("unbalanced", result.stderr)

    def test_misindented_metadata_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, malformed_metadata=True)
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("misindented", result.stderr)

    def test_null_frontmatter_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, null_frontmatter=True)
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("real value", result.stderr)

    def test_routing_index_keeps_primary_skills_visible(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for phrase, skill in (
            ("Review a PR", "code-review"),
            ("Assess prompts", "agent-usage-review"),
            ("Diagnose or improve", "service-improvement"),
        ):
            self.assertIn(phrase, readme)
            self.assertIn(f"`{skill}`", readme)


if __name__ == "__main__":
    unittest.main()
