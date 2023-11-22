class Node:
    def __init__(self, data: str):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    def _add_to_empty(self, data: str):

        if self.last is not None:
            return self.last

        # allocate memory to the new node and add data to the node
        new_node = Node(data)

        # assign last to new_node
        self.last = new_node

        # create link to itself
        self.last.next = self.last
        return self.last

    def __str__(self):
        if self.last is None:
            return "The list is empty"

        s = ''
        new_node = self.last.next
        while new_node:
            s += str(new_node.data) + ' -> '
            new_node = new_node.next
            if new_node == self.last.next:
                break
        return s

    # add node to the front
    def add_front(self, data):

        # check if the list is empty
        if self.last is None:
            return self._add_to_empty(data)

        # allocate memory to the new node and add data to the node
        new_node = Node(data)

        # store the address of the current first node in the new_node
        new_node.next = self.last.next

        # make new_node as last
        self.last.next = new_node

        return self.last

    # add node to the end
    def add_end(self, data):
        # check if the node is empty
        if self.last is None:
            return self._add_to_empty(data)

        # allocate memory to the new node and add data to the node
        new_node = Node(data)

        # store the address of the last node to next of new_node
        new_node.next = self.last.next

        # point the current last node to the new_node
        self.last.next = new_node

        # make new_node as the last node
        self.last = new_node

        return self.last

    # insert node after a specific node
    def add_after(self, data, item):

        # check if the list is empty
        if self.last is None:
            return None

        new_node = Node(data)
        p = self.last.next
        while p:

            # if the item is found, place new_node after it
            if p.data == item:

                # make the next of the current node as the next of new_node
                new_node.next = p.next

                # put new_node to the next of p
                p.next = new_node

                if p == self.last:
                    self.last = new_node
                    return self.last
                else:
                    return self.last
            p = p.next
            if p == self.last.next:
                print(item, "The given node is not present in the list")
                break

    # delete a node
    def delete_node(self, key):

        # If linked list is empty
        if self.last is None:
            return

        # If the list contains only a single node
        if self.last.data == key and self.last.next == self.last:
            self.last = None

        temp = self.last
        d = None

        # if last node is to be deleted
        if self.last.data == key:

            # find the node before the last node
            while temp.next != self.last:
                temp = temp.next

            # point temp node to the next of last i.e. first node
            temp.next = self.last.next
            self.last = temp.next

        # travel to the node to be deleted
        while temp.next != self.last and temp.next.data != key:
            temp = temp.next

        # if node to be deleted was found
        if temp.next.data == key:
            d = temp.next
            temp.next = d.next

        return self.last

    def traverse(self):
        if self.last is None:
            print("The list is empty")
            return

        new_node = self.last.next
        while new_node:
            print(new_node.data, end=" ")
            new_node = new_node.next
            if new_node == self.last.next:
                break

    def get_every_n(self, n, count):

        if self.last is None:
            return "The list is empty"

        cll = CircularLinkedList()
        this_count, i = 0, 0

        new_node = self.last.next
        while this_count < count:
            i += 1
            if i % n == 0:
                cll.add_end(new_node)
                this_count += 1
            new_node = new_node.next
