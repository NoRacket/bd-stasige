import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode(
            "This is a text node",
            TextType.BOLD,
            "https://github.com"
        )
        node2 = TextNode(
            "This is a text node",
            TextType.BOLD,
            "https://github.com"
        )
        self.assertEqual(node, node2)

    def test_neq_text(self):
        node1 = TextNode("This is the first node", TextType.PLAIN)
        node2 = TextNode("This is the second node", TextType.PLAIN)
        self.assertNotEqual(node1, node2)

    def test_neq_type(self):
        node1 = TextNode("This is a node", TextType.ITALIC)
        node2 = TextNode("This is a node", TextType.CODE)
        self.assertNotEqual(node1, node2)

    def test_neq_none_url(self):
        node1 = TextNode("This is a node", TextType.LINK)
        node2 = TextNode("This is a node", TextType.LINK, "https://github.com")
        self.assertNotEqual(node1, node2)

    def test_neq_url(self):
        node1 = TextNode(
            "This is a node",
            TextType.LINK,
            "https://youtube.com"
        )
        node2 = TextNode(
            "This is a node",
            TextType.LINK,
            "https://github.com"
        )
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
