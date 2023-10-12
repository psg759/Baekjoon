from collections import deque
# 2644번 촌수 계산
# dfs로 풀 경우 내가 찾는 사람을 발견했다 하더라도, 나머지 펼쳐진 재귀들을 다 수습을 해야하는 문제때문에 bfs 로 풀어야할듯
# bfs로 해봤는데 이걸로 하면 3까지 최단거리로 가는게 아니라 가까운 애들을 거쳐서 먼저 가기때문에 dfs가 적합함 수정방안을 생각해보자 ..
# 정답을 보고 내 식대로 다시 bfs로 해결해보자,,

#전체 사람 수
n = int(input())
a,b = map(int, input().split())
m = int(input())

graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))
    
data = [ [] for _ in range(n+1)]

for i in graph:
    data[i[0]].append(i[1])
    data[i[1]].append(i[0])
    
for j in data:
    j.sort()
    
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 0
    
    while queue:
        v = queue.popleft()
        
        if v == b:
            return visited[b]
            
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v] + 1
                
    return -1
         
visited = [0] * (n+1)

print(bfs(data,a,visited))
