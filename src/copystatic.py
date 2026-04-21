import os
import shutil

def copy_files_recursive(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    contents = os.listdir(src)

    for item in contents:
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        print(f" * {src_path} -> {dest_path}")
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        else:
            copy_files_recursive(src_path, dest_path)