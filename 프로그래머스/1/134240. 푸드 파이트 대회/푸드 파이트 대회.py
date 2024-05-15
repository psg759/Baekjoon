def solution(food):
    answer = ''
    for i in range(1,len(food)):
        if food[i] == 1:
            continue
        elif food[i] % 2 == 1:
            answer += str(i) * (food[i] // 2)
        elif food[i] % 2 == 0:
            answer += str(i) * (food[i] // 2)
    answer += '0' + answer[::-1]
    return answer