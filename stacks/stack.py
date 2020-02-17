class Node:

    def __init__(self, item):
        self.item = item
        self.prev = None


class SLLStack:
    """Singly Link List based Stack implementation"""

    def __init__(self):
        self.head = None

    def push(self, item):
        if self.head:
            new_node = Node(item=item)
            new_node.prev = self.head
            self.head = new_node
        else:
            self.head = Node(item=item)

    def pop(self):
        if self.head:
            prev_node = self.head
            self.head = self.head.prev
            prev_node.next = None
            return prev_node.item
        print("Stack Underflow.")

    def top(self):
        if self.head:
            print(self.head.item)
        else:
            print("Stack Underflow.")

    def display_stack(self):
        if self.head:
            iter_node = self.head
            while iter_node:
                print(iter_node.item)
                iter_node = iter_node.prev
        else:
            print("Stack Underflow.")
