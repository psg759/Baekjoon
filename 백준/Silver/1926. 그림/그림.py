from collections import deque
#1926번 그림

n,m = map(int, input().split())
data = []
data_2 = []

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
    
def bfs(x,y):
    res = 0
    queue = deque([])
    queue.append([x,y])
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            if data[nx][ny] == 0:
                continue
            if data[nx][ny] == 1:
                data[nx][ny] = 0
                res += 1
                queue.append([nx,ny])
    
    if res == 0:
        data_2.append(1)
    else:
        data_2.append(res)
  
check = sum(data,[])
if 1 not in check:
    print(0)
    print(0)
    exit()
        
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            bfs(i,j)
            
print(len(data_2))
print(max(data_2))