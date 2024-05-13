def solution(s):
    alpha = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9',
    }
    answer = ''
    ans = ''
    for i in s:
        if i in alpha.values():
            answer += i
        else:
            ans += i
            if ans in alpha.keys():
                answer += alpha[ans]
                ans = ''
    return int(answer)