class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        # String representing HTML tag name
        self.tag = tag
        # Represents text inside tag
        self.value = value
        # Represents children of this node
        self.children = children
        # Dictionary of key-value pairs representing the attributes of the HTML tag
        self.props = props
    
    def to_html(self):
        # Will be overwritten by subclass
        raise NotImplementedError
    
    def props_to_html(self):
        # If there are no props, return an empty string
        if not self.props:
            return ""

        # Convert the dictionary of props to a string of HTML attribute-value pairs
        return " " + " ".join([
            f'{k}="{v}"'  # Format each key-value pair as a HTML attribute-value pair
            for k, v in self.props.items()  # Iterate over each key-value pair in props
        ])

    def __repr__(self):
        parts = []
        if self.tag is not None:
            parts.append(f"tag = '{self.tag}'")
        if self.value is not None:
            parts.append(f"value = '{self.value}'")
        if self.children is not None:
            parts.append(f"children = '{len(self.children)}'")
        if self.props is not None:
            parts.append(f"props = '{str(self.props)}'")
        return f"HTMLNode({', '.join(parts)})"
    
    from htmlnode import HTMLNode
from typing import final

class LeafNode(HTMLNode):
    # Handles edge cases where there doesn't need to be a value
    self_closing_tags = {'img', 'br', 'hr', 'input', 'meta', 'link'}
    # Create LeafNode constructor which represents a single HTML tag with no children
    def __init__(self, value, tag=None, props=None):
        super().__init__(value = value, tag = tag, props=props)

    def to_html(self):
        if not self.value and self.tag not in self.self_closing_tags:
            raise ValueError("All non-self-closing leaf nodes must have a value")
        
        # If there's no tag, return raw text
        if not self.tag:
            return self.value
            
        prop_str = ""
        if self.props:
            for key,value in self.props.items():
                prop_str += f' {key}="{value}"'
        
        if self.tag in self.self_closing_tags:
            return f"<{self.tag}{prop_str}>"
        else:
            return f"<{self.tag}{prop_str}>{self.value}</{self.tag}>"
    
    class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props = None):
        # Creates parent node constructor which handles the HTML nodes inside of one another
        super().__init__(tag=tag, value=None, children = children, props = props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag")
            
        if not self.children:
            raise ValueError("All parent nodes must have children")
            
        child_html = ""
        for child in self.children:
            child_html += child.to_html()

        return f"<{self.tag}>{child_html}</{self.tag}>"

