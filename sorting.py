def quicksort(array, start=None, end=None):
    """Quicksort.

    Steps
      1. Set 3 pointers -- pivot, left, and right
      2. Advance left pointer if left <= pivot, right pointer if right >= pivot, swapping if necessary
      3. Repeat until left and right pointers cross
      4. Swap pivot with right pointer
      5. Recurse in left and right subarrays

               Time          Space
    Average    n * log(n)    log(n)
    Best       n * log(n)    log(n)
    Worst      n^2           n

    Worst case space complexity can in theory be optimized to log(n) using Sedgewick's trick.
    However, Python's lack of support for tail recursion makes this difficult while using a
    recursive algorithm; might be possible with iterative algorithm.
    https://en.wikipedia.org/wiki/Quicksort#Space_complexity
    """
    if start is None and end is None:
        start = 0
        end = len(array) - 1

    if start >= end:
        return array

    pivot = start
    left = pivot + 1
    right = end

    while left <= right:
        if array[right] < array[pivot] < array[left]:
            array[left], array[right] = array[right], array[left]
        if array[left] <= array[pivot]:
            left += 1
        if array[right] >= array[pivot]:
            right -= 1
    array[pivot], array[right] = array[right], array[pivot]

    quicksort(array, start, right - 1)
    quicksort(array, right + 1, end)

    return array


def heapsort(array):
    """Heapsort.

    Steps
      1. Build a max heap out of original array
      2. Conceptualize original array as consisting of two subarrays where
        - Left subarray is unsorted
        - Right subarray is sorted
        - At start of algorithm, left subarray is original array and right subarray is empty
      3. Swap first and last elements in left subarray, effectively expanding right subarray
         and shrinking left subarray by 1
      4. Sift down first element in left subarray in order to maintain heap property

               Time          Space
    Average    n * log(n)    1
    Best       n * log(n)    1
    Worse      n * log(n)    1

    Best case time complexity doesn't include special case where original array contains all dupes,
    in which case time complexity is O(n).
    """
    def build_max_heap(array):
        parent_idx = (len(array) - 2) // 2  # Last parent node with a child
        while parent_idx >= 0:
            sift_down(array, parent_idx)
            parent_idx -= 1

    def sift_down(array, parent_idx=0, end=None):
        if end is None:
            end = len(array) - 1

        left_idx = 2 * parent_idx + 1
        while left_idx <= end:
            if left_idx == end:
                # Only left child exists; swap parent with left if appropriate
                if array[parent_idx] >= array[left_idx]:
                    break
                array[parent_idx], array[left_idx] = array[left_idx], array[parent_idx]
                parent_idx = left_idx
            else:
                # Both children exist; swap parent with max(left, right) if appropriate
                right_idx = left_idx + 1
                if array[parent_idx] >= array[left_idx] and array[parent_idx] >= array[right_idx]:
                    break
                bigger = left_idx if array[left_idx] >= array[right_idx] else right_idx
                array[parent_idx], array[bigger] = array[bigger], array[parent_idx]
                parent_idx = bigger
            left_idx = parent_idx * 2 + 1

    build_max_heap(array)
    boundary = len(array) - 1
    while boundary > 0:
        array[0], array[boundary] = array[boundary], array[0]
        boundary -= 1
        sift_down(array, end=boundary)
    return array
