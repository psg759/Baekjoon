from collections import deque
#1697번 숨바꼭질

n,m = map(int, input().split())
cnt = 0
res = 0
visited = [0] * 1000000

def bfs(x,y):
    queue = deque([])
    queue.append([x,y])
    
    while queue:
      x,y = queue.popleft()
      
      for i in range(3):
        if i == 0:
            dx = x - 1
            if dx < 0 or dx > 100000:
                continue
            if visited[dx] == 0:
                visited[dx] = visited[x]+1
                if dx == y:
                    print(visited[y])
                    return
                else:
                    queue.append([dx,y])
        elif i == 1:
            dx = x + 1
            if dx < 0 or dx > 100000:
                continue
            if visited[dx] == 0:
                visited[dx] = visited[x]+1
                if dx == y:
                    print(visited[y])
                    return
                else:
                    queue.append([dx,y])
                
        elif i == 2:
            dx = x * 2
            if dx < 0 or dx > 100000:
                continue
            if visited[dx] == 0:
                visited[dx] = visited[x]+1
                if dx == y:
                    print(visited[y])  
                    return
                else:
                    queue.append([dx,y])
if n > m:
    print(n-m)
elif n == m:
    print(0)
else:                   
    bfs(n,m)
    
    
        