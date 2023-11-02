#11651번 좌표 정렬하기 2

n = int(input())

data = []

for _ in range(n):
    a, b = map(int, input().split())
    data.append((a,b))
    
def second(array):
    return (array[1],array[0])

sorted_data = sorted(data, key=second)

for i in sorted_data:
    print(i[0], i[1])