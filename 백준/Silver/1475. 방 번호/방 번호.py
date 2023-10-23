#1475번 방 번호
#11223같은 경우 1이 두번 중복돼서 이미 2세트가 확보돼서 2가 두개여도 세트를 +1할 필요가 없다는 예외 발견
#현재 세트 갯수를 추적해서 리스트의 값이 세트 갯수와 같으면 세트 값을 +1 갱신, 아니면 인덱스 값 +1 해주는 방식으로 변경

n = input()
set = 1
max = 1
data = [0] * 10

for i in n:
    #6과 9일때는 허용 범위 2
    if int(i) == 6 or int(i) == 9:
        if data[6] != max:
            data[6] += 1/2
        elif data[6] == max:
            max += 1
            data[6] += 1/2
            
    #나머지 숫자는 허용 1      
    else:    
        if data[int(i)] != max:
            data[int(i)] += 1
        elif data[int(i)] == max:
            max += 1
            data[int(i)] += 1

print(max)