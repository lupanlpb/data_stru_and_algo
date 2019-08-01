#!/usr/bin/env python

def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [ele for ele in arr[1:] if ele <= pivot]
        greater = [ele for ele in arr[1:] if ele > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([10, 5, 2, 1, 10, 34, 6, 9, 7, 3, 8]))
