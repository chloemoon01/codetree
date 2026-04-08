rst = 0

for r in range(4):
    arr = list(map(int, input().split()))
    for c in range(r + 1):   
        rst += arr[c]

print(rst)
