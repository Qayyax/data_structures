class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        # plus 1 because we want to start with index 1 (but still 0)
        return 2 * index + 1

    def _right_child(self, index):
        # would have been plus 1 for index 2 (but 3 cause index 0)
        return 2 * index + 2

    def _parent(self, index):
        # -1 cause we started from 0 and not index 1
        return (index - 1) // 2

    def _swap(self, index1, index2):
        # Swaps the value of 2 indexes
        self.heap[index1], self.heap[index2] = (
            self.heap[index2],
            self.heap[index1]
        )

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1  # index of the appended value

        while (current > 0 and  # not at the 0 index
               # value of current index > than value at it's parents
               self.heap[current] > self.heap[self._parent(current)]
               ):
            # Keep swapping until condition is False
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        # We only remove the max value (MaxHeap)
        # or the min value (MinHeap)
        # Then sinkdown to make it a complete graph
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()  # remove & bring the last value to top
        self._sink_down(0)

        return max_value

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (
                left_index < len(self.heap) and
                self.heap[left_index] > self.heap[max_index]
                    ):
                # setting only max_index because right might be greater as well
                max_index = left_index
            if (
                right_index < len(self.heap) and
                self.heap[right_index] > self.heap[max_index]
                    ):
                # comparing with value at max index and not index
                # (comparing with left)
                max_index = right_index

            if max_index != index:
                # if the value is currently not the highest
                self._swap(max_index, index)
                index = max_index
            else:
                return

    def __repr__(self):
        return f"[{', '.join(str(x) for x in self.heap)}]"


myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)
myheap.insert(100)
myheap.insert(75)
myheap.remove()
myheap.remove()
myheap.remove()
print(myheap)
