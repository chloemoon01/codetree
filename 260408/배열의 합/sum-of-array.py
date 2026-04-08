rst=0
for _ in range(1,5):
    arr = list(map(int,input().split()))
    for i in range(0,4):
        rst+=arr[i]
    print(rst)
    rst=0    