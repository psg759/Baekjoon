def solution(picture, k):
    for i in range(len(picture)):
        n = list(picture[i])
        for j in range(len(n)):
            n[j] = k*n[j]
        n = ''.join(n)
        picture[i] = n
        
    answer = []
    for i in range(len(picture)):
        for j in range(k):
            answer.append(picture[i])
    return answer