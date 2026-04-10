a, b = map(int, input().split())
arr = []

while True:
    if a <= 1:
        break
    k = a % b        
    a = a // b      
    arr.append(k)

# 나머지 등장 횟수 카운팅
count_arr = [0] * b
for k in arr:
    count_arr[k] += 1

# 횟수 제곱 후 합산
rst = 0
for cnt in count_arr:
    rst += cnt ** 2

print(rst)
