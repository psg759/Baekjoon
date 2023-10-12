# 2667번 단지번호 붙이기

n = int(input())
count = 2
result = []

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x,y):
    
    if x<0 or y<0 or x>n-1 or y > n-1:
        return False
    
    #count로 값을 바꿔주는 경우는 case가 1인경우 각 자리를 돌면서 계산한 자리를 또 계산하기 때문
    if graph[x][y] == 1:
        graph[x][y] = count
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
        
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            count += 1 

print(count-2)
res = sum(graph, [])

for k in range(2, count):
    result.append(res.count(k))

result.sort()

for i in result:
    print(i)

       
        






        

    
    
        
    
    









