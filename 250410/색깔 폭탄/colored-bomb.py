N,M = map(int,input().split())

EMPTY = M+1
RED = 0
board = [[-1] * (N+2)] + [[-1] + list(map(int,input().split())) + [-1] for _ in range(N)] + [[-1] * (N+2)]

from collections import deque
def bfs(sr,sc):
    q = deque()
    group = set()

    q.append((sr,sc))
    group.add((sr,sc))
    v[sr][sc] = 1
    color = board[sr][sc]

    r_cnt = 0
    tlst = []

    while q:
        cr,cc = q.popleft()
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr,nc = cr + dr, cc + dc
            if v[nr][nc] == 0 and (nr,nc) not in group and (board[nr][nc] == color or board[nr][nc] == RED):
                q.append((nr,nc))
                group.add((nr,nc))
                if board[nr][nc] == 0:
                    r_cnt += 1
                else:
                    v[nr][nc] = 1
    base_r,base_c = get_base(group)
    tlst.append((len(group),r_cnt,base_r,base_c,group))
    if len(tlst) > 0:
        tlst.sort(key=lambda x: (-x[0],x[1],-x[2],x[3]))
        bomb_group = tlst[0][-1]

    return bomb_group

def gravity():
    global board
    for c in range(1,N+1):
        for r in range(1,N):
            while 0<=board[r][c]<=M and board[r+1][c] == EMPTY:
                board[r][c],board[r+1][c] = board[r+1][c],board[r][c]
                r -= 1
def get_base(group):
    max_r, min_c = -1, N+1
    for gr,gc in group:
        if board[gr][gc] != RED:
            if gr > max_r or (gr == max_r and min_c > gc):
                max_r,min_c = gr,gc
    return max_r, min_c
ans = 0

while True:
    v = [[0] * (N+2) for _ in range(N+2)]
    bomb_group = set()
    for sr in range(1,N+1):
        for sc in range(1,N+1):
            if v[sr][sc] == 0 and 0<board[sr][sc]<=M:
                bomb_group = bfs(sr,sc)

    if len(bomb_group) < 2:
        break

    ans += len(bomb_group) ** 2
    for br,bc in bomb_group:
        board[br][bc] =EMPTY
    gravity()
    board = list(map(list,zip(*board)))[::-1]
    gravity()

print(ans)

