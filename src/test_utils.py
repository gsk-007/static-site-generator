import unittest

from textnode import TextNode, TextType
from utils import extract_markdown_images, extract_markdown_links, split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(new_nodes[1].text_type, TextType.CODE_TEXT)
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN_TEXT)

    def test_bold(self):
        node = TextNode("This is text with a **bolded phrase** word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD_TEXT)
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN_TEXT)

    def test_italics(self):
        node = TextNode("This is text with a _italic phrase_ word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN_TEXT)

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.example.com)"
        )
        self.assertListEqual([("link", "https://www.example.com")], matches)


if __name__ == "__main__":
    unittest.main()
