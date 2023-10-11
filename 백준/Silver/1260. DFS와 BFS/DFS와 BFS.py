from collections import deque
# 1260번 DFS와 BFS

n,m,v = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int,input().split())))
    
data = [[] for _ in range(n+1)]

for i in graph:
    data[i[0]].append(i[1])
    data[i[1]].append(i[0])
    
for j in data:
    j.sort()
       
def dfs(data, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in data[v]:
        if not visited[i]:
            dfs(data, i, visited)
            
def bfs(data,start,visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        p = queue.popleft()
        print(p, end = ' ')
        
        for i in data[p]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
visited_d = [False] * (n+1)    
visited_b = [False] * (n+1)

dfs(data,v, visited_d)
print()
bfs(data,v,visited_b)


        

    
    
        
    
    









