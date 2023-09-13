n, k = map(int, input().split())
data = [0] * n
result = 0

for i in range(n):
    data[i] = int(input())
    
data.sort(reverse=True)

for a in data:
    if k != 0:
        result += k //a
        k %= a
    else:
        break  
          
print(result)


    
    
