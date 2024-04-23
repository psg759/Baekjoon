def solution(code):
    mode = 0
    ret = []
    for i in range(len(code)):
        if code[i] == '1':
            if mode == 0:
                mode = 1
            elif mode == 1:
                mode = 0
            continue
        
        if mode == 0:
            if i % 2 == 0:
                ret.append(code[i])
            
        elif mode == 1:
            if i % 2 == 1:
                ret.append(code[i])
           
    answer = ''.join(ret)
    
    if answer == '':
        return "EMPTY"
    
    return answer