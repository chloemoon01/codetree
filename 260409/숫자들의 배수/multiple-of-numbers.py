n = int(input())

arr = []
cnt = 1    
five = 0   

while five < 2:
    rst = n * cnt        # n의 cnt번째 배수
    arr.append(rst)

    if rst% 5 == 0:
        five += 1             # 5의 배수 카운트 증가

    cnt += 1

print(*arr)
