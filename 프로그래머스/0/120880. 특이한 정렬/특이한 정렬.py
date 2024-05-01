def solution(numlist, n):
    absolute = []
    for i in range(len(numlist)):
        absolute.append([numlist[i],abs(n - numlist[i])])
    
    absolute.sort(key = lambda x : x[1])
    for i in range(len(absolute)-1):
        if absolute[i][1] == absolute[i+1][1]:
            if absolute[i][0] < absolute[i+1][0]:
                tmp = absolute[i][0]
                absolute[i][0] = absolute[i+1][0]
                absolute[i+1][0] = tmp
    answer = [i[0] for i in absolute]
    return answer
        
            
       