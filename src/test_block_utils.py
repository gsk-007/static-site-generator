

import unittest

from block_utils import block_to_block_type, markdown_to_blocks
from blocktype import BlockType


class TestBlockUtils(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_with_extra_newlines(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        md = [
            "# This is heading One",
            "## This is heading Two",
            "### This is heading Three",
            "##### This is heading Four",
        ]

        for doc in md:
            self.assertEqual(block_to_block_type(doc), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        doc = """```
        print("hello")
        ```"""

        self.assertEqual(block_to_block_type(doc), BlockType.CODE)


    def test_block_to_block_type_quote(self):
        md = [
            "> This is a quote",
            ">Another quote",
        ]

        for doc in md:
            self.assertEqual(block_to_block_type(doc), BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        md = [
            "- Item one",
            "- Item two",
        ]

        for doc in md:
            self.assertEqual(block_to_block_type(doc), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        md = [
            "1. First item",
            "1. Another item",
        ]

        for doc in md:
            self.assertEqual(block_to_block_type(doc), BlockType.ORDERED_LIST)

    def test_block_to_block_type_paragraph(self):
        md = [
            "This is a paragraph.",
            "Just some random text",
            "12345",
        ]

        for doc in md:
            self.assertEqual(block_to_block_type(doc), BlockType.PARAGRAPH)

    def test_block_to_block_type_edge_cases(self):
        md = [
            "",                  # empty string
            "   ",               # whitespace
            "#No space heading", # invalid markdown heading
            "-Item without space",
        ]

        for doc in md:
            self.assertEqual(block_to_block_type(doc), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
