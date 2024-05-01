def solution(num, total):
    answer = []
    
    if total == 0:
        for k in range(-((num - 1)//2), ((num - 1)//2)+1):
            answer.append(k)
        return answer
    
    for i in range(-total,total+1):
        for j in range(i,i+num):
            answer.append(j)
        if sum(answer) == total:
            return answer
        else:
            answer = []
    