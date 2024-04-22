def solution(num_list, n):
    answer = []
    for i in range(n):
        answer.append(num_list[i])
    ans = num_list[n:] + answer
    return ans