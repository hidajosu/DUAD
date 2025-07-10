# 2. Cree una estructura de objetos que asemeje un Double Ended Queue.
#     1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleEndedQueue:
    def __init__(self):
        self.left = None
        self.right = None

    def push_left(self, value):
        new_node = Node(value)
        if self.left is None:
            self.left = self.right = new_node
        else:
            new_node.next = self.left
            self.left.prev = new_node
            self.left = new_node
        print(f"Pushed left: {value}")

    def push_right(self, value):
        new_node = Node(value)
        if self.right is None:
            self.left = self.right = new_node
        else:
            new_node.prev = self.right
            self.right.next = new_node
            self.right = new_node
        print(f"Pushed right: {value}")

    def pop_left(self):
        if self.left is None:
            print("Queue is empty. Nothing to pop left.")
            return None
        value = self.left.value
        if self.left == self.right:
            self.left = self.right = None
        else:
            self.left = self.left.next
            self.left.prev = None
        print(f"Popped left: {value}")
        return value

    def pop_right(self):
        if self.right is None:
            print("Queue is empty. Nothing to pop right.")
            return None
        value = self.right.value
        if self.left == self.right:
            self.left = self.right = None
        else:
            self.right = self.right.prev
            self.right.next = None
        print(f"Popped right: {value}")
        return value

    def print_queue(self):
        current = self.left
        print("Queue contents (left to right):")
        while current is not None:
            print(current.value)
            current = current.next


deq = DoubleEndedQueue()
deq.push_left(10)
deq.push_right(20)
deq.push_left(5)
deq.print_queue()
deq.pop_right()
deq.print_queue()
deq.pop_left()
deq.print_queue()