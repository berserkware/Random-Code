import math

def jumpSearch(arr, target, length):
    step = math.sqrt(length)

    prev = 0
    while arr[int(min(step, length) - 1)] < target:
        prev = step
        step += math.sqrt(length)
        if prev >= length:
            return -1

    while arr[int(prev)] < target:
        prev += 1

        if prev == min(step, length):
            return -1

    if arr[int(prev)] == target:
        return prev
    
    return -1

arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610 ]
x = 34
n = len(arr)
 
print(jumpSearch(arr, x, n))