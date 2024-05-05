class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.name) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

def construct_book_tree():
    book = Node(input("Enter the name of the book: "))

    num_chapters = int(input("Enter the number of chapters: "))
    for chapter_num in range(1, num_chapters + 1):
        chapter = Node(input(f"Enter the name of Chapter {chapter_num}: "))
        book.add_child(chapter)

        num_sections = int(input(f"Enter the number of sections for {chapter.name}: "))
        for section_num in range(1, num_sections + 1):
            section = Node(input(f"Enter the name of Section {section_num} in {chapter.name}: "))
            chapter.add_child(section)

            num_subsections = int(input(f"Enter the number of subsections for {section.name}: "))
            for subsection_num in range(1, num_subsections + 1):
                subsection = Node(input(f"Enter the name of Subsection {subsection_num} in {section.name}: "))
                section.add_child(subsection)

    return book

if __name__ == "__main__":
    book_tree = construct_book_tree()
    print("Book Tree:")
    print(book_tree)