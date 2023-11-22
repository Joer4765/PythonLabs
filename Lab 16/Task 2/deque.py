class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Display elements of the list
    def __str__(self):
        s = ''
        current = self.head
        while current:
            s += current.data + " <-> "
            current = current.next
        return s

    # Get the number of elements in the list
    def __len__(self):
        return self.size

    # Check if the list is empty
    def is_empty(self):
        return self.head is None

    # Insert elements into the list
    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def push_back (self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop_front(self):

        if self.is_empty():
            return

        if self.tail == self.head:
            self.tail = self.head = None
            return

        node = self.head
        next_node = node.next
        next_node.prev = None
        self.head = next_node
        return node.data

    def pop_back(self):

        if self.is_empty():
            return

        if self.tail == self.head:
            self.tail = self.head = None
            return

        node = self.tail
        prev_node = node.prev
        prev_node.next = None
        self.tail = prev_node
        return node.data

    def front(self):
        return self.head.data

    def back(self):
        return self.tail.data

    def clear(self):
        self.head = self.tail = None
        self.size = 0


if __name__ == '__main__':
    deque = Deque()
    print(deque.pop_back())
    print(deque.pop_front())

