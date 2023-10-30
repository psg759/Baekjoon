#2753번 수 정렬하기 4

import sys

data = []
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    data.append(int(sys.stdin.readline().rstrip()))
    
data.sort(reverse=True)

for i in data:
    print(i)