n = int(input())

arr = []
arr.append(1)
arr.append(n)

i = 2
while True:
    k = arr[i-2] + arr[i-1]  
    arr.append(k)             
    if k >= 100:              
        break
    i += 1                     

print(*arr)
