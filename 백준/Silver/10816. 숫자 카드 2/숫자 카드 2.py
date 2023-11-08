#10816번 숫자 카드 2

n = int(input())

data = list(map(int, input().split()))

data.sort()

m = int(input())

data_2 = list(map(int, input().split()))

data_dict = {}

for i in data:
    if i not in data_dict:
        data_dict[i] = 1
    elif i in data_dict:
        data_dict[i] += 1

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return array[mid]
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for j in data_2:
    result = binary_search(data, j, 0, n-1)
    if result != None:
        print(data_dict[result], end=' ')
    else:
        print(0, end=' ')   