h = {}
h_i = []
for _ in range(int(input())):
    hh = input().split('.')[-1]
    if hh in h:
        h[hh] += 1
    else:
        h[hh] = 1
        h_i.append(hh)
        
h_i.sort()

for i in h_i:
    print(i, h[i])
