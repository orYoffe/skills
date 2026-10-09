"""Find long sentences and contractions. This is not a full STE checker."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
CONTRACTION = re.compile(
    r"\b(?:[a-z]+n['’]t|(?:i|you|he|she|it|we|they|that|there|what|who|how|where|when)['’](?:m|re|s|ve|ll|d))\b",
    re.IGNORECASE,
)
WORDS = re.compile(r"[\w]+(?:[-'’][\w]+)*")


def prose_blocks(text: str) -> list[tuple[int, str]]:
    """Return prose blocks with source line numbers. Keep fence contents outside the check."""
    blocks: list[tuple[int, str]] = []
    paragraph: list[str] = []
    start = 1
    fence: str | None = None
    frontmatter = text.startswith("---\n")

    def flush() -> None:
        if paragraph:
            blocks.append((start, " ".join(paragraph)))
            paragraph.clear()

    for number, line in enumerate(text.splitlines(), 1):
        if frontmatter:
            if number > 1 and line == "---":
                frontmatter = False
            elif line.startswith("description:"):
                blocks.append((number, line.split(":", 1)[1].strip()))
            continue
        marker = FENCE.match(line)
        if marker:
            flush()
            value = marker.group(1)
            if fence is None:
                fence = value
            elif value[0] == fence[0] and len(value) >= len(fence):
                fence = None
            continue
        if fence is not None:
            continue
        if not line.strip() or re.match(r"^\s*(?:#|<!--)", line):
            flush()
            continue
        if line.strip().startswith("|"):
            flush()
            for cell in line.strip().strip("|").split("|"):
                if cell.strip() and not re.fullmatch(r"[\s:-]+", cell):
                    blocks.append((number, cell.strip()))
            continue
        item = re.match(r"^\s*(?:[-*+] |\d+[.)] )(.+)", line)
        if item:
            flush()
            start = number
            paragraph.append(item.group(1))
        else:
            if not paragraph:
                start = number
            paragraph.append(line.strip())
    flush()
    return blocks


def text_errors(text: str) -> list[tuple[int, str]]:
    """Examine Markdown prose. Count inline code spans as one word."""
    errors: list[tuple[int, str]] = []
    for line, block in prose_blocks(text):
        block = re.sub(r"`+[^`]+`+", "CODE", block)
        block = re.sub(r"\[([^]]+)\]\([^\s)]+\)", r"\1", block)
        block = re.sub(r"https?://\S+", "URL", block)
        for sentence in re.split(r"[.!?](?:[\"'’]?\s+|$)", block):
            count = len(WORDS.findall(sentence))
            if count > 20:
                errors.append((line, f"sentence has {count} words; maximum is 20"))
            if CONTRACTION.search(sentence):
                errors.append((line, "replace the contraction with complete words"))
    return errors


def file_errors(path: Path) -> list[tuple[int, str]]:
    text = path.read_text(encoding="utf-8")
    if path.suffix != ".yaml":
        return text_errors(text)
    errors: list[tuple[int, str]] = []
    for line, value in enumerate(text.splitlines(), 1):
        match = re.fullmatch(r'\s+(?:display_name|short_description|default_prompt): "(.*)"', value)
        if match:
            errors.extend((line, message) for _, message in text_errors(match.group(1)))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    root = parser.parse_args().root.resolve()
    paths = sorted(set(root.rglob("*.md")) | set((root / "skills").rglob("agents/openai.yaml")))
    errors = [(path, line, message) for path in paths for line, message in file_errors(path)]
    for path, line, message in errors:
        print(f"{path.relative_to(root)}:{line}: {message}")
    if errors:
        return 1
    print(f"Text checks passed for {len(paths)} files. Full STE conformance remains outside this check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
