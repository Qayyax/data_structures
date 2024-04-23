# LinkedList data structure
# Node class because we don't want to create a new node everytime
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Linkedlist class which would create a new node everytime
class Linkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node  # Pointer to the new node
        self.tail = new_node  # Pointer to the new node
        self.lenght = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1
        return True

    def pop(self):
        if self.lenght == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.lenght -= 1
        if self.lenght == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.lenght += 1
        return True

    def pop_first(self):
        if self.lenght == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.lenght -= 1
        if self.lenght == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.lenght:
            return None
        current_node = self.head
        for _ in range(0, index):
            current_node = current_node.next
        return current_node

    def set_value(self, index, value):
        index = self.get(index)
        if index:
            index.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.lenght:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.lenght:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.lenght += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.lenght:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.lenght - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.lenght -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.lenght):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def __repr__(self):
        temp_node = self.head  # starting from the first node
        word = []
        while temp_node is not None:  # temp_node is none when .next == None
            word.append(str(temp_node.value))
            temp_node = temp_node.next
        return " -> ".join(word)


llist = Linkedlist(0)
llist.append(2)
llist.insert(1, 1)
print(llist)

llist.reverse()
print(llist)
