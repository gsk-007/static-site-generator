import os
from block_utils import markdown_to_html_node

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        line.strip()
        if line.startswith('# '):
            return line[2:].strip()

    raise Exception('No h1 header found')

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_content = ''
    with open(from_path, 'r') as file:
        markdown_content = file.read()

    f = open(template_path, "r+")
    template = f.read()
    title = extract_title(markdown_content)
    html = markdown_to_html_node(markdown_content).to_html()

    full_html = template.replace('{{ Title }}', title)
    full_html = template.replace('{{ Content }}', html)

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write output
    with open(dest_path, "w") as f:
        f.write(full_html)
    f.close()

