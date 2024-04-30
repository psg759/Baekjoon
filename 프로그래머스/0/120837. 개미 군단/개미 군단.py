def solution(hp):
    answer = 0
    j = hp // 5
    hp %= 5
    b = hp // 3
    hp %= 3
    i = hp // 1
    return j + b + i