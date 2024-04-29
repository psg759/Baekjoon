def solution(n):
    answer = [[0]* n for _ in range(n)]
    answer[0][0] = 1
    x = 0
    y = 0
    cnt = 2
    m = n
    flag = 2

    while True:
        if cnt == n**2 + 1:
            break

        if flag == 0:
            for j in range(m-1):
                y+=1
                answer[x][y] = cnt
                cnt += 1
            for j in range(m-2):
                x+=1
                answer[x][y] = cnt
                cnt += 1

            m -= 1
            flag = 1

        elif flag == 1:
            for j in range(m-1):
                y -= 1
                answer[x][y] = cnt
                cnt += 1
            for j in range(m-2):
                x -= 1
                answer[x][y] = cnt
                cnt += 1

            m -= 1
            flag = 0
        elif flag == 2:
            for j in range(m-1):
                y+=1
                answer[x][y] = cnt
                cnt += 1
            for j in range(m-1):
                x+=1
                answer[x][y] = cnt
                cnt += 1

            flag = 1
    return answer