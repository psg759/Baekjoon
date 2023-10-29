#2751번 수 정렬하기 2
import sys

data = []
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    data.append(int(sys.stdin.readline().rstrip()))
    
data.sort()

for i in data:
    print(i)