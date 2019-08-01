while True:
    try:
        if input().split() == '':
            break
        else:
            print(sum(map(int,input().split())))
    except:
        pass
