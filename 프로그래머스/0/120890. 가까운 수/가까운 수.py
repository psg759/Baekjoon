def solution(array, n):
    array.append(n)
    array.sort()
    print(array)
    for i in range(len(array)):
        if array[i] == n:
            if i == 0:
                return array[i+1]
            elif i == len(array)-1:
                return array[-2]
            else:
                a = abs(n - array[i-1])
                b = abs(n - array[i+1])
                if a < b:
                    return array[i-1]
                elif a == b:
                    return array[i-1]
                else:
                    return array[i+1]
    
    return num