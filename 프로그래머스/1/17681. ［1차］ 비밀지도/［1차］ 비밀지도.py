def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        num1 = ""
        num2 = ""
        while arr1[i] > 0:
            if arr1[i] == 1:
                num1 += '1'
                break
            num1 += str(arr1[i] % 2)
            arr1[i] //= 2
        if len(num1) < n:
            num1 += '0' * (n - len(num1))
        num1 = list(num1)
        num1.reverse()
        
        while arr2[i] > 0:
            if arr2[i] == 1:
                num2 += '1'
                break
            num2 += str(arr2[i] % 2)
            arr2[i] //= 2
        if len(num2) < n:
            num2 += '0' * (n - len(num2))
        num2 = list(num2)
        num2.reverse()
        
        ans = ''
        for i in range(n):
            if int(num1[i]) or int(num2[i]):
                ans += "#"
            else:
                ans += ' '
        answer.append(ans)
        
    return answer