# Queues data structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1
        return temp

    def __repr__(self):
        queue = []
        temp = self.first
        while temp is not None:
            queue.append(temp.value)
            temp = temp.next
        return " -> ".join([str(q) for q in queue])


my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.dequeue()
my_queue.dequeue()
print(my_queue)
