def solution(str_list, ex):
    answer = []
    for i in str_list:
        if ex in i:
            continue
        else:
            answer.append(i)
    answer = ''.join(answer)
    return answer