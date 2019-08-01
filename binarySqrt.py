# binary search

def binarySqrt(x):
    down = 0
    up = x
    mid = (down + up)/2
    while abs(mid**2 - x) >= 0.000001:
        if x < mid**2:
            up = mid
        else:
            down = mid
        mid = (down + up)/2
    return mid

#  test
x = 25
xsqrt = binarySqrt(x)
print(x, '->', xsqrt)

