def solution(polynomial):
    n = 0
    m = 0
    polynomial = polynomial.split(' + ')
    for i in polynomial:
        if 'x' in i:
            i=i.split("x")
            if i[0] == '':
                n += 1
            elif i[0] == '-':
                n -= 1
            else:
                n += int(i[0])
        else:
            m += int(i)
    
    if  n == 0 and m == 0:
        return "0"
    elif n == 0:
        return f"{m}"
    elif n == 1:
        if m == 0:
            return "x"
        else:
            return f"x + {m}"
    elif n == -1:
        if m == 0:
            return "-x"
        else:
            return f"-x + {m}"
    elif m == 0:
        return f"{n}x"
    else:
        return f"{n}x + {m}"