import unittest

from htmlnode import HTMLNode
class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(props={"href": "https://boot.dev", "target": "_blank"})
        result = node.props_to_html()
        expected_output = ' href="https://boot.dev" target="_blank"'
        self.assertEqual(result, expected_output)

    def test_props2(self):
        node = HTMLNode()
        result = node.props_to_html()
        expected_output = ""
        self.assertEqual(result, expected_output)
    
    def test___repr__(self):
        node = HTMLNode("<a>", "Visit boot.dev", None, {"href": "https://boot.dev", "target":"_blank"})
        result = node.__repr__()
        expected_output = "HTMLNode(tag = '<a>', value = 'Visit boot.dev', props = '{'href': 'https://boot.dev', 'target': '_blank'}')"
        self.assertEqual(result, expected_output)
    
    def test__repr__(self):
        node = HTMLNode()
        result = node.__repr__()
        expected_output = "HTMLNode()"
        self.assertEqual(result, expected_output)