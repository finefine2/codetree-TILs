from collections import deque
import copy

N,M = tuple(map(int,input().split()))
board = []
fires = []
blanks = []

for i in range(N):
    board.append(list(map(int,input().split())))
    for j in range(M):
        if board[i][j] == 2:
            fires.append((i,j))
        elif board[i][j] == 0:
            blanks.append((i,j))
visited = [[0] * M for _ in range(N)]
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
        for j in range(M):
            visited[i][j] = 0
new_board = copy.deepcopy(board)
def initialize_board():
    for i in range(N):
        for j in range(M):
            board[i][j] = new_board[i][j]

def in_range(r,c):
    return 0<=r<N and 0<=c<M

def bfs():
    drs,dcs = [1,0,-1,0],[0,1,0,-1]
    while q:
        r,c = q.popleft()
        for dr,dc in zip(drs,dcs):
            nr,nc = r + dr, c + dc
            if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] != 1:
                q.append((nr,nc))
                visited[nr][nc] = 1
                board[nr][nc] = 2 

def calc_zero():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1
    return cnt
# 방화벽 세울 위치

wall_pos = gen_combi(blanks,3)
max_ans = -1
for i in range(len(wall_pos)):
    initialize_board()
    initialize_visit()
    walls = wall_pos[i]
    for wr,wc in walls:
        board[wr][wc] = 1
    q = deque()
    for fr,fc in fires:
       visited[fr][fc] = 1
       q.append((fr,fc))
    bfs()
    max_ans = max(max_ans,calc_zero())
print(max_ans)