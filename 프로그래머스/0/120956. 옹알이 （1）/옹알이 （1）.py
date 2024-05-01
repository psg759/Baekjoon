def solution(babbling):
    cnt = 0
    speak = [ "aya", "ye", "woo", "ma" ]
    for i in babbling:
        n = 0
        for j in speak:
            while j in i:
                n += 1
                i = i.replace(j, ".")
                print(i)
                
                if i == "."*n:
                    cnt += 1
                    print(cnt)
                
    return cnt