class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        if self.head:
            new_node = Node(value=value)
            new_node.prev = self.head
            self.head = new_node
        else:
            self.head = Node(value=value)
        self.size += 1
        print("Value Pushed.")

    def pop(self):
        if self.head:
            prev_node = self.head.prev
            self.head = prev_node
            self.size -= 1
            print("Value Popped")
        else:
            print("Stack Is Empty.")

    def top(self):
        if self.head:
            print(self.head.value)
        else:
            print("Stack Is Empty.")

    def get_size(self):
        print(self.size)

    def is_empty(self):
        print(False if self.head else True)

    def display(self):
        iterator = self.head
        while iterator:
            print(iterator.value)
            iterator = iterator.prev

    def get_max(self):
        """To be implemented"""
