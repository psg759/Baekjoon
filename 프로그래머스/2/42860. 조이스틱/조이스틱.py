def solution(name):
    #알파벳 이동값 초기화
    alpha_move = 0
    #커서 이동값 초기화 -> A가 한개도 존재하지 않을 것을 고려해 초기값 설정
    cursor_move = len(name) - 1
    
    #for문을 통해 어느 인덱스를 기준으로 방향 전환을 했을때 가장 min한 값이 나오는지 조회
    for i, spell in enumerate(name):
        #알파벳 이동 횟수
        alpha_move += min(ord(spell) - 65, 91 - ord(spell))
        
        #커서 이동 횟수
        next = i+1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 아래 3가지 경우 중 최소 이동 값으로 갱신 (i는 현재 위치 인덱스, next는 연속된 A의 마지막 인덱스)
        # 1. cursor_move = 돌아가지 않고 앞으로만 간 경우
        # 2. i*2 + (len(name) - next) = 앞으로 가다가 뒤로 다시 돌아가는 경우
        # 3. i+2 * (len(name) - next) = 뒤로 먼저 간 뒤 앞으로 다시 돌아오는 경우
        cursor_move = min([cursor_move, i * 2 + (len(name) - next), i + 2 * (len(name) - next) ])
        
    return alpha_move + cursor_move
        