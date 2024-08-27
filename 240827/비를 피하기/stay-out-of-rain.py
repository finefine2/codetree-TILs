from collections import deque

N,H,M = tuple(map(int,input().split()))
people_pos = []
board = []
exits = []
# 0 빈곳 1 벽 2 사람 3 피난처
for i in range(N):
    board.append(list(map(int,input().split())))
    for j in range(N):
        if board[i][j] == 2:
            people_pos.append((i,j))
        elif board[i][j] == 3:
            exits.append((i,j))
ans = [[0] * N for _ in range(N)]
steps = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def initialize_visit():
    for i in range(N):
        for j in range(N):
            visited[i][j] = 0
def initialize_steps():
    for i in range(N):
        for j in range(N):
            steps[i][j] = 0
def in_range(r,c):
    return 0<=r<N and 0<=c<N

def push(nr,nc,new_step):
    q.append((nr,nc))
    visited[nr][nc] = 1
    steps[nr][nc] = new_step

# for pr,pc in people_pos:
#     print(pr,pc)
q = deque()
def bfs():
    cnt = 10000
    drs,dcs = [1,0,-1,0],[0,1,0,-1]
    while q:
        r,c = q.popleft()
        for dr,dc in zip(drs,dcs):
            nr,nc = r + dr, c + dc
            if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] != 1:
                push(nr,nc,steps[r][c]+1)
    for er,ec in exits:
        if steps[er][ec]:
            cnt = min(cnt,steps[er][ec])
        else:
            cnt = -1
    return cnt

for p in people_pos:
    initialize_visit()
    initialize_steps()
    pr,pc = p
    q.append((pr,pc))
    visited[pr][pc] = 1
    steps[pr][pc] = 1

    ans[pr][pc] = bfs() - 1

for a in ans:
    print(*a)