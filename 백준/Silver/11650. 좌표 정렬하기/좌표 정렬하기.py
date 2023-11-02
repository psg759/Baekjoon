#11650번 좌표 정렬하기

n = int(input())

data = []

for _ in range(n):
    a, b = map(int, input().split())
    data.append((a,b))

sorted_data = sorted(data)

for i in sorted_data:
    print(i[0], i[1])