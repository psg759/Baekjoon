#3273번 두 수의 합

n = int(input())
data = list(map(int, input().split()))
x = int(input())

data.sort()
left, right = 0, n-1
cnt = 0

while left < right:
    tmp = data[left]+data[right]
    if tmp == x:
        cnt += 1
    if tmp < x:
        left += 1
        continue
    right -= 1
    
print(cnt)
