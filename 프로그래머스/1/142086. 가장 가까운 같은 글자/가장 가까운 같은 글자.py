def solution(s):
    answer = []
    ind = {}
    for i in range(len(s)):
        if s[i] not in ind:
            answer.append(-1)
            ind[s[i]] = i
        else:
            answer.append(i - ind[s[i]])
            ind[s[i]] = i
    return answer