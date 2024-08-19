from htmlnode import HTMLNode
from typing import final

@final
class LeafNode(HTMLNode):
    # Handles edge cases where there doesn't need to be a value
    self_closing_tags = {'img', 'br', 'hr', 'input', 'meta', 'link'}
    # Create LeafNode constructor which represents a single HTML tag with no children
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if not self.value and self.tag not in self.self_closing_tags:
            raise ValueError("All non-self-closing leaf nodes must have a value")
    
        # If theres no tag, return raw text
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
