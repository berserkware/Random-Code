def bubbleSort(arr):
    arrlen = len(arr)

    for i in range(arrlen):
        for j in range(0, arrlen-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
print(arr)
bubbleSort(arr)
print(arr)