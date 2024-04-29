def solution(l, r):
    answer = []
    for i in range(l, r+1):
        i = str(i)
        s = set(i)
        if s == {'5'} or s == {'0'} or s == {'5', '0'} or s == {'0','5'}:
            answer.append(int(i))
    if answer == []:
        return [-1]
    return answer