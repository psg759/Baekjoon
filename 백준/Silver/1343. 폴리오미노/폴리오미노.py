pol = input()
p = len(pol)
cnt = 0
res = ""

for i in range(p):
    if pol[i] == "X":
        cnt += 1
    elif pol[i] == ".":
        if cnt % 4 == 0:
            res += "A" * cnt + "."
        elif cnt % 2 == 0:
            res += "A" * (cnt-2) + "B" * 2 + "."
        else:
            print(-1)
            exit()
        cnt = 0
    if i == p - 1:
        if cnt % 4 == 0:
            res += "A" * cnt
        elif cnt % 2 == 0:
            res += "A" * (cnt-2) + "B" * 2 
        else:
            print(-1)
            exit()

print(res)