n = int(input())
#처음에 입력받은 빈 리스트
name = []
#결과를 저장할 리스트
res = []

# 예를 들어 aaa aab abb abc
for _ in range(n):
    name.append(input())

#글자 수가 다 같기 때문에 글자 수 길이만큼 반복문을 돌음.
for i in range(len(name[0])):
    #첫 글자의 i번째 고정 (aaa의 0번째 -> a ,aaa의 1번째 -> a ,aaa의 2번째 -> a)
    tmp = name[0][i]
    #단어 수
    for j in range(n):
        #j단어의 i번째 글자가 tmp(name[0][i])과 같다면 그대로 넘어가기
        if tmp == name[j][i]:
            continue
        #다르다면 tmp 에 ?저장해주기
        else:
            tmp = '?'
            break
    #반복문을 다 돌아서 j 개의 단어들을 비교해봤을 때 j 개 다 tmp 와 같다면 그대로 append, 다르다면 tmp에 ?가 저장된 상태로 append
    res.append(tmp)
#리스트 res를 문자열로 변경해주기 위해 join 함수 사용 
res = ''.join(res)
print(res)
    
            
        
        
        
    
        
    
        
    