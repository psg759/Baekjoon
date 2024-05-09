def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(len(arr)):
        if arr[i] in answer and answer[len(answer)-1] != arr[i]:
            answer.append(arr[i])
        elif arr[i] not in answer:
            answer.append(arr[i])
    return answer