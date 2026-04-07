n = int(input())
cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        cnt+=2
        print(cnt,end=' ')
        if cnt==8:
            cnt=0
    print()
