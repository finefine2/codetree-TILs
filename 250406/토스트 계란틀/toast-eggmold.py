from collections import deque

def solution(N, L, R, board):
    def can_move(val1, val2):
        diff = abs(val1 - val2)
        return L <= diff <= R
    
    def bfs(sr, sc, visited, day_changed):
        q = deque([(sr, sc)])
        visited[sr][sc] = day_changed
        total = board[sr][sc]
        count = 1
        positions = [(sr, sc)]
        
        while q:
            r, c = q.popleft()
            cur_val = board[r][c]
            
            # 4방향 탐색을 미리 정의
            for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                if (0 <= nr < N and 0 <= nc < N and 
                    visited[nr][nc] != day_changed and
                    can_move(cur_val, board[nr][nc])):
                    visited[nr][nc] = day_changed
                    q.append((nr, nc))
                    total += board[nr][nc]
                    count += 1
                    positions.append((nr, nc))
        
        # 인구 이동이 있는 경우만 처리
        if count > 1:
            avg = total // count
            for r, c in positions:
                board[r][c] = avg
            return True
        return False

    visited = [[0] * N for _ in range(N)]
    days = 0
    
    while True:
        day_changed = days + 1
        moved = False
        
        # 최적화된 좌표 순회
        for r in range(N):
            for c in range(N):
                if visited[r][c] != day_changed:
                    if bfs(r, c, visited, day_changed):
                        moved = True
        
        if not moved:
            return days
        days += 1

# 입력 처리
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, L, R, board))