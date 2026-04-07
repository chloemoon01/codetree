arr = list(map(int,input().split()))

n = len(arr)
rst=0
a=0
cnt=0
for i in range(1,n,2):
    rst+=arr[i]
for j in range(2,n,3):
    cnt+=1
    a+=arr[j]
    
print(f'{rst} {a/cnt:.1f}')

