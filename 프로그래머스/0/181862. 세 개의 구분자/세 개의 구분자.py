def solution(myStr):
    myStr = list(myStr)
    for i in range(len(myStr)):
        if myStr[i] == 'a' or myStr[i] == 'b':
            myStr[i] = 'c'
    myStr = ''.join(myStr)
    myStr = myStr.split('c')
    answer = list(filter(None, myStr))
    if answer == []:
        return ["EMPTY"]
    return answer