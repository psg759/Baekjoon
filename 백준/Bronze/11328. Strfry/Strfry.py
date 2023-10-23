#11328번 Strfry

n = int(input())
data = []

for _ in range(n):
    a,b = input().split()
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    if a == b:
        print('Possible')
    else:
        print('Impossible')
    
        
        