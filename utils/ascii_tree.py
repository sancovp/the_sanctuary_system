import os

def generate_ascii_tree(directory, prefix=""):
    """
    Recursively generates an ASCII tree for a directory.

    Args:
        directory (str): The root directory path.
        prefix (str): The prefix for the current level in the tree.
    """
    contents = os.listdir(directory)
    pointers = ["├── "] * (len(contents) - 1) + ["└── "]

    for pointer, item in zip(pointers, contents):
        path = os.path.join(directory, item)
        print(f"{prefix}{pointer}{item}")

        if os.path.isdir(path):
            extension = "│   " if pointer == "├── " else "    "
            generate_ascii_tree(path, prefix=prefix + extension)

if __name__ == "__main__":
    print("Current Directory ASCII Tree:\n")
    generate_ascii_tree(os.getcwd())
