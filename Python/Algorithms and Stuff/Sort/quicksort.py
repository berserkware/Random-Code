def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if start < end:
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end

def quickSort(start, end, array):
    if start < end:
        p = partition(start, end, array)

        quickSort(start, p - 1, array)
        quickSort(p + 1, end, array)

array = [6, 8, 2, 0, 3, 5, 2]
quickSort(0, len(array) - 1, array)
print(array)