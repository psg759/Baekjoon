import heapq

line = []
n = int(input())

for _ in range(n):
    line.append(list(map(int, input().split())))

line.sort()

room = []
heapq.heappush(room, line[0][1])

for i in range(1, n):
    #시작시간이 종료지점보다 이전이다 그럼 그냥 새 방을 파기
    if line[i][0] < room[0]:
        heapq.heappush(room, line[i][1])
    else:
        #시작시간이 종료지점 이후이면 방을 갱신
        #heappop의 경우 가장 작은 원소가 출력됨
        heapq.heappop(room)
        heapq.heappush(room, line[i][1])

print(len(room))


