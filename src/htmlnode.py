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