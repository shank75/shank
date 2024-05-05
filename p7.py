class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def construct_expression_tree(expression):
    ops = set(['+', '-', '*', '/'])
    stack = []
    for char in reversed(expression):
        if char in ops:
            node = TreeNode(char)
            node.left, node.right = stack.pop(), stack.pop()
            stack.append(node)
        else:
            stack.append(TreeNode(char))
    return stack.pop()

def postorder_traversal(root):
    if not root: return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return result[::-1]

def print_tree(root, level=0):
    if root:
        print_tree(root.right, level + 1)
        print(' ' * 4 * level + '->', root.val)
        print_tree(root.left, level + 1)

def delete_tree(root):
    if root:
        delete_tree(root.left)
        delete_tree(root.right)
        del root

prefix = input("Enter the prefix expression: ")
tree = construct_expression_tree(prefix)
print("\nExpression Tree:")
print_tree(tree)
print("\nPostorder Traversal (non-recursive):", postorder_traversal(tree))
delete_tree(tree)
print("Tree deleted successfully.")
