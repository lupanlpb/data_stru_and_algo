def bubbleSort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':
    arr = [54, 26, 93, 77, 44, 31, 44, 55, 20]
    print('initial array: %s' % arr)
    bubbleSort(arr)
    print('Sorted array: %s' % arr)
