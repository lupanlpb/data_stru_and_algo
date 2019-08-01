while True:
    try:
        A = list(map(int, input().strip().split()))
        A.sort()
        print(A[-1]*A[-2]*A[-3])
    except:
        break
