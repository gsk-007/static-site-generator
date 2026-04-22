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
    full_html = full_html.replace('{{ Content }}', html)

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write output
    with open(dest_path, "w") as file:
        file.write(full_html)
    f.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dirs = os.listdir(dir_path_content)

    for item in dirs:
        src_path = os.path.join(dir_path_content, item)
        if os.path.isfile(src_path):
            dest_path = os.path.join(dest_dir_path, item.split(".")[0]+".html")
            print(f" * {src_path} -> {dest_path}")
            generate_page(src_path, template_path, dest_path)
        else:
            dest_path = os.path.join(dest_dir_path, item)
            print(f" * {src_path} -> {dest_path}")
            generate_pages_recursive(src_path, template_path, dest_path)

