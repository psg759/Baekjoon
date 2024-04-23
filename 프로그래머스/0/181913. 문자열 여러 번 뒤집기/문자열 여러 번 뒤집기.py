def solution(my_string, queries):
    my_string = list(my_string)
    for i in range(len(queries)):
        x = my_string[queries[i][0]:queries[i][1]+1]
        x.reverse()
        my_string[queries[i][0]:queries[i][1]+1] = x
    my_string = ''.join(my_string)
    return my_string