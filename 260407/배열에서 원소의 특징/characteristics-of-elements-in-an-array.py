arr = list(map(int,input().split()))

a = len(arr)

for i in range(0,a):
    if arr[i]%3==0:
        rst=arr[i-1]
        break
print(rst)