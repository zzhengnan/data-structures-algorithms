class MinHeap:
    """MinHeap.

                  Time      Space
    build_heap    n         1
    push          log(n)    1
    remove        log(n)    1
    sift_up       log(n)    1
    sift_down     log(n)    1
    """
    def __init__(self, array):
        self.heap = array
        self.build_heap()

    @property
    def size(self):
        return len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def sift_up(self):
        """Iteratively sift child node up the heap."""
        child_idx = self.size - 1
        parent_idx = (child_idx - 1) // 2
        while parent_idx >= 0 and self.heap[parent_idx] > self.heap[child_idx]:
            self.swap(child_idx, parent_idx)
            child_idx = parent_idx
            parent_idx = (child_idx - 1) // 2

    def sift_down(self, parent_idx=0):
        """Iteratively sift given parent node down the heap.

        Optional parent_idx is used when building the heap.
        """
        left_idx = parent_idx * 2 + 1
        while left_idx < self.size:
            if left_idx == self.size - 1:
                # Only left child exists; swap parent with left if appropriate
                if self.heap[parent_idx] <= self.heap[left_idx]:
                    break
                self.swap(parent_idx, left_idx)
                parent_idx = left_idx
            else:
                # Both children exist; swap parent with min(left, right) if appropriate
                right_idx = left_idx + 1
                if self.heap[parent_idx] <= self.heap[left_idx] and self.heap[parent_idx] <= self.heap[right_idx]:
                    break
                smaller = left_idx if self.heap[left_idx] <= self.heap[right_idx] else right_idx
                self.swap(parent_idx, smaller)
                parent_idx = smaller
            left_idx = parent_idx * 2 + 1

    def build_heap(self):
        """Build heap by iteratively sifting parent nodes down the heap.

        This is more optimal from a time complexity point of view than the alternative -- iteratively adding child nodes
        at the end and sifting them up the heap, which runs in O(n * log(n)).
        """
        parent_idx = (self.size - 2) // 2  # Last parent node with child
        while parent_idx >= 0:
            self.sift_down(parent_idx)
            parent_idx -= 1

    def push(self, value):
        self.heap.append(value)
        self.sift_up()

    def pop(self):
        self.swap(0, self.size - 1)
        value = self.heap.pop()
        self.sift_down()
        return value

    def peek(self):
        return self.heap[0]
