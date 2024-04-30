def solution(sides):
    b = max(sides)
    a = sum(sides)
    a = a - b
    
    if b < a:
        return 1
    else:
        return 2