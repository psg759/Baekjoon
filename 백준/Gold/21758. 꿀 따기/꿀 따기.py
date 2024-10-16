n = int(input())

bee = list(map(int, input().split()))

b_sum = [bee[0]] + [0] * (n-1)

ans = 0


#기준이 되는 누적합 초기화
for i in range(1, n):
    b_sum[i] = b_sum[i-1] + bee[i]


for i in range(1, n-1):
    #꿀 통이 오른쪽 끝, 벌이 왼쪽 끝 & 중간 어딘가 있는 경우
    right = 2 * b_sum[-1] - bee[i] -bee[0] -b_sum[i]

    #꿀 통이 왼쪽 끝, 벌이 오른쪽 끝 & 중간 어딘가 있는 경우
    left = b_sum[-1] - bee[-1] +b_sum[i-1] - bee[i]

    #꿀 통이 중간, 벌이 양쪽 끝에 있는 경우
    mid = b_sum[i] - bee[0] + b_sum[-1] - bee[-1] - b_sum[i-1]
    ans = max(ans, right, left, mid)

print(ans)


