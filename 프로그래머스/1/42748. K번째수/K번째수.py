def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        n, m, l = commands[i][0], commands[i][1], commands[i][2]
        answer.append(list(sorted(array[n-1:m]))[l-1])
    return answer