#!usr/bin/env python
'''
    This program implementes the select sort.
'''

# find the smallest element and it's corresponding index in the array 
def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# get the sorted array
def selectSort(arr):
    newarr = []
    for i in range(len(arr)):
        smallest_index = findsmallest(arr)
        newarr.append(arr.pop(smallest_index))
    return newarr

# test selection sort 
print(selectSort([5, 3, 6, 2, 10]))
print(selectSort([5, 6, 3, 2, 10, 12, 1, 3, 5, 8, 20]))
