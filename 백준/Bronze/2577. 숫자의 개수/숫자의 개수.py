#2577번 숫자의 개수

a = int(input())
b = int(input())
c = int(input())
data = [0] * 10
res = str(a * b * c)
for i in range(len(res)):
    data[int(res[i])] += 1

for i in data:
    print(i)