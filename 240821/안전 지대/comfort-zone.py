import sys
sys.setrecursionlimit(2500)

N,M = tuple(map(int,input().split()))

# dfs 조건은 값이 k보다 클 때 반드시 명시해줘야함

board = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
K = -1

for r in range(N):
    for c in range(M):
        K = max(K, board[r][c])


def initialize():
    for r in range(N):
        for c in range(M):
            visited[r][c] = False

def in_range(r,c):
    return 0<=r<N and 0<=c<M

def dfs(r,c,k):
    drs,dcs = [1,0,-1,0], [0,1,0,-1]
    visited[r][c] = 1
    for dr,dc in zip(drs,dcs):
        nr,nc = r + dr, c + dc
        if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] > k:

            visited[nr][nc] = 1
            dfs(nr,nc,k)

# how to count zone area
# the number of area depends on k
# how to?
cnt = 0
def get_area(k):
    global cnt
    cnt = 0
    initialize()
    for r in range(N):
        for c in range(M):
            if in_range(r,c) and not visited[r][c] and board[r][c] > k:
                visited[r][c] = 1
                cnt += 1
                dfs(r,c,k)

max_num = -1
ans_k = 0

for k in range(1,K+1):
    get_area(k)
    if cnt > max_num:
        max_num,ans_k = cnt, k
print(ans_k, max_num)