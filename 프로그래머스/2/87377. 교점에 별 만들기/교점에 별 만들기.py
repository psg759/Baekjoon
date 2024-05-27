def solution(line):
    answer = []
    real_ans = []
    for i in range(len(line)):
        for j in range(len(line) - 1 - i):
            a1, b1, c1 = line[i][0], line[i][1], line[i][2]
            a2, b2, c2 = line[i+j+1][0], line[i+j+1][1], line[i+j+1][2]
            cross_dot = a1 * b2 - b1 * a2

            #평행 상태이므로 교점 x
            if cross_dot == 0:
                continue
            #교점이 존재
            else:
                x = ((b1 * c2) - (c1 * b2)) / cross_dot
                y = ((c1 * a2) - (a1 * c2)) / cross_dot
                #교점 x, y가 정수라면 answer에 추가
                if x == int(x) and y == int(y) and [int(x), int(y)] not in answer:
                    answer.append([int(x),int(y)])
    #교점이 한개라면
    if len(answer) == 1:
        return ["*"]
    

    # 교점이 한개가 아닐때의 사각형 너비 구하기
    answer = sorted(answer, key = lambda x : x[0])
    x_min, x_max = answer[0][0], answer[-1][0]
    width = x_max - x_min + 1
    
    # 교점이 한개가 아닐때의 사각형 높이 구하기 
    answer = sorted(answer, key = lambda x : x[1])
    y_min, y_max = answer[0][1], answer[-1][1]
    height = y_max - y_min + 1


   # 좌표를 (0, 0) 기준으로 이동
    normalized_points = [(x - x_min, y_max - y) for x, y in answer]

    # 사각형 그리기
    canvas = [['.' for _ in range(width)] for _ in range(height)]
    for x, y in normalized_points:
        canvas[y][x] = '*'

    real_ans = [''.join(row) for row in canvas]
    
    return real_ans