import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')



if __name__ == "__main__":
    unittest.main()
