def solution(line):
    answer = []

    # 교점 계산
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a1, b1, c1 = line[i]
            a2, b2, c2 = line[j]
            cross_dot = a1 * b2 - b1 * a2

            # 평행 상태이므로 교점 없음
            if cross_dot == 0:
                continue

            # 교점이 존재
            x = ((b1 * c2) - (c1 * b2)) / cross_dot
            y = ((c1 * a2) - (a1 * c2)) / cross_dot

            # 교점 x, y가 정수라면 answer에 추가
            if x == int(x) and y == int(y):
                point = [int(x), int(y)]
                if point not in answer:
                    answer.append(point)

    if not answer:
        return ["*"]

    # 교점의 x, y 좌표 최솟값과 최댓값을 구하기
    x_min = min(x for x, y in answer)
    x_max = max(x for x, y in answer)
    y_min = min(y for x, y in answer)
    y_max = max(y for x, y in answer)

    width = x_max - x_min + 1
    height = y_max - y_min + 1

    # 좌표를 (0, 0) 기준으로 이동
    normalized_points = [(x - x_min, y_max - y) for x, y in answer]

    # 사각형 그리기
    canvas = [['.' for _ in range(width)] for _ in range(height)]
    for x, y in normalized_points:
        canvas[y][x] = '*'

    real_ans = [''.join(row) for row in canvas]
    
    return real_ans

