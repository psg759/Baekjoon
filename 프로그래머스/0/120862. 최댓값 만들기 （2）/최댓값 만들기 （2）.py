def solution(numbers):
    numbers.sort()
    first = numbers[0]
    second = numbers[1]
    third = numbers[-1]
    fourth = numbers[-2]
    
    if first * second >= third * fourth:
        return first * second
    else:
        return third * fourth