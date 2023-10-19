#7562 나이트의 이동
from collections import deque

n = int(input())
data = []


dx = [-2,-2,2,2,-1,1,-1,1]
dy = [-1,1,-1,1,-2,-2,2,2]

for _ in range(n):
    data.append(int(input()))
    data.append(list(map(int, input().split())))
    data.append(list(map(int, input().split())))

def bfs(num,x,y):
    global q,r
    queue = deque()
    queue.append([x,y])
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx > num-1 or ny > num-1:
                continue
            if chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y] + 1
                queue.append([nx,ny])
    
    return chess[q][r]
        
    
    
for i in range(n):
    chess = [[0 for _ in range(data[3*i])] for _ in range(data[3*i])]
    x = data[1+3*i][0]
    y = data[1+3*i][1]
    q = data[2+3*i][0]
    r = data[2+3*i][1]
    if x == q and y == r:
        print(0)
        continue
    print(bfs(data[3*i],x,y))
    
