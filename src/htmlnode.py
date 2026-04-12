class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props =props

    def to_html(self):
        raise NotImplementedError("Implement HTML Conversion")

    def props_to_html(self):
        if self.props is None:
            return ""
        res = ""
        for item,value in self.props.items():
            res += f' {item}="{value}"'

        return res

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"