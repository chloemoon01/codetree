N = int(input())
arr = map(int,input().split())
rst=[]
for i in arr:
    if i%2==0:
        rst.append(i)
rst.reverse()
print(*rst)
