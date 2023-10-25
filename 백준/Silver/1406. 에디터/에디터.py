#1406번 에디터
#배열을 두개 설정하고 꺼냈다 뺐다 스택의 개념
#연결리스트보다 스택으로 푸는게 더 효율적으로 보임
#reverse(st2에 값이 없다면 에러남) 말고 reversed를 써야함 

import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())
    elif command[0] == 'B':
        if st1:
            st1.pop()
    else:
        st1.append(command[1])

st1.extend(reversed(st2))
print(''.join(st1))