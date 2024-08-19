import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    # Test case 1: Node with no tag (just text)
    def test_node_with_no_tag(self):
        test1 = LeafNode("Hello World!")
        self.assertEqual(test1.to_html(), "Hello World!")

    # Test case 2: Node with a tag but no properties
    def test_node_with_tag_no_properties(self):
        test2 = LeafNode("Hello World!", "p")
        self.assertEqual(test2.to_html(), "<p>Hello World!</p>")

    # Test case 3: Node with a tag and one property
    def test_node_with_tag_and_one_property(self):
        test3 = LeafNode("Visit boot.dev", "a", {"href": "https://www.boot.dev"})
        self.assertEqual(test3.to_html(), '<a href="https://www.boot.dev">Visit boot.dev</a>')

    # Test case 4: Node with no value, one tag, and multiple properties
    def test_node_with_no_value_tag_and_multiple_properties(self):
        test4 = LeafNode("", "img", {"src": "image.jpg", "alt": "An Image"})
        self.assertEqual(test4.to_html(), '<img src="image.jpg" alt="An Image">')

if __name__ == '__main__':
    unittest.main()