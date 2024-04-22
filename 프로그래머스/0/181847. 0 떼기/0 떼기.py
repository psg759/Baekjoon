def solution(n_str):
    answer = []
    if n_str.startswith('0'):
        for i in range(len(n_str)):
            if n_str[i] != '0':
                j = i
                break
        return n_str[j:]
    else:
        return n_str
            