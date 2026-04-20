

import unittest

from block_utils import block_to_block_type, markdown_to_blocks, markdown_to_html_node
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

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_blockquote(self):
        md = """
> This is a quote
> with **bold** text
> and _italic_ too
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with <b>bold</b> text and <i>italic</i> too</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- First item with **bold**
- Second item with _italic_
- Third item with `code`
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>First item with <b>bold</b></li><li>Second item with <i>italic</i></li><li>Third item with <code>code</code></li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. First item
2. Second item with **bold**
3. Third item with _italic_
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item with <b>bold</b></li><li>Third item with <i>italic</i></li></ol></div>",
        )

    def test_mixed_blocks(self):
        md = """
# Heading

This is a paragraph with **bold** text.

- list item one
- list item two

> a wise quote
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading</h1><p>This is a paragraph with <b>bold</b> text.</p><ul><li>list item one</li><li>list item two</li></ul><blockquote>a wise quote</blockquote></div>",
        )

if __name__ == "__main__":
    unittest.main()
