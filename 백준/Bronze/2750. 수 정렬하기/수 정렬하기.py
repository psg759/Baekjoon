#2750번 수 정렬하기

data = []
n = int(input())

for _ in range(n):
    data.append(int(input()))
    
data.sort()

for i in data:
    print(i)