def solution(s):
    ans = []
    answer = []
    for i in s:
        if i.isupper():
            ans.append(i)
        else:
            answer.append(i)
    ans.sort(reverse=True)
    answer.sort(reverse=True)
    ans = ''.join(ans)
    answer = ''.join(answer)
    return answer + ans