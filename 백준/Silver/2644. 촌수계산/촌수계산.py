from collections import deque

n = int(input())
a,b = map(int, input().split())
m = int(input())

graph = []

for _ in range(m):
    graph.append(list(map(int, input().split())))

data = [[] for _ in range(n+1)]

for i in graph:
    data[i[0]].append(i[1])
    data[i[1]].append(i[0])
    
for j in data:
    j.sort()

visited = [0] * (n+1)

def bfs(a,b):
    queue = deque([a])
    visited[a] = 0
    
    while queue:
        v = queue.popleft()
        
        if v == b:
            return visited[b]
        
        for k in data[v]:
            if visited[k] == 0:
                queue.append(k)
                visited[k] = visited[v] + 1
    
    return -1

print(bfs(a,b))