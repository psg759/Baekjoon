def solution(str_list):
    answer = []
    if 'l' not in str_list and 'r' not in str_list:
        return []
    
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            answer.extend(str_list[:i])
            return answer
            
        elif str_list[i] == 'r':
            answer.extend(str_list[i+1:])
            return answer
        