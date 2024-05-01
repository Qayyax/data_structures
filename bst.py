# Binary Search Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Loop approach
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

    # Recurssive approach
    def __r_insert(self, current_node, value):
        if current_node is None:
            # current_node = Node(value)
            return Node(value)
        if value > current_node.value:
            # setting current_node.right = Node(value)
            # but it recursivesly callsback, so new_node if None
            # else, the checks again if value > or < than
            current_node.right = self.__r_insert(current_node.right, value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        return current_node  # Return current_node to maintain tree structure

    def r_insert(self, value):
        if self.root is None:
            # need to set self.root to Node, so that,
            # self.__r_insert() would point to the other node or self.root
            # when it returns current_node
            self.root = Node(value)
        self.__r_insert(self.root, value)

    # Recussive approach as opposed to loop approach
    def __r_contains(self, current_node, value):
        if current_node is None:
            # Check if current_node is None meaning at the end of tree
            return False
        if current_node.value == value:
            return True

        if current_node.value < value:  # value > current_node.value
            return self.__r_contains(current_node.right, value)
        if current_node.value > value:  # value > current_node.value
            return self.__r_contains(current_node.left, value)

    # calling the recursion helper method
    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    # Loop approach
    def contains(self, value):
        temp = self.root
        # if self.root is None (temp is None) -> False would not trigger loop
        # so it would return False
        while temp:
            if value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
            else:
                return True
        return False

    def min_value(self, current_node):
        '''Helper function to find min value on the right
        for self.__delete()
        '''
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def __delete(self, current_node, value):
        if current_node is None:
            return None

        if value > current_node.value:
            current_node.right = self.__delete(current_node.right, value)
        elif value < current_node.value:
            current_node.left = self.__delete(current_node.left, value)
        else:  # if value == current_node.value
            # if current_node doesn't have child nodes at all
            if current_node.right is None and current_node.left is None:
                return None
            # if current_node has only one child node on the right not left
            if current_node.right is not None and current_node.left is None:
                return current_node.right
            # if current_node has only one child node on the left not right
            if current_node.left is not None and current_node.right is None:
                return current_node.right
            # if current_node has child nodes on both right and left
            if (current_node.right is not None
                    and current_node.left is not None):
                # find the min_value on the right of the current_node
                min_value = self.min_value(current_node.right)
                # change current_node value to min_value
                current_node.value = min_value
                # Delete the node that was swapped
                current_node.right = self.__delete(current_node.right,
                                                   min_value)
        return current_node

    def delete(self, value):
        self.__delete(self.root, value)

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def dfs_pre_order(self):
        # Checks all the left before checking the right
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                # always traverse left first
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def dfs_post_order(self):
        # Checks all to the left, but start appending from right
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results

    def dfs_in_order(self):
        # appends the values from lowest to highest
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print("BFS:", my_tree.BFS())
print("DFS_pre_order:", my_tree.dfs_pre_order())
print("DFS_post_order:", my_tree.dfs_post_order())
print("DFS_in_order:", my_tree.dfs_in_order())
