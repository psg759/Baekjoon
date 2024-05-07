def solution(n):
    answer = 0
    m = n ** 0.5
    if m == int(m):
        return (m+1) ** 2
    else:
        return -1