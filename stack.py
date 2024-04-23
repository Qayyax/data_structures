# Stack data structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp

    def __repr__(self):
        stack = []
        temp = self.top
        while temp is not None:
            stack.append(temp.value)
            temp = temp.next
        return " -> ".join([str(s) for s in stack])


my_stack = Stack(1)
my_stack.push(2)
print(my_stack)
