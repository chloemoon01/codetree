for _ in range(5):
    arr = list(map(str,input().split()))
    for i in range(3):
        arr[i]=arr[i].upper()

    print(*arr)
