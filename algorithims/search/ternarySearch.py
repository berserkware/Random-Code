import math

def ternarySearch(low, high, target, arr):
    while high >= low:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if key == arr[mid1]:
            return mid1
        if key == mid2:
            return mid2

        if target < arr[mid1]:
            high = mid1 - 1
        elif target > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
        
    return -1

ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# Starting index
l = 0
 
# Length of list
r = 9
 
# Checking for 5
# Key to be searched in the list
key = 345634634563546
 
# Search the key using ternary search
p = ternarySearch(l, r, key, ar)
 
# Print the result
print("Index of", key, "is", p)