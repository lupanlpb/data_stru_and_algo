# binary search

def binarySearch(arr, target):
    '''
    search the first element which is equal to target
    '''
    head = 0
    tail = len(arr) - 1
    while head <= tail:
        mid = (head + tail)//2
        if arr[mid] > target:
            tail =  mid - 1
        elif arr[mid] < target:
            head = mid + 1
        else:
            if mid == 0 or arr[mid - 1] != target:
                return mid
            else:
                tail = mid - 1

    return "The target don't exist"

mylist = [1, 3, 5, 5, 7, 7, 9]
print(mylist)
print(5, binarySearch(mylist, 5))
print(7, binarySearch(mylist, 7))
print(-1, binarySearch(mylist, -1))

