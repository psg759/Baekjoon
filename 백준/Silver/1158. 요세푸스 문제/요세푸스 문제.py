#1158번 요세푸스 문제
#원형 문제는 큐로 해결할 수 있음

from collections import deque

n, k = map(int, input().split())

queue = deque(list(range(1,n+1)))

print('<', end='')

for i in range(n-1):
    for j in range(k-1):
        queue.append(queue.popleft())
    print(queue[0], end=", ")
    queue.popleft()
    
print(str(queue[0]) + '>')