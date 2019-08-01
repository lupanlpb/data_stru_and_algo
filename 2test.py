
def sums(lists):
    if lists == []:
        return 0
    else:
        return lists[0] + sums(lists[1:])

print(sums([1, 10, 7, 4, 5, 9]))
