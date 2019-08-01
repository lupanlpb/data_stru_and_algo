#!/bin/env python

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0
    sortedArr = []
    while i < len(left) and  j < len(right):
        if left[i] <= right[j]:
            sortedArr.append(left[i])
            i += 1
        else:
            sortedArr.append(right[j])
            j += 1
    sortedArr += left[i:]
    sortedArr += right[j:]
    return sortedArr

# test
arr = [5,3,0,6,1,4]
print('arr: ', arr)
print('sortedArr: ', mergeSort(arr))
