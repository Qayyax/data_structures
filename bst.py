# Binary Search Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while temp:
            if temp.value == new_node.value:
                return False
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left

    def contains(self, value):
        temp = self.root
        # if self.root is None -> False would not trigger loop
        # so it would return False
        while temp:
            if value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
            else:
                return True
        return False


my_tree = BinarySearchTree()
my_tree.insert(2)
print(my_tree.root.value)
my_tree.insert(1)
print(my_tree.root.left.value)
my_tree.insert(3)
print(my_tree.root.right.value)
print(my_tree.contains(8))
