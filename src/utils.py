from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    res =  []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            res.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid markdown: delimiter not closed")
        for i, part in enumerate(parts):
            if part:
                res.append(TextNode(part, TextType.PLAIN_TEXT if i % 2 == 0 else text_type))
    return res

