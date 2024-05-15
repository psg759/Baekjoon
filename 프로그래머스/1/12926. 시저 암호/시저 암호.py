def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
            continue
        elif ord(i) < 91 and 90 < (ord(i)+n):
            answer += chr((ord(i)+n) - 26)
            continue
        elif 96 < ord(i) and (ord(i)+n) > 122:
            answer += chr((ord(i)+n) - 26)
            continue
        else:
            answer += chr((ord(i)+n))
    return answer