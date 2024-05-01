import math
def solution(numer1, denom1, numer2, denom2):
    result = []
    demon = math.gcd(denom1, denom2)
    #분모에 공약수가 없는 경우
    if demon == 1:
        # 분모가 둘 다 1인 경우
        if denom1 == denom2:
            return [numer1+numer2,1]
        up = numer1 * denom2 + numer2 * denom1
        down = denom1 * denom2
        n = math.gcd(up, down)
        if n == 1:
            return [up, down]
        else:
            up //= n
            down //= n
            return [up, down]
    #분모에 공약수가 있는 경우
    else:
        up = numer1 * denom2 + numer2 * denom1
        down = denom1 * denom2
        m = math.gcd(up,down)
        #분수를 더한 값 자체가 기약분수인경우
        if  m == 1:
            return [up,down]
        #분수를 더한 값이 기약분수가 아닌 경우 (최대공약수로 나누어서 기약분수를 만듬)
        else:
            up //= m
            down //= m
            return [up, down]