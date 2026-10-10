"""Regression tests for the dependency-free collection validator."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_skills import markdown_lines_outside_fences


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

    def test_output_heading_inside_code_fence_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root)
            skill_file = root / "skills" / "sample-skill" / "SKILL.md"
            text = skill_file.read_text(encoding="utf-8")
            text = text.replace("## Exact output format\n\n", "")
            text = text.replace("```text\n", "```text\n## Exact output format\n")
            skill_file.write_text(text, encoding="utf-8")
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("missing exact output format", result.stderr)

    def test_missing_output_heading_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root)
            skill_file = root / "skills" / "sample-skill" / "SKILL.md"
            text = skill_file.read_text(encoding="utf-8").replace(
                "## Exact output format\n\n", ""
            )
            skill_file.write_text(text, encoding="utf-8")
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("missing exact output format", result.stderr)

    def test_markdown_heading_parser_ignores_fenced_content(self) -> None:
        headings, unclosed = markdown_lines_outside_fences(
            "# Real\n\n```markdown\n## Fake\n```\n"
        )
        self.assertFalse(unclosed)
        self.assertIn("# Real", headings)
        self.assertNotIn("## Fake", headings)

    def test_duplicate_output_heading_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root)
            skill_file = root / "skills" / "sample-skill" / "SKILL.md"
            skill_file.write_text(
                skill_file.read_text(encoding="utf-8")
                + "\n## Exact output format\n",
                encoding="utf-8",
            )
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("duplicate exact output format", result.stderr)

    def test_invalid_name_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root)
            skill_file = root / "skills" / "sample-skill" / "SKILL.md"
            skill_file.write_text(
                skill_file.read_text(encoding="utf-8").replace(
                    "name: sample-skill", "name: Sample_skill"
                ),
                encoding="utf-8",
            )
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("lowercase hyphen-case", result.stderr)

    def test_duplicate_frontmatter_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root)
            skill_file = root / "skills" / "sample-skill" / "SKILL.md"
            skill_file.write_text(
                skill_file.read_text(encoding="utf-8").replace(
                    "description: Review a sample skill for structural correctness.\n",
                    "description: Review a sample skill for structural correctness.\n"
                    "description: Duplicate description.\n",
                ),
                encoding="utf-8",
            )
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("duplicate frontmatter field", result.stderr)

    def test_invalid_metadata_values_fail(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root)
            metadata_file = root / "skills" / "sample-skill" / "agents" / "openai.yaml"
            metadata = metadata_file.read_text(encoding="utf-8")
            metadata = metadata.replace(
                'short_description: "Validate a sample skill structure"',
                'short_description: "Too short"',
            ).replace("$sample-skill", "sample-skill")
            metadata_file.write_text(metadata, encoding="utf-8")
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("25-64 characters", result.stderr)
            self.assertIn("must mention the skill", result.stderr)

    def test_dangling_readme_link_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root)
            readme = root / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8")
                + "- [missing](skills/missing/SKILL.md)\n",
                encoding="utf-8",
            )
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("link target does not exist", result.stderr)

    def test_missing_skill_files_fail(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root)
            (root / "skills" / "sample-skill" / "SKILL.md").unlink()
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("missing SKILL.md", result.stderr)

    def test_missing_metadata_files_fail(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root)
            (root / "skills" / "sample-skill" / "agents" / "openai.yaml").unlink()
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("missing agents/openai.yaml", result.stderr)

    def test_skill_indexed_in_linked_catalog_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, indexed=False)
            (root / "docs").mkdir()
            (root / "README.md").write_text("[Independent skills](docs/independent-skills.md)\n")
            (root / "docs/independent-skills.md").write_text("[Sample](../skills/sample-skill/SKILL.md)\n")
            result = self.run_validator(root)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_unlinked_catalog_does_not_hide_unindexed_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root, indexed=False)
            (root / "docs").mkdir()
            (root / "docs/independent-skills.md").write_text("[Sample](../skills/sample-skill/SKILL.md)\n")
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("not indexed", result.stderr)

    def test_missing_linked_catalog_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_fixture(root)
            readme = root / "README.md"
            readme.write_text(readme.read_text() + "[Independent skills](docs/independent-skills.md)\n")
            result = self.run_validator(root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("catalog is missing", result.stderr)


if __name__ == "__main__":
    unittest.main()
