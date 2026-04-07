arr = list(map(int,input().split()))

n = len(arr)
rst=0
a=0
cnt=0
for i in range(1,n+1):
    if i%2==0:
        rst+=i
for j in range(1,n+1):
    if j%3==0:
        cnt+=1
        a+=j
    
print(rst, a/cnt)

