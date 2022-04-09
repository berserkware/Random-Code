def interpolationSearch(arr, low, high, target):
    if low <= high and x >= arr[low] and target <= arr[high]:

        pos = low + ((high - low) // (arr[high] - arr[low]) * (target - arr[low]))

        if arr[pos] == target:
            return pos

        if arr[pos] < target:
            return interpolationSearch(arr, pos + 1, high, target)
        
        if arr[pos] > x:
            return interpolationSearch(arr, low, pos - 1, target)

    return -1

arr = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)
 
# Element to be searched
x = 6358435863658358484348453
index = interpolationSearch(arr, 0, n - 1, x)
 
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")