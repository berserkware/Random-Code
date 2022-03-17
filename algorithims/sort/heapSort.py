def heapify(arr, length, i):
    largest = i 
    left = 2 * i + 1    
    right = 2 * i + 2     
 
    if left < length and arr[largest] < arr[left]:
        largest = left
 
    if right < length and arr[largest] < arr[right]:
        largest = right
 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
 
        heapify(arr, length, largest)
 
def heapSort(arr):
    length = len(arr)
 
    for i in range(length//2 - 1, -1, -1):
        heapify(arr, length, i)

    for i in range(length-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print(arr)