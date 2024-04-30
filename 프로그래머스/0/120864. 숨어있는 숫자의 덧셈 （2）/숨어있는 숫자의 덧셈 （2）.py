def solution(my_string):
    num = ['1','2','3','4','5','6','7','8','9','0']
    ans = ''
    answer = 0
    for i in range(len(my_string)):
        if my_string[i] in num:
            ans += my_string[i]
            if i == len(my_string)-1 or my_string[i+1] not in num:
                answer += int(ans)
                ans = ''
                
    if ans != '':
        return int(ans)
    
    return answer