board = input()
tmp = ''
cnt = 0

for i in range(len(board)):
    if board[i] == "X":
        cnt += 1
    elif board[i] == '.':
        if cnt % 2 == 1:
            print(-1)
            exit()
        else:
            if cnt == 2:
                tmp += 'BB'
            elif cnt == 4:
                tmp += 'AAAA'
            else:
                a = cnt % 4
                cnt = cnt // 4
                tmp += 'AAAA' * cnt + 'BB' * (a//2)
        tmp += '.'
        cnt = 0
    if i == (len(board) - 1):
        if cnt % 2 == 1:
            print(-1)
            exit()
        else:
            if cnt == 2:
                tmp += 'BB'
            elif cnt == 4:
                tmp += 'AAAA'
            else:
                a = cnt % 4
                cnt = cnt // 4
                tmp += 'AAAA' * cnt + 'BB' * (a//2)
print(tmp)