tmp = [0] * 31
for i in range(28):
    n = int(input())
    tmp[n] += 1

for i, j in enumerate(tmp):
    if j == 0 and i != 0:
        print(i) 