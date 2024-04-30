def solution(numbers):
    n = max(numbers)
    numbers.remove(n)
    m = max(numbers)
    answer = n * m
    return answer