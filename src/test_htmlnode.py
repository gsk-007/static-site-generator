import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_values(self):
          node = HTMLNode(
              "div",
              "I wish I could read",
          )
          self.assertEqual(
              node.tag,
              "div",
          )
          self.assertEqual(
              node.value,
              "I wish I could read",
          )
          self.assertEqual(
              node.children,
              None,
          )
          self.assertEqual(
              node.props,
              None,
          )

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

    def test_repr(self):
            node = HTMLNode(
                "p",
                "What a strange world",
                None,
                {"class": "primary"},
            )
            self.assertEqual(
                node.__repr__(),
                "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
            )



if __name__ == "__main__":
    unittest.main()
