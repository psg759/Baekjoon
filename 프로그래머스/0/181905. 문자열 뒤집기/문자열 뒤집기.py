def solution(my_string, s, e):
    my_string = list(my_string)
    x = my_string[s:e+1]
    x = list(x)
    x.reverse()
    my_string[s:e+1] = x
    my_string = ''.join(my_string)
    return my_string