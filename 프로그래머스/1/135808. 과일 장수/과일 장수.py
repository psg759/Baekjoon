def solution(k, m, score):
    answer = []
    price = 0
    score = sorted(score, reverse=True)
    
    for i in range(len(score)):
        answer.append(score[i])
        if len(answer) == m:
            price += min(answer) * m
            answer = []
        
    return price