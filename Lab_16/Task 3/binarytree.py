from tkinter import messagebox


class Node:
    def __init__(self, key, string):
        self.left = None
        self.right = None
        self.key = key
        self.string = string


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, string):
        self.root = self._insert(self.root, key, string)

    def _insert(self, root, key, string):
        if root is None:
            return Node(key, string)
        if key < root.key:
            root.left = self._insert(root.left, key, string)
        else:
            root.right = self._insert(root.right, key, string)
        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            messagebox.showerror("Error", "Element is not in the tree.")
            return None
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self.min_value_node(root.right).key
            root.right = self._delete(root.right, root.key)
        return root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        result = {}
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result[root.key] = root.string
            self._inorder_traversal(root.right, result)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None:
            return None
        if root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)
