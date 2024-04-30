def solution(numbers, k):
    answer = 0
    n = 0
    for _ in range(k):
        answer = numbers[n]
        n += 2
        print(answer)
        if n >= len(numbers):
            n = n - len(numbers)
    return answer