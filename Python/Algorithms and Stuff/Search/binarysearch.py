def binarySearch(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        middle = low + (high - low) // 2

        if array[middle] == target:
            return middle
        elif array[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target = 19

result = binarySearch(array, target)

print(result)
        