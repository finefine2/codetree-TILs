def rotate(board, start_r, start_c): 
    new_board = [x[:] for x in board]
    for r in range(3):
        for c in range(3):
            new_board[start_r+r][start_c+c] = board[start_r+3-c-1][start_c+r] 
    return new_board

def bfs(board, visited, start_r, start_c, clear_mode):
    from collections import deque
    
    # 시작 위치의 값이 0이면 즉시 반환
    if board[start_r][start_c] == 0:
        return 0
        
    q = deque([(start_r, start_c)])
    connected = {(start_r, start_c)}
    visited[start_r][start_c] = 1
    target = board[start_r][start_c]
    
    while q:
        curr_r, curr_c = q.popleft()
        for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
            next_r, next_c = curr_r + dr, curr_c + dc
            if (0 <= next_r < 5 and 0 <= next_c < 5 and 
                visited[next_r][next_c] == 0 and 
                board[next_r][next_c] == target):
                q.append((next_r, next_c))
                connected.add((next_r, next_c))
                visited[next_r][next_c] = 1

    if len(connected) >= 3:
        if clear_mode:
            for r, c in connected:
                board[r][c] = 0
        return len(connected)
    return 0

def count_clear(board, clear_mode): 
    visited = [[0] * 5 for _ in range(5)]
    total_count = 0
    
    for r in range(5):
        for c in range(5):
            if visited[r][c] == 0:
                count = bfs(board, visited, r, c, clear_mode) 
                total_count += count
                
    return total_count

def solve():
    # 입력 받기
    K, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(5)]
    treasures = list(map(int, input().split()))
    results = []

    # K번의 턴 진행
    for _ in range(K):
        # [1] 최적의 회전 찾기
        max_count = 0
        best_board = None
        
        for rotation in range(1, 4):  # 회전 횟수
            for start_c in range(3):  # 시작 열
                for start_r in range(3):  # 시작 행
                    temp_board = [x[:] for x in board]
                    for _ in range(rotation):
                        temp_board = rotate(temp_board, start_r, start_c)
                    
                    # 현재 상태에서 얻을 수 있는 점수 계산
                    count = count_clear(temp_board, 0)
                    if max_count < count:
                        max_count = count
                        best_board = [x[:] for x in temp_board]
        
        # 더 이상 제거할 수 있는 블록이 없으면 종료
        if max_count == 0:
            break

        # [2] 연쇄 제거 진행
        board = best_board
        chain_count = 0
        
        while True:
            count = count_clear(board, 1)  # 블록 제거
            if count == 0:
                break
            chain_count += count

            # 빈 공간 채우기
            for c in range(5):
                for r in range(4, -1, -1):
                    if board[r][c] == 0:
                        board[r][c] = treasures.pop(0)
        
        results.append(chain_count)
    
    # 결과 출력
    print(*results)

# 메인 실행
solve()