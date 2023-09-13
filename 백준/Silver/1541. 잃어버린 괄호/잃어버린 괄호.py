data = input().split('-')
cnt = 0

#첫 숫자 처리
for i in data[0].split('+'):
    cnt += int(i)
    
#나머지 숫자 뺄셈 처리
for i in data[1:]:
    for j in i.split('+'):
        cnt -= int(j)

print(cnt)
