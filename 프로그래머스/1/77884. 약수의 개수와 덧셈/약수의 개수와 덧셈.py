import math
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        num = {1}
        for j in range(1, int(math.sqrt(i))+1):
            if i % j == 0:
                num.add(i // j)
                num.add(j)
        num = list(num)
        if len(num) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer