def solution(score):
    avg = []
    dict_a = {}
    cnt = 1
    for i in score:
        avg.append(sum(i) / 2)
        
    average = avg.copy()
    avg.sort(reverse=True)
    
    for i in range(len(avg)):
        if avg[i] in dict_a:
            cnt += 1
            continue
        else:
            dict_a[avg[i]] = cnt
            cnt += 1
    for i in range(len(average)):
        average[i] = dict_a[average[i]]
    
    return average