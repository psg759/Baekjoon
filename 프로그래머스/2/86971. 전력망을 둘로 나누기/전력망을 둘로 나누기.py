import copy
#그냥 copy 함수는 이차원 리스트에서는 먹히지 않아서 deepcopy를 사용해야함

def dfs(graph, now, visited, cnt):
    visited[now] = True
    cnt += 1
    for j in graph[now]:
        if not visited[j]:
            cnt = dfs(graph, j, visited, cnt)
    
    return cnt
    

def solution(n, wires):
    min_abs = 0
    res = []
    
    graph = [[] for _ in range(n+1)]
    for x,y in wires:
        graph[x].append(y)
        graph[y].append(x)
    
    for i in range(len(wires)):
        visited = [False] * (n+1)
        tmp = []
        graph_ex = copy.deepcopy(graph)
        graph_ex[wires[i][0]].remove(wires[i][1])
        graph_ex[wires[i][1]].remove(wires[i][0])
        
        for i in range(1, n+1):
            if visited[i] == False:
                top_cnt = dfs(graph_ex, i, visited, 0)
                tmp.append(top_cnt)
        res.append(abs(tmp[0] - tmp[1]))
        
        
    return min(res)
                
        
                
                
            
