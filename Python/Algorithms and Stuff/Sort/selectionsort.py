def selectionsort(arr):
    for i in range(len(arr)):
        min_indx = i
        for j in range(i+1, len(arr)):
            if arr[min_indx] > arr[j]:
                min_indx = j

        arr[i], arr[min_indx] = arr[min_indx], arr[i]

arr = [6, 4, 2, 9, 5]
selectionsort(arr)
print(arr)

