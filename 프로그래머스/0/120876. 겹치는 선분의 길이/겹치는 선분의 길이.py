def solution(lines):
    a, b, c = [], [], []
    n = 0
    for i in lines:
        n += 1
        for j in range(i[0],i[1]+1):
            if n == 1:
                a.append(j)
            elif n == 2:
                b.append(j)
            else:
                c.append(j)
    a = set(a)
    b = set(b)
    c = set(c)
    d = a.intersection(b)
    e = a.intersection(c)
    f = b.intersection(c)
    
    #교집합이 아예 없는 경우(셋다 len이 0)
    if len(d) in [1,0] and len(e) in [1,0] and len(f) in [1,0]: 
        return 0
    #교집합이 한개 있는 경우(둘만 len이 0)
    elif len(d) == 0 and len(e) == 0 and len(f) != 0:
        f = list(f)
        return (max(f) - min(f))
    elif len(d) == 0 and len(e) != 0 and len(f) == 0:
        e = list(e)
        return (max(e) - min(e))
    elif len(d) != 0 and len(e) == 0 and len(f) == 0:
        d = list(d)
        return (max(d) - min(d))
    #교집합이 두개 있는 경우(하나만 len이 0)
    elif len(d) == 0 and len(e) != 0 and len(f) != 0:
        e = list(e)
        f = list(f)
        return (max(e) - min(e)) + (max(f) - min(f))
    elif len(d) != 0 and len(e) == 0 and len(f) != 0:
        d = list(d)
        f = list(f)
        return (max(d) - min(d)) + (max(f) - min(f))
    elif len(d) != 0 and len(e) != 0 and len(f) == 0:
        e = list(e)
        d = list(d)
        return (max(e) - min(e)) + (max(d) - min(d))
    #교집합이 3개 있는 경우
    elif len(d) != 0 and len(e) != 0 and len(f) != 0:
        d = d.union(e)
        d = d.union(f)
        d = list(d)
        return (max(d) - min(d))