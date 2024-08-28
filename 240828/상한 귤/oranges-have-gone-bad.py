from collections import deque

N,K = tuple(map(int,input().split()))
board = []
rotten_oranges = []
healthy_oranges = []
ans = [[0] * N for _ in range(N)]
for i in range(N):
    board.append(list(map(int,input().split())))
    for j in range(N):
        if board[i][j] == 0:
            ans[i][j] = -1
        elif board[i][j] == 1:
            healthy_oranges.append((i,j))
        elif board[i][j] == 2:
            rotten_oranges.append((i, j))
            ans[i][j] = 0

visited = [[0] * N for _ in range(N)]
steps = [[0] * N for _ in range(N)]

def in_range(r,c):
    return 0<=r<N and 0<=c<N

def push(nr,nc,new_step):
    q.append((nr,nc))
    visited[nr][nc] = 1
    steps[nr][nc] = new_step

def bfs():
    drs,dcs = [1,0,-1,0],[0,1,0,-1]
    while q:
        r,c = q.popleft()
        for dr,dc in zip(drs,dcs):
            nr,nc = r + dr, c + dc
            if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] != 0:
                push(nr,nc,steps[r][c]+1)

q=deque()
for rr,rc in rotten_oranges:
    push(rr,rc,0)
bfs()

for r in range(N):
    for c in range(N):
        if (r,c) in healthy_oranges:
            if steps[r][c] == 0:
                ans[r][c] = -2
            else:
                ans[r][c] = steps[r][c]
for a in ans:
    print(*a)