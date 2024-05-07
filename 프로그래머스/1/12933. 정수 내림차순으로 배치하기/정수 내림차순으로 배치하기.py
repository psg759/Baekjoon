def solution(n):
    answer = 0
    n = str(n)
    n = list(n)
    n.sort(reverse = True)
    n = ''.join(n)
    return int(n)