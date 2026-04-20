from typing_extensions import List
from blocktype import BlockType
from htmlnode import LeafNode, ParentNode
from utils import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        block = block.strip()
        if block == "":
            continue
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].endswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    res = []
    for block in blocks:
        type = block_to_block_type(block)

        match type:
            case BlockType.HEADING:
                splits = block.split(" ",1)
                all_nodes = text_to_textnodes(splits[1])
                html_nodes = [text_node_to_html_node(node) for node in all_nodes]
                tag = f"h{len(splits[0])}"
                res.append(ParentNode(tag, html_nodes))
            case BlockType.QUOTE:
                splits = block.split("\n")
                clean_lines = []
                for line in splits:
                    clean_lines.append(line.removeprefix("> "))

                content = " ".join(clean_lines)
                all_nodes = text_to_textnodes(content)
                html_nodes = [text_node_to_html_node(node) for node in all_nodes]
                res.append(ParentNode("blockquote", html_nodes))
            case BlockType.CODE:
                content = block.removeprefix("```\n").removesuffix("```")
                text_node = TextNode(content, TextType.PLAIN_TEXT)
                html_node = text_node_to_html_node(text_node)
                code_node = ParentNode("code", [html_node])
                res.append(ParentNode("pre", [code_node]))
            case BlockType.UNORDERED_LIST:
                splits = block.split("\n")
                ul_list = []
                for line in splits:
                    clean_line = line.removeprefix("- ")
                    all_nodes = text_to_textnodes(clean_line)
                    html_nodes = [text_node_to_html_node(node) for node in all_nodes]
                    ul_list.append(ParentNode('li',html_nodes))
                res.append(ParentNode('ul', ul_list))
            case BlockType.ORDERED_LIST:
                splits = block.split("\n")
                ol_list = []
                for line in splits:
                    clean_line = line[3:]
                    all_nodes = text_to_textnodes(clean_line)
                    html_nodes = [text_node_to_html_node(node) for node in all_nodes]
                    ol_list.append(ParentNode('li',html_nodes))
                res.append(ParentNode('ol', ol_list))
            case BlockType.PARAGRAPH:
                all_nodes = text_to_textnodes(" ".join(line.strip() for line in block.split("\n")))
                html_nodes = [text_node_to_html_node(node) for node in all_nodes]
                tag = "p"
                res.append(ParentNode(tag, html_nodes))

    return ParentNode("div", res)