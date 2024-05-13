def solution(array, commands):
    answer = []
    a = array.copy()
    for i in range(len(commands)):
        a = array.copy()
        n, m, l = commands[i][0], commands[i][1], commands[i][2]
        a = a[n-1:m]
        a.sort()
        answer.append(a[l-1])
    return answer