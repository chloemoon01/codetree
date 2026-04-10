arr = list(map(int,input().split()))
cnt=[0]*7

for _ in arr:
    cnt[_]+=1

for i in range(1,7):
    print(f'{i} - {cnt[i]}')
