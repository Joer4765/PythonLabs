class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
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
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert_at_position(self, data, position):
        if position < 0:
            position = 0
        if position > self.size:
            position = self.size

        new_node = Node(data)

        if position == 0:
            self.insert_at_beginning(data)
        elif position == self.size:
            self.insert_at_end(data)
        else:
            current = self.head
            for _ in range(position):
                current = current.next
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node

        self.size += 1

    # Remove elements from the list
    def remove_all(self):
        self.head = self.tail = None
        self.size = 0

    def remove_at_index(self, index):
        if 0 <= index < self.size:
            current = self.head
            for _ in range(index):
                current = current.next
            if current.prev:
                current.prev.next = current.next
            else:
                self.head = current.next
            if current.next:
                current.next.prev = current.prev
            else:
                self.tail = current.prev
            self.size -= 1

    def remove_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.size -= 1
            current = current.next

    def remove_values(self, values):
        for value in values:
            self.remove_value(value)

    # Edit elements in the list
    def edit(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                return
            current = current.next

    # Replace all instances of a value with a new value
    def replace_all(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
            current = current.next

    # Search for elements by a given field
    def search(self, index: int):
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    # Sort the list (assuming elements are comparable)
    def sort(self):
        if self.head is None:
            return

        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next

        values.sort()

        current = self.head
        for value in values:
            current.data = value
            current = current.next

    # Save the list to a file
    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            current = self.head
            while current:
                file.write(str(current.data) + '\n')
                current = current.next

    # Load the list from a file
    def load_from_file(self, filename):
        self.remove_all()
        with open(filename, 'r') as file:
            lines = file.read().splitlines()
            for line in lines:
                self.insert_at_end(line)


if __name__ == '__main__':
    my_list = DoublyLinkedList()

    # Insert elements
    my_list.insert_at_beginning(10)
    my_list.insert_at_end(20)
    my_list.insert_at_position(1, 15)

    # Display the list
    print(str(my_list))

    # Remove elements
    my_list.remove_at_index(1)
    my_list.remove_value(10)

    # Display the updated list
    print(str(my_list))
