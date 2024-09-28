#1912 백준 연속합

n = int(input())

tmp = list(map(int, input().split()))

plus = 0

dp = [0] * n
dp[0] = tmp[0]

for i in range(1, n):
    dp[i] = max(tmp[i], dp[i-1] + tmp[i])
    
print(max(dp))