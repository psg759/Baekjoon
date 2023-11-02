#10814번 나이순 정렬

data = []

n = int(input())
min = 0

for _ in range(n):
    a,b = input().split()
    a = int(a) 
    data.append((a,b))
    
def first(array):
    return array[0]
    
sorted_data = sorted(data,key=first)

for i in sorted_data:
    a = i[0]
    b = i[1]
    print(a,b)