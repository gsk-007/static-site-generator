class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props =props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for item,value in self.props.items():
            props_html += f' {item}="{value}"'

        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("parent nodes must have tag")

        if self.children is None:
            return ValueError("parent node must have children")

        child_nodes = ""
        for child in self.children:
            child_nodes += child.to_html()
        props = self.props_to_html()
        return f'<{self.tag}{props}>{child_nodes}</{self.tag}>'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf nodes must have value")

        if self.tag is None:
            return self.value

        props = self.props_to_html()
        return f'<{self.tag}{props}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"