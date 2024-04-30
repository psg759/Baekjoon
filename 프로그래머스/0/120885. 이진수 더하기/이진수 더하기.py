def solution(bin1, bin2):
    answer = ''
    n = len(bin1)-1
    m = len(bin2)-1
    num = 0
    num2 = 0
    for i in bin1:
        if i == '1':
            num += 2 ** n
            n -= 1
        elif i == '0':
            n -= 1
    for j in bin2:
        if j == '1':
            num2 += 2 ** m
            m -= 1
        elif j == '0':
            m -= 1
    number = num + num2
    
    if number == 0:
        return "0"
    
    while True:
        answer = str(number % 2) + answer
        number //= 2
        
        if number == 1:
            answer = str(number) + answer
            break
    
    return answer