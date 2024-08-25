from collections import deque

N,M = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

def initialize_visit():
    for r in range(N):
        for c in range(M):
            visited[r][c] = 0

def calc_ice():
    ans = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                ans += 1
    return ans

ans = []
def in_range(r,c):
    return 0<=r<N and 0<=c<M
q = deque()
water_pos = deque()
def bfs_water():
    drs,dcs = [1,0,-1,0],[0,1,0,-1]
    while q:
        r,c = q.popleft()
        for dr,dc in zip(drs,dcs):
            nr,nc = r + dr, c + dc
            if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] == 0:
                q.append((nr,nc))
                visited[nr][nc] = 1
                water_pos.append((nr,nc))
def bfs_melt():
    drs,dcs = [1,0,-1,0],[0,1,0,-1]
    while water_pos:
        wr,wc = water_pos.popleft()
        for dr,dc in zip(drs,dcs):
            nr,nc = wr + dr, wc + dc
            if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] == 1:
                board[nr][nc] = 0

while True:
    cnt = calc_ice()
    ans.append(cnt)

    initialize_visit()
    q.append((0,0))
    visited[0][0] = 1
    bfs_water()
    bfs_melt()
    if cnt == 0:
        break

print(len(ans)-1, ans[-2])