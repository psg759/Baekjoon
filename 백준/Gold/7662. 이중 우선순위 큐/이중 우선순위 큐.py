import sys, heapq
t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    min_heap, max_heap = [], []
    visit = [False]*k
    
    for idx in range(k):
        cmd = sys.stdin.readline().split()
        
        if cmd[0] == 'I': 
            heapq.heappush(min_heap, (int(cmd[1]), idx))
            heapq.heappush(max_heap, (-int(cmd[1]), idx))
            visit[idx] = True
            
        elif cmd[0] == 'D': 
            if cmd[1] == '-1': 
                while min_heap and not visit[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visit[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif cmd[1] == '1':
                while max_heap and not visit[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)
        
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')