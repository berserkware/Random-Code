def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
  
        mergeSort(R)
  
        leftIter = rightIter = masterIter = 0
        while leftIter < len(L) and rightIter < len(R):
            if L[leftIter] < R[rightIter]: 
                arr[masterIter] = L[leftIter]
                leftIter += 1
            else:
                arr[masterIter] = R[rightIter]
                rightIter += 1
            masterIter += 1
  
        while leftIter < len(L):
            arr[masterIter] = L[leftIter]
            leftIter += 1
            masterIter += 1
  
        while rightIter < len(R):
            arr[masterIter] = R[rightIter]
            rightIter += 1
            masterIter += 1

arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)
print(arr)