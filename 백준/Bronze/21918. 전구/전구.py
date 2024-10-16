n, m = map(int, input().split())

bulb = input().split()

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        bulb[b-1] = str(c)
    elif a == 2:
        for i in range(b-1, c):
            bulb[i] = '1'  if bulb[i] == '0' else '0'
    elif a == 3:
        for i in range(b-1, c):
            bulb[i] = '0'
    elif a == 4:
        for i in range(b-1, c):
            bulb[i] = '1'
    
print(' '.join(bulb))