def solution(arr):
    cnt = 0
    n = len(arr)
    answer = [False] * n * n
    for i in range(n):
        for j in range(n):
            if arr[i][j] == arr[j][i]:
                answer[cnt] = True
            cnt += 1
            
    if False in answer:
        return 0
    else:
        return 1