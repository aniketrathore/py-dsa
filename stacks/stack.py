class Node:

    def __init__(self, item):
        self.item = item
        self.prev = None


class SLLStack:
    """Stack implementation using Singly Linked List """

    def __init__(self):
        self.head = None

    def top(self):
        if self.head:
            return self.head.item
        print("Stack Underflow.")

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
            self.head = prev_node.prev
            return prev_node.item
        else:
            print("Stack Underflow.")

    def display(self):
        iter_node = self.head
        while iter_node:
            print(iter_node.item)
            iter_node = iter_node.prev

    def is_empty(self):
        return True if self.head else False
