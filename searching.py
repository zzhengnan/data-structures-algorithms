def quickselect(array, k):
    """Select k'th smallest element from array.

    Steps
      1. Perform quicksort
      2. After each pass, once pivot has been moved into correct position,
         search in either left or right subarray (not both)

               Time          Space
    Average    n             1
    Best       n             1
    Worst      n^2           1
    """
    target_idx = k - 1
    start = 0
    end = len(array) - 1

    while start != end:
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

        if right == target_idx:
            start = end = right
        elif right < target_idx:
            start = right + 1
        else:
            end = right - 1

    return array[start]
