#5397번 키로거

import sys
for _ in range(int(sys.stdin.readline())):
    st1 = []
    st2 = []
    command = list(sys.stdin.readline().rstrip())
    for i in command:
        if i == "<":
            if not st1:
                continue
            elif st1:
                st2.append(st1.pop())
        elif i == ">":
            if not st2:
                continue
            elif st2:
                st1.append(st2.pop())
        elif i == '-':
            if st1:
                st1.pop()
        else:
            st1.append(i)
            
    st1.extend(reversed(st2))
    print("".join(st1))