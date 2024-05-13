def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            break
        for j in range(i+1, len(numbers)):
            if (numbers[i]+numbers[j]) not in answer:
                answer.append(numbers[i]+numbers[j])
    return sorted(answer)