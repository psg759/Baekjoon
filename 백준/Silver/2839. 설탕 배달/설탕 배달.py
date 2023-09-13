n = int(input())
max_n = n // 5
data = []
data_2 = []


for x in range(max_n+1):
    if (n - 5 * x) % 3 == 0:
        data.append((x,(n - 5 * x) / 3))
        
        
if len(data) == 0:
    print(-1)
else:
    for j in data:
        data_sum = sum(j)
        data_2.append(data_sum)
        
    print(int(min(data_2)))
        