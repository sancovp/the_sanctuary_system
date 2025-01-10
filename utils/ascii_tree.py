import os
import sys

def generate_ascii_tree(directory, prefix=""):
    contents = os.listdir(directory)
    pointers = ["├── "] * (len(contents) - 1) + ["└── "]

    for pointer, item in zip(pointers, contents):
        path = os.path.join(directory, item)
        print(f"{prefix}{pointer}{item}")

        if os.path.isdir(path):
            extension = "│   " if pointer == "├── " else "    "
            generate_ascii_tree(path, prefix=prefix + extension)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ascii_tree.py <directory>")
    else:
        directory = sys.argv[1]
        print(f"Directory ASCII Tree: {directory}\\n")
        generate_ascii_tree(directory)
