def solution(arr, queries):
    for i in range(len(queries)):
        for j in range(len(arr)):
            if queries[i][0]<= j <= queries[i][1]:
                arr[j] += 1
            
    return arr