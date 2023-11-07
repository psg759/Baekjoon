#1920번 수 찾기

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
data = list(map(int, input().split()))

data.sort()

m = int(input())
data_2 = list(map(int, input().split()))

for i in data_2:
    result = binary_search(data, i, 0, n-1)
    if result != None:
        print(1)
    else:
        print(0)