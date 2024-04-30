def solution(i, j, k):
    answer = 0
    for n in range(i,j+1):
        if str(k) in str(n):
            for m in str(n):
                if m == str(k):
                    answer += 1
            
    return answer