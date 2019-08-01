#!/usr/bin/env python

def iterSum(arr):
    head, *tails = arr
    return head + sum(tails) if tails else head

print(iterSum([1, 10, 7, 4, 5, 9]))
