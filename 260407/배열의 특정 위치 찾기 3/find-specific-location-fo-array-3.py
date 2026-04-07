arr = list(map(int,input().split()))
n = len(arr)
for i in range(0,n):
    if arr[i]==0:
        rst=arr[i-3]+arr[i-2]+arr[i-1]
        break
print(rst)