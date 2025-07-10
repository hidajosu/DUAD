# 1. Cree una estructura de objetos que asemeje un Stack.
#     1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed: {value}")

    def pop(self):
        if self.top is None:
            print("Stack is empty. Nothing to pop.")
            return None
        value = self.top.value
        self.top = self.top.next
        print(f"Popped: {value}")
        return value

    def print_stack(self):
        current = self.top
        print("Stack contents:")
        while current is not None:
            print(current.value)
            current = current.next

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.print_stack()
stack.pop()
stack.print_stack()