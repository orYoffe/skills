"""Examine skill structure without third-party packages.

This validator supports only the metadata format used in this repository.
It rejects unknown fields and incorrect indentation. It is not a general YAML parser.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_FIELD = re.compile(r"^(name|description):\s*(\S.*)$")
UI_FIELD = re.compile(r'^ {2}(display_name|short_description|default_prompt):\s+"([^"]*)"\s*$')
README_LINK = re.compile(r"\]\(((?:\.\./)?skills/([a-z0-9-]+)/SKILL\.md)\)")
NULL_VALUE = re.compile(r"^(?:null|Null|NULL|~)(?:\s+#.*)?$")
FENCE = re.compile(r"^ {0,3}(?P<marker>`{3,}|~{3,})")
EXACT_OUTPUT_HEADING = re.compile(r"^ {0,3}## Exact output format\s*$")


def fail(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path}: {message}")


def markdown_lines_outside_fences(text: str) -> tuple[list[str], bool]:
    """Return lines outside code fences and an unclosed-fence flag."""

    lines_outside_fences: list[str] = []
    open_marker: str | None = None
    open_length = 0
    for line in text.splitlines():
        fence = FENCE.match(line)
        if fence:
            marker = fence.group("marker")
            if open_marker is None:
                open_marker = marker[0]
                open_length = len(marker)
            elif marker[0] == open_marker and len(marker) >= open_length:
                open_marker = None
                open_length = 0
            continue
        if open_marker is None:
            lines_outside_fences.append(line)
    return lines_outside_fences, open_marker is not None


def validate_skill(skill_dir: Path, errors: list[str]) -> None:
    skill_file = skill_dir / "SKILL.md"
    metadata_file = skill_dir / "agents" / "openai.yaml"
    if not skill_file.is_file():
        fail(errors, skill_dir, "missing SKILL.md")
        return
    if not metadata_file.is_file():
        fail(errors, skill_dir, "missing agents/openai.yaml")
        return

    text = skill_file.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) < 5 or lines[0] != "---":
        fail(errors, skill_file, "frontmatter must start with ---")
        return
    try:
        end = lines.index("---", 1)
    except ValueError:
        fail(errors, skill_file, "frontmatter has no closing ---")
        return

    fields: dict[str, str] = {}
    seen_fields: set[str] = set()
    for line in lines[1:end]:
        if not line.strip():
            continue
        match = FRONTMATTER_FIELD.match(line)
        if not match:
            fail(errors, skill_file, f"unsupported frontmatter line: {line}")
            continue
        if match.group(1) in seen_fields:
            fail(errors, skill_file, f"duplicate frontmatter field: {match.group(1)}")
        seen_fields.add(match.group(1))
        value = match.group(2).strip()
        if not value or NULL_VALUE.fullmatch(value) or value.startswith("#"):
            fail(errors, skill_file, f"frontmatter {match.group(1)} must have a real value")
        fields[match.group(1)] = value
    for required in ("name", "description"):
        if not fields.get(required):
            fail(errors, skill_file, f"frontmatter missing non-empty {required}")
    if fields.get("name") != skill_dir.name:
        fail(errors, skill_file, "frontmatter name must match directory name")
    if fields.get("name") and not NAME_RE.fullmatch(fields["name"]):
        fail(errors, skill_file, "name must be lowercase hyphen-case")
    lines_outside_fences, has_unclosed_fence = markdown_lines_outside_fences(text)
    if has_unclosed_fence:
        fail(errors, skill_file, "Markdown code fences are unbalanced")

    metadata = metadata_file.read_text(encoding="utf-8")
    if not re.search(r"^interface:\s*$", metadata, re.MULTILINE):
        fail(errors, metadata_file, "missing interface section")
    ui: dict[str, str] = {}
    seen_ui_fields: set[str] = set()
    expected_ui_fields = ("display_name", "short_description", "default_prompt")
    metadata_lines = metadata.splitlines()
    if not metadata_lines or metadata_lines[0] != "interface:":
        fail(errors, metadata_file, "interface must be the first metadata line")
    for line in metadata_lines[1:]:
        if not line.strip():
            continue
        match = UI_FIELD.match(line)
        if not match:
            fail(errors, metadata_file, f"unsupported or misindented metadata line: {line}")
            continue
        expected = expected_ui_fields[len(seen_ui_fields)] if len(seen_ui_fields) < len(expected_ui_fields) else None
        if match.group(1) != expected:
            fail(errors, metadata_file, f"interface fields must be ordered as {', '.join(expected_ui_fields)}")
        if match.group(1) in seen_ui_fields:
            fail(errors, metadata_file, f"duplicate interface field: {match.group(1)}")
        seen_ui_fields.add(match.group(1))
        ui[match.group(1)] = match.group(2)
    for required in ("display_name", "short_description", "default_prompt"):
        if not ui.get(required):
            fail(errors, metadata_file, f"missing quoted interface.{required}")
    if ui.get("short_description") and not 25 <= len(ui["short_description"]) <= 64:
        fail(errors, metadata_file, "short_description must be 25-64 characters")
    if ui.get("default_prompt") and f"${skill_dir.name}" not in ui["default_prompt"]:
        fail(errors, metadata_file, "default_prompt must mention the skill with $skill-name")
    output_headings = [
        line
        for line in lines_outside_fences
        if EXACT_OUTPUT_HEADING.fullmatch(line)
    ]
    if not output_headings:
        fail(errors, skill_file, "missing exact output format section")
    elif len(output_headings) > 1:
        fail(errors, skill_file, "duplicate exact output format sections")


def validate_readme(root: Path, skill_names: set[str], errors: list[str]) -> None:
    readme = root / "README.md"
    if not readme.is_file():
        fail(errors, readme, "missing README.md")
        return
    documents = [readme]
    readme_text = readme.read_text(encoding="utf-8")
    catalog = root / "docs" / "independent-skills.md"
    if "](docs/independent-skills.md)" in readme_text:
        if catalog.is_file():
            documents.append(catalog)
        else:
            fail(errors, readme, "independent skill catalog is missing")
    linked_names: set[str] = set()
    for document in documents:
        text = document.read_text(encoding="utf-8")
        for link, skill_name in README_LINK.findall(text):
            linked_names.add(skill_name)
            if not (document.parent / link).is_file():
                fail(errors, document, f"link target does not exist: {link}")
            if not (root / "skills" / skill_name / "SKILL.md").is_file():
                fail(errors, document, f"linked skill is missing: {skill_name}")
    for skill_name in sorted(skill_names - linked_names):
        fail(errors, readme, f"skill is not indexed in README.md or its independent catalog: {skill_name}")



def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    skills_dir = root / "skills"
    errors: list[str] = []
    skill_names: set[str] = set()
    if not skills_dir.is_dir():
        fail(errors, skills_dir, "missing skills directory")
    else:
        skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir())
        if not skill_dirs:
            fail(errors, skills_dir, "no skill directories found")
        for skill_dir in skill_dirs:
            skill_names.add(skill_dir.name)
            validate_skill(skill_dir, errors)
    validate_readme(root, skill_names, errors)
    if errors:
        print("Skill validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    count = len([path for path in skills_dir.iterdir() if path.is_dir()])
    print(f"Structure checks passed for {count} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
