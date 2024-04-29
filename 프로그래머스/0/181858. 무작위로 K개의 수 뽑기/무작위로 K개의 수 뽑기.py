def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if arr[i] not in answer and len(answer) < k:
            answer.append(arr[i])
    if len(answer) < k:
        n = k-len(answer)
        for i in range(n):
            answer.append(-1)
    
    return answer