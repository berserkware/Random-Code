def linearSearch(arr, target):
    for i in arr:
        if i == target:
            return arr.index(i)
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 23
print(linearSearch(arr, target))