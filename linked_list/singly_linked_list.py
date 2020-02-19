class Node:

    def __init__(self, item):
        self.item = item
        self.prev = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, item):
        if self.head:
            new_node = Node(item=item)
            new_node.prev = self.head
            self.head = new_node
        else:
            self.head = Node(item=item)
        return item

    def clear(self):
        self.head = None
        return "Cleared"

    def pop(self):
        if self.head:
            self.head = self.head.prev
        else:
            print("Empty LinkedList.")

    def remove(self, value):
        iter_node = self.head
        if iter_node:
            value_removed = False
            while iter_node:
                if value == iter_node.item:
                    """To Be Implemented."""
                    value_removed = True
                    break
            return value if value_removed else "Value not found."
        else:
            print("Empty LinkedList.")

    def display(self):
        iter_node = self.head
        if iter_node:
            items = []
            while iter_node:
                items.append(iter_node.item)
                iter_node = iter_node.prev
            if items:
                items.reverse()
                for item in items: print("> ", item, end=" ")
        else:
            print("Empty LinkedList.")
