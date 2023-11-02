#15688번 수 정렬하기 5

import sys

data = []
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    
    data.append(int(sys.stdin.readline()))
for i in sorted(data):
    print(i)