def solution(dots):
    if dots[1][0] != dots[0][0]:
        r = abs(dots[1][0] - dots[0][0])
    elif dots[2][0] != dots[0][0]:
        r = abs(dots[2][0] - dots[0][0])
    elif dots[3][0] != dots[0][0]:
        r = abs(dots[3][0] - dots[0][0])
        
    if dots[1][1] != dots[0][1]:
        c = abs(dots[1][1] - dots[0][1])
    elif dots[2][1] != dots[0][1]:
        c = abs(dots[2][1] - dots[0][1])
    elif dots[3][1] != dots[0][1]:
        c = abs(dots[3][1] - dots[0][1])
    answer = r * c
    return answer