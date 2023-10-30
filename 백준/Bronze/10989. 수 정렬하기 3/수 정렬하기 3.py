#2753번 수 정렬하기 3 (256mb -> 8mb)
#계수정렬로 풀었는데 메모리 초과남 -> 리스트 입력받은걸 토대로 0인 리스트를 증가시키지 말고, 입력받자마자 0인 리스트에 바로 +1로 수정
#일반 sort로 풀었는데도 메모리 초과남

import sys

data = [0] * 10001
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    m = int(sys.stdin.readline().rstrip())
    data[m] += 1
    

for i in  range (len(data)):
    for j in range(data[i]):
        print(i)