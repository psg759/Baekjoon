def solution(board):
    cnt = 0
    tmp = []
    n = len(board)
    if n == 1:
        if board[0][0] == 0:
            return 1
        else:
            return 0
        
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                tmp.append([i,j])
    for k in tmp:
        i = k[0]
        j = k[1]
        if i - 1 <0 and j - 1 < 0:
            board[i+1][j] = 1
            board[i][j+1] = 1
            board[i+1][j+1] = 1
        elif i + 1 == len(board) and j + 1 == len(board):
            board[i-1][j] = 1
            board[i][j-1] = 1
            board[i-1][j-1] = 1
        elif i + 1 == len(board) and j - 1 < 0:
            board[i-1][j] = 1
            board[i][j+1] = 1
            board[i-1][j+1] = 1
        elif i - 1 < 0 and j + 1 == len(board):
            board[i+1][j] = 1
            board[i][j-1] = 1
            board[i+1][j-1] = 1
        elif j - 1 < 0:
            board[i-1][j] = 1
            board[i+1][j] = 1
            board[i-1][j+1] = 1
            board[i][j+1] = 1
            board[i+1][j+1] = 1
        elif i - 1 < 0:
            board[i][j-1] = 1
            board[i][j+1] = 1
            board[i+1][j-1] = 1
            board[i+1][j] = 1
            board[i+1][j+1] = 1
        elif j + 1 == len(board):
            board[i-1][j] = 1
            board[i+1][j] = 1
            board[i-1][j-1] = 1
            board[i][j-1] = 1
            board[i+1][j-1] = 1
        elif i + 1 == len(board):
            board[i][j-1] = 1
            board[i][j+1] = 1
            board[i-1][j-1] = 1
            board[i-1][j] = 1
            board[i-1][j+1] = 1
        else:
            board[i-1][j-1] = 1
            board[i-1][j] = 1
            board[i-1][j+1] = 1
            board[i][j-1] = 1
            board[i][j+1] = 1
            board[i+1][j-1] = 1 
            board[i+1][j] = 1
            board[i+1][j+1] = 1
    
    for i in board:
        cnt += i.count(0)
        print(cnt)
        
    return cnt
                    
                    
                    
            
            
    