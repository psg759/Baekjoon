def solution(a, b, n):
    coke = 0
    while n > a-1:
        coke += (n // a)*b
        m = n % a
        n = (n // a)*b
        n += m
    return coke