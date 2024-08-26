import copy
from collections import deque

N,K,M = tuple(map(int,input().split()))
board = []
# 1: stone, 0: blank,
stones = []
for i in range(N):
    board.append((list(map(int,input().split()))))
    for j in range(N):
        if board[i][j] == 1:
            stones.append((i,j))
starts = []
for i in range(K):
    r,c = tuple(map(int,input().split()))
    starts.append((r-1,c-1))

visited = [[0] * N for _ in range(N)]

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

def bfs():
    drs, dcs = [1,0,-1,0],[0,1,0,-1]
    while q:
        r,c = q.popleft()
        for dr,dc in zip(drs,dcs):
            nr,nc = r + dr, c + dc
            if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] == 0:
                q.append((nr,nc))
                visited[nr][nc] = 1
stone_combi = gen_combi(stones,M)

def calc_visit():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                cnt += 1
    return cnt
# q = deque()
# for sr,sc in starts:
#     print(sr, sc)
#     visited[sr][sc] = 1
#     q.append((sr,sc))
# bfs()
# print(calc_visit())
max_ans = -1
for i in range(len(stone_combi)):
    initialize_board()
    initialize_visit()
    q = deque()
    for sr,sc in starts:
        q.append((sr,sc))
        visited[sr][sc] = 1

    stone_remove = stone_combi[i]
    for sr,sc in stone_remove:
        board[sr][sc] = 0 
    bfs()
    max_ans = max(max_ans,calc_visit())

print(max_ans)