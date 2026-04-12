import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        test_output = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode(None, None, None, test_props)
        self.assertEqual(node.props_to_html(), test_output)

    def test_empty_props_to_html(self):
        test_props = {}
        test_output = ''
        node = HTMLNode(None, None, None, test_props)
        self.assertEqual(node.props_to_html(), test_output)


    def test_none_props_to_html(self):
        test_props = None
        test_output = ''
        node = HTMLNode(None, None, None, test_props)
        self.assertEqual(node.props_to_html(), test_output)



if __name__ == "__main__":
    unittest.main()
