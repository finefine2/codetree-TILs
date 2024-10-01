from collections import deque

N, M = tuple(map(int, input().split()))
board = [[-1] * (N + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (N + 2)]
EMPTY = M + 1
ans = 0

def bfs():
    v = [[0] * (N + 2) for _ in range(N + 2)]
    mx_group = set()
    mx_rcnt = float('inf')  # 빨간색 폭탄 수를 최소화하기 위해 초기값을 무한대로 설정
    drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    for sr in range(N + 1, 0, -1):
        for sc in range(1, N + 1):
            if v[sr][sc] == 0 and 0 < board[sr][sc] <= M:
                q = deque()
                group = set()
                r_cnt = 0
                color_count = {}
                
                q.append((sr, sc))
                group.add((sr, sc))
                v[sr][sc] = 1
                color = board[sr][sc]
                color_count[color] = color_count.get(color, 0) + 1

                while q:
                    cr, cc = q.popleft()
                    for dr, dc in zip(drs, dcs):
                        nr, nc = cr + dr, cc + dc
                        if v[nr][nc] == 0 and (nr, nc) not in group and (board[nr][nc] == color or board[nr][nc] == 0):
                            q.append((nr, nc))
                            group.add((nr, nc))
                            v[nr][nc] = 1
                            if board[nr][nc] == 0:
                                r_cnt += 1
                            else:
                                color_count[board[nr][nc]] = color_count.get(board[nr][nc], 0) + 1

                # 폭탄 묶음 조건 확인
                if len(group) >= 2:
                    if (len(color_count) == 1 and color not in color_count) or (len(color_count) > 2):
                        continue  # 빨간색 폭탄만 있거나 2개 이상의 색깔이 있는 경우 제외

                    # 폭탄 묶음 선택 우선순위
                    if len(mx_group) < len(group) or (len(mx_group) == len(group) and mx_rcnt > r_cnt):
                        mx_group, mx_rcnt = group, r_cnt
                    elif len(mx_group) == len(group) and mx_rcnt == r_cnt:
                        # 기준점 선택
                        max_row = max((r for r, c in group if board[r][c] != 0), default=-1)
                        min_col = min((c for r, c in group if board[r][c] != 0 and r == max_row), default=float('inf'))
                        if max_row > -1 and (max_row, min_col) < (max((r for r, c in mx_group if board[r][c] != 0), default=-1), min((c for r, c in mx_group if board[r][c] != 0 and r == max((r for r, c in mx_group if board[r][c] != 0), default=-1)), default=float('inf')))):
                            mx_group = group

    return mx_group

def gravity():
    for sc in range(1, N + 1):
        cr = N
        for sr in range(N, 0, -1):
            if board[sr][sc] != EMPTY:
                if sr != cr:
                    board[cr][sc] = board[sr][sc]
                    board[sr][sc] = EMPTY
                cr -= 1

def counter_rotate(arr):
    narr = [x[:] for x in arr]
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            narr[r][c] = arr[c][len(arr) - r - 1]
    return narr

while True:
    bomb_group = bfs()
    if len(bomb_group) == 0:
        break
    ans += len(bomb_group) ** 2
    for br, bc in bomb_group:
        board[br][bc] = EMPTY
    gravity()
    board = counter_rotate(board)
    gravity()

print(ans)