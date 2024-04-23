def solution(arr):
    x = 0
    y = arr.copy()
    while True:
        x += 1
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] /= 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] *= 2
                arr[i] += 1
        
        if y == arr:
            return x - 1
        else:
            y = arr.copy()