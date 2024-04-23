def solution(rank, attendance):
    new = []
    new2 = []
    for i in range(len(attendance)):
        if attendance[i]:
            new.append([rank[i], i])
    new.sort()
    a = new[0][1]
    b = new[1][1]
    c = new[2][1]
    
    return a * 10000 + b * 100 + c
    
    