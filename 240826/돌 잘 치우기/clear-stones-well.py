import copy
from collections import deque

def gen_combi(arr,n):
    res = []
    if n == 0:
        return [[]]
    for i in range(0,len(arr)):
        elem = arr[i]
        for C in gen_combi(arr[i+1:],n-1):
            res.append([elem]+C)
    return res
N,K,M = tuple(map(int,input().split()))
board = []
visited = [[0] * N for _ in range(N)]
stones = []
starts = []
for i in range(N):
    board.append(list(map(int,input().split())))
    for j in range(N):
        if board[i][j] == 1:
            stones.append((i,j))
for i in range(K):
    r,c = tuple(map(int,input().split()))
    starts.append((r-1,c-1))
# print(stones)
def initialize_visit():
    for r in range(N):
        for c in range(N):
            if (r,c) not in starts:
                visited[r][c] = 0

def in_range(r,c):
    return 0<=r<N and 0<=c<N

def bfs():
    drs,dcs = [1,0,-1,0],[0,1,0,-1]
    while q:
        r,c = q.popleft()
        for dr,dc in zip(drs,dcs):
            nr,nc = r + dr, c + dc
            if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] == 1:
                q.append((nr,nc))
                visited[nr][nc] = 1
def calc_visit():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                cnt += 1
    return cnt

stones_select = gen_combi(stones,M)

# 영역의 최대화 - 돌이 이어진 곳이 최소화
min_ans = 10000
for i in range(len(stones_select)):
    initialize_visit()
    stones_remove = stones_select[i]
    q = deque()
    for sr,sc in stones:
        # print(sr,sc)
        if (sr,sc) in stones_remove:
            # print(f"but those have to be removed {sr, sc}")
            continue
        else:
            q.append((sr,sc))
            visited[sr][sc] = 1
    # print(f"final queue looks like {q} ")
    # bfs()
    mid = calc_visit()
    # print(mid)
    min_ans = min(mid,min_ans)

    # for b in board:
    #     print(*b)
    # print("##############")
print(N*N - min_ans)