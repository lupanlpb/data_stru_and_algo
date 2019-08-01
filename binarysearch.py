# binary search

def binarySearch(arr, target):
    head = 0
    tail = len(arr) - 1
    while head <= tail:
        mid = (head + tail)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            head = mid + 1
        else:
            tail = mid - 1
    return "The target don't exist"

mylist = [1, 3, 5, 7, 9]
print(binarySearch(mylist, 7))
print(binarySearch(mylist, -1))

