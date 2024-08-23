import copy
from collections import deque

N,K,M = tuple(map(int,input().split()))
board = []
stone_pos = []
for i in range(N):
    board.append(list(map(int,input().split())))
    for j in range(N):
        if board[i][j] == 1:
            stone_pos.append((i,j))

visited = [[0] * N for _ in range(N)]
q = deque()
start_pos = []
for _ in range(K):
    r,c = tuple(map(int,input().split()))
    q.append((r-1,c-1))
    visited[r-1][c-1] = 1
    start_pos.append((r-1,c-1))
def initialize_visit():
    for r in range(N):
        for c in range(N):
            if (r,c) not in start_pos:
                visited[r][c] = 0
def gen_combi(arr,n):
    res = []
    if n == 0:
        return [[]]
    for i in range(0,len(arr)):
        elem = arr[i]
        for C in gen_combi(arr[i+1:],n-1):
            res.append([elem]+C)
    return res
def in_range(r,c):
    return 0<=r<N and 0<=c<N

def can_move(r,c):
    global new_board
    return in_range(r,c) and not visited[r][c] and new_board[r][c] == 0

drs, dcs = [1,0,-1,0],[0,1,0,-1]
def bfs():
    while q:
        r,c = q.popleft()
        for dr,dc in zip(drs,dcs):
            nr,nc = r + dr, c + dc
            if can_move(nr,nc):
                q.append((nr,nc))
                visited[nr][nc] = 1
stone_combi = gen_combi(stone_pos,M)

def get_ans():
    return sum(visited[i][j] for i in range(N) for j in range(N))

def change_board(stone_c):

    new_r, new_c = 0,0
    for sr,sc in stone_c:
        new_r, new_c = sr,sc

    for r in range(N):
        for c in range(N):
            if (r,c) == (new_r,new_c):
                new_board[r][c] = 0
    return new_board
ans = -1
for stone_c in stone_combi:
    new_board = copy.deepcopy(board)
    change_board(stone_c)
    initialize_visit()
    bfs()
    ans = max(ans, get_ans())
print(ans)