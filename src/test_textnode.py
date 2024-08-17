import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)
    
    def test_eq2(self):
        node1 = TextNode("These nodes are not equal", "italics")
        node2 = TextNode("These nodes aren't equal", "bold", "http://www.google.com")
        self.assertNotEqual(node1, node2)
    
    def test_eq3(self):
        node1 = TextNode("Unit testing for boot.dev", "bold", "http://www.boot.dev")
        node2 = TextNode("Unit testing for boot.dev", "bold", "http://www.boot.dev")
        self.assertEqual(node1, node2)
    
    def test_eq4(self):
        node1 = TextNode("Testing url = none", "italics", url = None)
        node2 = TextNode("Testing url = none", "italics", url = None)
        self.assertEqual(node1, node2)


if __name__ == "__main__":
    unittest.main() 