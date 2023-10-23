#13300번 방 배정
#여학생은 성별 0 남학생은 성별 1

#참가 학생수, 한 방에 배정할 수 있는 최대 인원 수
n,k = map(int, input().split())
data = [0] * 12
room = 0

for _ in range(n):
    #성별, 학년
    a,b = map(int, input().split())
    
    if a == 0:
        data[2*b-2] += 1
    elif a == 1:
        data[2*b-1] += 1
        
for i in data:
    if i == 0:
        continue
    elif i <= k:
        room += 1
    else:
        room += i//k +1 
        
print(room)