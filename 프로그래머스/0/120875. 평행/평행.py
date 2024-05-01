import math
def solution(dots):
    for cnt in range(1,4):
        #1,2 & 3,4
        if cnt == 1:
            a = dots[1][1] - dots[0][1]
            b = dots[1][0] - dots[0][0]
            c = dots[3][1] - dots[2][1]
            d = dots[3][0] - dots[2][0]
        # 1,3 & 2,4
        elif cnt == 2:
            a = dots[2][1] - dots[0][1]
            b = dots[2][0] - dots[0][0]
            c = dots[3][1] - dots[1][1]
            d = dots[3][0] - dots[1][0]
        # 1,4 & 2,3
        elif cnt == 3:
            a = dots[3][1] - dots[0][1]
            b = dots[3][0] - dots[0][0]
            c = dots[2][1] - dots[1][1]
            d = dots[2][0] - dots[1][0]

        # Handle vertical lines
        if b == 0 and d == 0:
            return 1
        # Handle horizontal lines
        elif a == 0 and c == 0:
            return 1
        # Compare slopes using cross multiplication to avoid floating-point issues
        elif a * d == b * c:
            return 1

    return 0