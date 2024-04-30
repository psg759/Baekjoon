def solution(keyinput, board):
    x = board[0] // 2
    y = board[1] // 2
    n = x
    m = y
    
    for i in keyinput:
        if i == "left":
            if x == 0:
                continue
            else:
                x -= 1
        elif i == "right":
            if x == board[0] - 1:
                continue
            else:
                x += 1 
        elif i == "up":
            if y == board[1]-1:
                continue
            else:
                y += 1
        elif i == "down":
            if y == 0:
                continue
            else:
                y -= 1
    answer = []
    answer.append(x - n)
    answer.append(y - m)
    return answer