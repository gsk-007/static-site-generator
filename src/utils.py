import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
    images = []
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    for alt, url in matches:
        images.append((alt, url))
    return images

def extract_markdown_links(text):
    links = []
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    for alt, url in matches:
        links.append((alt, url))
    return links

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

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE_TEXT,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN_TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK_TEXT, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN_TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.PLAIN_TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC_TEXT)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE_TEXT)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes