K, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(5)]

treasures = list(map(int, input().split()))


def rotate(sr, sc, board):
    nboard = [x[:] for x in board]
    for r in range(3):
        for c in range(3):
            nboard[sr + r][sc + c] = board[sr + 3 - c - 1][sc + r]
    return nboard


def in_range(r, c):
    return 0 <= r < 5 and 0 <= c < 5


ans = []
from collections import deque


def bfs(board, v, sr, sc, clr):
    q = deque()
    v[sr][sc] = 1
    q.append((sr, sc))

    collected = [(sr, sc)]
    target = board[sr][sc]
    while q:
        cr, cc = q.popleft()
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nr, nc = cr + dr, cc + dc
            if in_range(nr, nc) and v[nr][nc] == 0 and board[nr][nc] == target:
                collected.append((nr, nc))
                v[nr][nc] = 1
                q.append((nr, nc))
    if len(collected) >= 3:
        if clr == 1:
            for xr, xc in collected:
                board[xr][xc] = 0
        return len(collected)
    return len(collected)


def count_clear(board, clr):
    v = [[0] * 5 for _ in range(5)]
    cnt = 0
    for r in range(5):
        for c in range(5):
            if v[r][c] == 0:
                cnt += bfs(board, v, r, c, clr)
    return cnt


ans = []
for _ in range(K):
    max_cnt = 0
    # [1] 탐사 진행
    for rot in range(1, 4):
        for c in range(3):
            for r in range(3):
                nboard = [x[:] for x in board]
                for _ in range(rot):
                    nboard = rotate(r, c, nboard)
                t = count_clear(nboard, 0)

                if t > max_cnt:
                    max_cnt = t
                    best_board = nboard
    if max_cnt == 0:
        break
    cnt = 0
    board = best_board
    # [2] 유물 획득
    # 1차 획득
    while True:
        t = count_clear(board, 1)
        if t == 0:
            break
        cnt += t
        for c in range(5):
            for r in range(4, -1, -1):
                if board[r][c] == 0:
                    board[r][c] = treasures.pop(0)
    ans.append(cnt)

for a in ans:
    print(a, end=" ")

