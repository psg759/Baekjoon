def solution(array):
    array2 = set(array)
    array2 = list(array2)
    tmp = []

    for i in array2:
        tmp.append(array.count(i))
        
    print(tmp)
    big = max(tmp)
    idx = tmp.index(max(tmp))
    if tmp.count(big) == 1:
        return array2[idx]
    elif tmp.count(big) >=2:
        return -1