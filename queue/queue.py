class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        if self.head:
            new_node = Node(value=value)
            self.tail.prev = new_node
            self.tail = new_node
        else:
            new_node = Node(value=value)
            self.head = self.tail = new_node
        print("Enqueued.")

    def dequeue(self):
        if self.head:
            prev_node = self.head.prev
            self.head = prev_node
            if not prev_node:
                self.tail = None
            print("Dequeued.")
        else:
            print("Queue Is Empty")

    def display(self):
        iterator = self.head
        while iterator:
            print(iterator.value)
            iterator = iterator.prev

    def get_front(self):
        print(self.head.value if self.head else "Queue Is Empty")

    def get_rear(self):
        print(self.tail.value if self.tail else "Queue Is Empty")
