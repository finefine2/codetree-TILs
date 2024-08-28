import copy
from collections import deque
N,K = tuple(map(int,input().split()))
walls = []
board = []
for i in range(N):
    board.append(list(map(int,input().split())))
    for j in range(N):
        if board[i][j] == 1:
            walls.append((i,j))

r1,c1 = tuple(map(int,input().split()))
r2,c2 = tuple(map(int,input().split()))

r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1
visited = [[0] * N for _ in range(N)]
steps = [[0] * N for _ in range(N)]
def gen_combi(arr,n):
    res = []
    if n == 0:
        return [[]]
    for i in range(0,len(arr)):
        elem = arr[i]
        for C in gen_combi(arr[i+1:],n-1):
            res.append([elem]+C)
    return res

def initialize_visit():
    for i in range(N):
        for j in range(N):
            visited[i][j] = 0
new_board = copy.deepcopy(board)
def initialize_board():
    for i in range(N):
        for j in range(N):
            board[i][j] = new_board[i][j]
def in_range(r,c):
    return 0<=r<N and 0<=c<N

def push(nr,nc,new_step):
    visited[nr][nc] = 1
    q.append((nr,nc))
    steps[nr][nc] = new_step

def bfs():
    drs, dcs = [1,0,-1,0],[0,1,0,-1]
    while q:
        r,c = q.popleft()
        for dr,dc in zip(drs,dcs):
            nr,nc = r + dr, c + dc
            if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] == 0:
                push(nr,nc,steps[r][c]+1)

wall_remove = gen_combi(walls,K)

min_ans = 10000
for i in range(len(wall_remove)):
    initialize_visit()
    initialize_board()
    wall_out = wall_remove[i]
    for wr,wc in wall_out:
        board[wr][wc] = 0

    q = deque()
    push(r1,c1,0)
    bfs()
    if steps[r2][c2] != 0:
        min_ans = min(min_ans,steps[r2][c2])
if min_ans == 10000:
    print(-1)
else:
    print(min_ans)