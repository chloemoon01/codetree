a, b = map(int, input().split()) 

arr = [0] * 10
arr[0] = a
arr[1] = b

# 3번째 항부터 (인덱스 2~9)
for i in range(2, 10):          
    arr[i] = (arr[i-2] + arr[i-1]) % 10 

print(*arr)
