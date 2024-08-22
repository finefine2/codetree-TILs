import sys
sys.setrecursionlimit(2500)
from collections import deque
N,K = tuple(map(int,input().split()))

board = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

start_points = []
for _ in range(K):
    r,c = tuple(map(int,input().split()))
    start_points.append((r-1,c-1))
q = deque()
# 움직일 수 있는 조건?
# 맵 안에 있고 + not visited 여야 하는데
# 또한 start_points에 안 속하게
# visited 를 갱신할 필요는 없다
def in_range(r,c):
    return 0<=r<N and 0<=c<N

num = 0
def bfs():
    global num
    drs,dcs = [0,1,0,-1],[1,0,-1,0]
    while q:
        r,c = q.popleft()
        for dr,dc in zip(drs,dcs):
            nr,nc = r+dr, c+dc
            if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] == 0:
                visited[nr][nc] = 1
                num += 1
                q.append((nr,nc))
for sr,sc in start_points:
    num += 1
    visited[sr][sc] = 1
    q.append((sr,sc))
    bfs()

cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 1:
            cnt += 1
print(cnt)