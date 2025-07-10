# 3. Cree una estructura de objetos que asemeje un Binary Tree.
#     1. Debe incluir un método para hacer `print` de toda la estructura.
#     2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert_left(self, parent_node, value):
        if parent_node.left is None:
            parent_node.left = TreeNode(value)
            print(f"Inserted {value} to the left of {parent_node.value}")
        else:
            print(f"Left child of {parent_node.value} already exists.")

    def insert_right(self, parent_node, value):
        if parent_node.right is None:
            parent_node.right = TreeNode(value)
            print(f"Inserted {value} to the right of {parent_node.value}")
        else:
            print(f"Right child of {parent_node.value} already exists.")

    def print_tree(self):
        def _print(node, level=0):
            if node is not None:
                print("  " * level + str(node.value))
                _print(node.left, level + 1)
                _print(node.right, level + 1)
        print("Binary Tree Structure:")
        _print(self.root)


tree = BinaryTree(10)
tree.insert_left(tree.root, 5)
tree.insert_right(tree.root, 15)
tree.insert_left(tree.root.left, 3)
tree.insert_right(tree.root.left, 7)
tree.print_tree()