import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))

stack = []
ans = [0] * N

for i in range(N):
    #스택이 차 있다면
    while stack:
        #수신 가능한 송신탑이 앞에 있다 -> 그 송신탑의 위치로 ans 갱신
        if stack[-1][1] > towers[i]:
            ans[i] = stack[-1][0] + 1
            break
        # 9 8 8 7 6 8 9 10
        else:
            stack.pop()
    #(인덱스, 타워값)
    stack.append((i, towers[i]))
print(*ans)