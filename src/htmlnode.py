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



class LeafNode(HTMLNode):
    def __init__(self, value, tag, props=None):
        super().__init__(value, tag, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf nodes must have value")

        if self.tag is None:
            return self.value

        props = self.props_to_html()
        return f'<{self.tag}{props}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"