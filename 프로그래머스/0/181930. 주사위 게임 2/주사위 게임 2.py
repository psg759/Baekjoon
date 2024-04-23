def solution(a, b, c):
    point = 0
    d = a+b+c
    dd = d * (a**2+b**2+c**2)
    ddd = dd * (a**3+b**3+c**3)
    if a != b and a != c and b !=c :
        point += d
    elif a != b == c or a == b != c or a == c != b:
        point += dd
    elif a == b == c:
        point += ddd
    return point