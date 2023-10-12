# 2606번 바이러스 - dfs 사용해서 품

n = int(input())
m = int(input())
count = 0

graph = []
for i in range(m):
    graph.append(list(map(int,input().split())))
    
data = [[] for _ in range(n+1)]

for i in graph:
    data[i[0]].append(i[1])
    data[i[1]].append(i[0])
    
for j in data:
    j.sort()
    
#print(data)
    
visited = [False] * (n+1)

def dfs(data, v, visited):
    visited[v] = True
    
    for i in data[v]:
        if not visited[i]:
            dfs(data,i,visited)
    

dfs(data,1,visited)

for i in visited:
    if i == True:
        count += 1
        
print(count-1)



        

    
    
        
    
    









