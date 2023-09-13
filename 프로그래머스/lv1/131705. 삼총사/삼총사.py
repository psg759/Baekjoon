from itertools import combinations

def solution(number):
    result = []
    subset = list(combinations(number, 3))
    
    for i in subset:
        data_sum = sum(i)
        result.append(data_sum)
        
    answer = result.count(0)
    
    return answer