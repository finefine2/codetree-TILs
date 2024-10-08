from collections import deque

N,M  = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]

EMPTY = M+1
RED = 0
def in_range(r,c):
    return 0<=r<N and 0<=c<N
def bfs(sr,sc):
    q = deque()
    q.append((sr,sc))
    v = [[0] * N for _ in range(N)]
    v[sr][sc] = 1
    tmp,tmp_red,tmp_list = 1,0,[(sr,sc)]
    drs,dcs = [-1,1,0,0],[0,0,-1,1]
    while q:
        cr,cc = q.popleft()
        for dr,dc in zip(drs,dcs):
            nr,nc = cr + dr, cc + dc
            if in_range(nr,nc) and not v[nr][nc] and (board[nr][nc] == board[cr][cc] or board[nr][nc] == RED):
                q.append((nr,nc))
                v[nr][nc] = 1
                tmp += 1
                tmp_list.append((nr,nc))
                if board[nr][nc] == RED:
                    tmp_red += 1
    return tmp, tmp_red, tmp_list
def gravity():
    for sr in range(N-1):
        for sc in range(N):
            cr,cc = sr,sc
            while in_range(cr,cc) and 0<=board[cr][cc]<=M and board[cr+1][cc]==EMPTY:
                board[cr][cc],board[cr+1][cc] = board[cr+1][cc],board[cr][cc]
                cr -= 1
ans = 0
while True:

    max_cnt, min_red, bomb_list = 0,N**2,[]
    # 행이 크고 열은 작다
    for r in range(N-1,-1,-1):
        for c in range(N):
            if 0 < board[r][c] <= M:
                tmp,tmp_red,tmp_list = bfs(r,c)
                # 크기가 가장 큰 폭탄묶음
                if tmp > max_cnt:
                    max_cnt = tmp
                    min_red = tmp_red
                    bomb_list = tmp_list
                # 빨간 폭탄이 가장 적게 포함
                elif tmp == max_cnt:
                    if tmp_red < min_red:
                        min_red = tmp_red
                        bomb_list = tmp_list

    if max_cnt < 2:
        break
    ans += max_cnt ** 2
    # 폭탄 제거
    for br,bc in bomb_list:
        board[br][bc] = EMPTY
    gravity()
    # counter clockwise rotation
    board = list(map(list,zip(*board)))[::-1]
    gravity()
print(ans)