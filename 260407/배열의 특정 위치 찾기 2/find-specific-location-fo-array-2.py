arr = list(map(int,input().split()))
a = len(arr)

jj=0
h=0
for i in range(0,a):
    if i%2==0:
        jj+=arr[i]
    else:
        h+=arr[i]
if jj>h:
    print(jj-h)
else:
    print(h-jj)