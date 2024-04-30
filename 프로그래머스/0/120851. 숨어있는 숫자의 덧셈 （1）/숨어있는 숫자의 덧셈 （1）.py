def solution(my_string):
    num = ['1','2','3','4','5','6','7','8','9']
    answer = 0
    for i in my_string:
        if i in num:
            answer += int(i)
    return answer