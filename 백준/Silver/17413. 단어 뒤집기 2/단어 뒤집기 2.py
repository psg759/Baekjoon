sen = input()

flag = 0
tmp, res = "", ""

for char in sen:
    # 기호 <일 경우 flag를 1로 설정하고 tmp에 값을 추가
    if char == "<":
        res += tmp[::-1]  # 이전까지 쌓인 tmp를 역순으로 추가
        tmp = "<"         # tmp를 초기화하고 <를 추가
        flag = 1          # 기호 안쪽으로 들어갔음을 표시
    elif char == ">":
        tmp += ">"        # > 기호를 추가
        res += tmp        # tmp를 그대로 res에 추가
        tmp = ""          # tmp 초기화
        flag = 0          # 기호 바깥으로 나왔음을 표시
    elif flag == 1:
        tmp += char       # 기호 안에서는 순서대로 tmp에 추가
    elif flag == 0:
        if char == " ":
            res += tmp[::-1] + " "  # 공백이 오면 tmp를 역순으로 추가하고 공백도 추가
            tmp = ""                # tmp 초기화
        else:
            tmp += char             # tmp에 역순으로 쌓일 문자들 추가

# 마지막 남은 tmp 처리 (공백이 없으면 tmp가 남아 있을 수 있음)
res += tmp[::-1]

print(res)
