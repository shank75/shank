class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

def build_tree():
    root_name = input("Enter the name of the book: ")
    book = TreeNode(root_name)

    while True:
        chapter_name = input("Enter the name of a chapter (or type 'exit' to finish): ")
        if chapter_name.lower() == 'exit':
            break

        chapter = TreeNode(chapter_name)
        book.children.append(chapter)

        while True:
            section_name = input("Enter the name of a section (or type 'exit' to finish): ")
            if section_name.lower() == 'exit':
                break

            section = TreeNode(section_name)
            chapter.children.append(section)

            while True:
                subsection_name = input("Enter the name of a subsection (or type 'exit' to finish): ")
                if subsection_name.lower() == 'exit':
                    break

                subsection = TreeNode(subsection_name)
                section.children.append(subsection)

    return book

def print_tree(node, level=0):
    print("  " * level + node.name)
    for child in node.children:
        print_tree(child, level + 1)

book = build_tree()

# Print the tree
print("\nBook Structure:")
print_tree(book)
