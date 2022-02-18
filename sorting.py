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
