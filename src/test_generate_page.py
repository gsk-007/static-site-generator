import unittest

from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_multiple_lines(self):
        md = "Some text\n# Title Here\nMore text"
        self.assertEqual(extract_title(md), "Title Here")

    def test_no_h1(self):
        with self.assertRaises(Exception):
            extract_title("## Not H1\nNo title")

if __name__ == "__main__":
    unittest.main()