def solution(sizes):
    a_1 = []
    a_2 = []
    for i in sizes:
        a_1.append(max(i))
        a_2.append(min(i))
    return max(a_1) * max(a_2)