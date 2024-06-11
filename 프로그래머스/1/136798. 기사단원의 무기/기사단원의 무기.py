def solution(number, limit, power):
    answer = []
    
    for i in range(1,number+1):
        num = 0
        for j in range(1, int(i**(1/2)) + 1):
            if (i % j == 0):
                num += 1
                if ((j ** 2) != i):
                    num += 1
        answer.append(num)
        
    answer = list(map(lambda x : power if x > limit else x, answer))
    return sum(answer)                