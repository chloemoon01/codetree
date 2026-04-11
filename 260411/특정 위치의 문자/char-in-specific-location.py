arr = ['L', 'E' , 'B', 'R', 'O', 'S']
a = str(input())

idx=-1
for i in range(len(arr)):
    if arr[i]==a:
        idx=i
        
if idx!=0:
    print(idx)
else:
    print('None')
    




