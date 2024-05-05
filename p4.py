class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def find_longest_path(self):
        return self._find_longest_path_recursive(self.root)
    
    def _find_longest_path_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self._find_longest_path_recursive(node.left), self._find_longest_path_recursive(node.right))
    
    def find_minimum(self):
        return self._find_minimum_recursive(self.root)
    
    def _find_minimum_recursive(self, node):
        if node.left is None:
            return node.value
        return self._find_minimum_recursive(node.left)
    
    def swap_left_right(self):
        self._swap_left_right_recursive(self.root)
    
    def _swap_left_right_recursive(self, node):
        if node is not None:
            node.left, node.right = node.right, node.left
            self._swap_left_right_recursive(node.left)
            self._swap_left_right_recursive(node.right)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def print_tree(self):
        self._print_tree_recursive(self.root, 0)
    
    def _print_tree_recursive(self, node, depth):
        if node is not None:
            self._print_tree_recursive(node.right, depth + 1)
            print("  " * depth + str(node.value))
            self._print_tree_recursive(node.left, depth + 1)

def construct_tree(values):
    tree = BinarySearchTree()
    for value in values:
        tree.insert(value)
    return tree

# Functions to perform operations
def insert_node(tree):
    new_node_value = int(input("Enter value of new node to insert: "))
    tree.insert(new_node_value)

def find_longest_path(tree):
    print("Number of nodes in longest path from root:", tree.find_longest_path())

def find_minimum(tree):
    print("Minimum data value found in the tree:", tree.find_minimum())

def swap_left_right(tree):
    tree.swap_left_right()
    print("Tree updated with roles of left and right pointers swapped.")

def search_value(tree):
    search_value = int(input("Enter value to search: "))
    result = tree.search(search_value)
    if result:
        print(f"Value {search_value} found in the tree.")
    else:
        print(f"Value {search_value} not found in the tree.")

def show_tree(tree):
    print("Binary Search Tree:")
    tree.print_tree()

# Mapping operation names to their corresponding functions
operations = {
    "insert": insert_node,
    "find_longest_path": find_longest_path,
    "find_minimum": find_minimum,
    "swap_left_right": swap_left_right,
    "search_value": search_value,
    "show_tree": show_tree
}

def main():
    while True:
        # Input from user
        values = list(map(int, input("Enter values to insert into the binary search tree (separated by space): ").split()))

        # Construct the tree
        tree = construct_tree(values)

        # Perform operations
        print("Binary Search Tree Operations:")
        print("1. Insert new node")
        print("2. Find number of nodes in longest path from root")
        print("3. Minimum data value found in the tree")
        print("4. Change the tree so that the roles of the left and right pointers are swapped at every node")
        print("5. Search a value")
        print("6. Show the tree")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 7:
            print("Exiting...")
            break

        # Perform the selected operation
        operation = list(operations.keys())[choice - 1]
        operations[operation](tree)

# Main execution
if __name__ == "__main__":
    main()