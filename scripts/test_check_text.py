"""Test text diagnostics and exclusions with independent input examples."""

import tempfile
import unittest
from pathlib import Path

from scripts.check_text import file_errors, text_errors


class TextCheckTests(unittest.TestCase):
    def test_sentence_limit(self):
        self.assertEqual(text_errors(" ".join(["word"] * 20) + "."), [])
        self.assertIn("21 words", text_errors(" ".join(["word"] * 21) + ".")[0][1])

    def test_paragraph_limit(self):
        self.assertEqual(text_errors("Do the checks. " * 6), [])
        self.assertIn("six sentences", text_errors("Do the checks. " * 7)[0][1])
        self.assertEqual(text_errors("Do the checks. " * 4 + "\n\n" + "Do the checks. " * 4), [])

    def test_wrapped_paragraph_is_one_sentence(self):
        text = " ".join(["word"] * 11) + "\n" + " ".join(["word"] * 10) + "."
        self.assertEqual(text_errors(text)[0][0], 1)

    def test_separate_sentences_and_items(self):
        sentence = " ".join(["word"] * 15) + "."
        self.assertEqual(text_errors(sentence + " " + sentence), [])
        self.assertEqual(text_errors("- " + sentence + "\n- " + sentence), [])

    def test_contractions_and_possessives(self):
        for text in ("Do not assume it’s correct.", "Don't change this.", "We'll wait."):
            self.assertTrue(text_errors(text), text)
        self.assertEqual(text_errors("Keep the user's files."), [])

    def test_code_and_link_destinations_do_not_add_words(self):
        text = "Use `" + " ".join(["code"] * 30) + "` with [the guide](https://example.com/long/path)."
        self.assertEqual(text_errors(text), [])
        self.assertTrue(text_errors("[" + " ".join(["word"] * 21) + "](https://example.com)."))

    def test_fences_use_matching_markers(self):
        text = "~~~~python\nDon't count this.\n```\nStill don't count it.\n~~~~\nDon't skip this."
        self.assertEqual(len(text_errors(text)), 1)
        self.assertEqual(text_errors(text)[0][0], 6)

    def test_frontmatter_and_metadata_are_examined(self):
        self.assertTrue(text_errors("---\nname: sample\ndescription: Don't do this.\n---\n# Name\n"))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "openai.yaml"
            path.write_text('interface:\n  default_prompt: "Don’t skip the checks."\n')
            self.assertTrue(file_errors(path))

    def test_table_cells_are_separate(self):
        cell = " ".join(["word"] * 15)
        self.assertEqual(text_errors(f"| {cell} | {cell} |"), [])
        self.assertTrue(text_errors("| " + " ".join(["word"] * 21) + " | result |"))


if __name__ == "__main__":
    unittest.main()
