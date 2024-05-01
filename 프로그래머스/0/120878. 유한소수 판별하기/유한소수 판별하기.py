import math
def solution(a, b):
    c = math.gcd(a,b)
    if c == 1:
        pass    
    else:
        b //= c
        
    while b % 2 == 0 or b % 5 == 0:
        if b % 2 == 0:
            b //= 2
        elif b % 5 == 0:
            b //= 5
            
    if b == 1:
        return 1
    else:
        return 2
