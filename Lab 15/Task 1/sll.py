class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


    # Display elements of the list
    def __str__(self):
        s = ''
        current = self.head
        while current:
            s += current.data + " -> "
            current = current.next
        return s

    # Get the number of elements in the list
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size is None

    # Insert elements into the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def insert_at_position(self, data, position: int):
        if position < 0:
            position = 0
        if position > self.size:
            position = self.size

        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    # Remove elements from the list
    def remove_all(self):
        self.head = None
        self.size = 0

    def remove_at_index(self, index: int):
        if 0 <= index < self.size:
            if index == 0:
                self.head = self.head.next
            else:
                current = self.head
                for _ in range(index - 1):
                    current = current.next
                current.next = current.next.next
            self.size -= 1

    def remove_value(self, value, mul=False):
        current = self.head
        while current and current.data == value:
            self.head = current.next
            current = self.head
            self.size -= 1
            if not mul:
                return
        while current:
            if current.next and current.next.data == value:
                current.next = current.next.next
                self.size -= 1
                if not mul:
                    return
            current = current.next

    def remove_values(self, values):
        for value in values:
            self.remove_value(value, mul=True)

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

    # Search for element by a given index
    def search(self, index: int):
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    # Sort the list (assuming elements are comparable)
    def sort(self):
        if not self.head:
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
    my_list = SinglyLinkedList()

    # Insert elements
    my_list.insert_at_beginning(10)
    my_list.insert_at_end(20)
    my_list.insert_at_position(1, 15)

    # Display the list and its size
    print(str(my_list))
    print("Size:", my_list.size)

    # Remove elements
    my_list.remove_at_index(1)
    my_list.remove_value(10)

    # Display the updated list and its size
    print(str(my_list))
    print("Size:", my_list.size)

