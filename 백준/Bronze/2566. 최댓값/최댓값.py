arr = []
max_arr = [] 

for i in range(9):
    arr.append(list(map(int, input().split())))
    
max = arr[0][0]
    
for i in range(9):
    for j in range(9):
        if arr[i][j] >= max:
             max = arr[i][j]
             max_arr.append([i,j])
    
last = max_arr[-1]
print(max)
print(last[0]+1, last[1]+1)