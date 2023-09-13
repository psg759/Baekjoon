n = int(input())

data = list(map(int, input().split()))
data_2 = []
data.sort()

for i in range(len(data)):
    data_2.append(sum(data[0:i+1]))
    
print(sum(data_2))