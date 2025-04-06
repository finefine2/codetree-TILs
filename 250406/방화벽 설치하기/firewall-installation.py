from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 빈 칸과 불 위치 찾기
blanks = []
fires = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            blanks.append((i, j))
        elif board[i][j] == 2:
            fires.append((i, j))

def in_range(r, c):
    return 0 <= r < N and 0 <= c < M

def spread_fire():
    temp_board = [row[:] for row in board]
    visited = [[False] * M for _ in range(N)]
    q = deque(fires)
    
    # 불 위치 방문 처리
    for r, c in fires:
        visited[r][c] = True
    
    while q:
        r, c = q.popleft()
        for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
            nr, nc = r + dr, c + dc
            if in_range(nr, nc) and not visited[nr][nc] and temp_board[nr][nc] == 0:
                temp_board[nr][nc] = 2
                visited[nr][nc] = True
                q.append((nr, nc))
    
    # 안전 영역 계산
    safe_count = 0
    for i in range(N):
        for j in range(M):
            if temp_board[i][j] == 0:
                safe_count += 1
                
    return safe_count

def solve():
    max_safe = 0
    blank_cnt = len(blanks)
    
    # 3개의 벽을 놓는 모든 조합 시도
    for i in range(blank_cnt):
        r1, c1 = blanks[i]
        board[r1][c1] = 1
        
        for j in range(i + 1, blank_cnt):
            r2, c2 = blanks[j]
            board[r2][c2] = 1
            
            for k in range(j + 1, blank_cnt):
                r3, c3 = blanks[k]
                board[r3][c3] = 1
                
                # 불이 퍼진 후 안전 영역 계산
                safe_area = spread_fire()
                max_safe = max(max_safe, safe_area)
                
                # 세 번째 벽 제거
                board[r3][c3] = 0
            
            # 두 번째 벽 제거
            board[r2][c2] = 0
        
        # 첫 번째 벽 제거
        board[r1][c1] = 0
    
    return max_safe

print(solve())