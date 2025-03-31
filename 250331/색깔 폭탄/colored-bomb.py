N,M = tuple(map(int,input().split()))
# -1 black 0 red 1~m color
BLACK = -1
RED = 0
EMPTY = M+1
board = [[-1] * (N+2)] + [[-1] + list(map(int,input().split())) + [-1] for _ in range(N)] + [[-1] * (N+2)]
from collections import deque

def gravity():
    for r in range(1,N):
        for c in range(1,N+1):
            cr,cc = r,c
            while 0<=board[cr][cc]<=M and board[cr+1][cc] == EMPTY:
                board[cr][cc],board[cr+1][cc] = board[cr+1][cc],board[cr][cc]
                cr -= 1


ans = 0

def get_base(group):
    base_r,base_c = 1,N+1
    for (r,c) in group:
        if board[r][c] != 0:
            if r > base_r or (r == base_r and c < base_c):
                base_r,base_c = r,c
    return base_r,base_c
# 가장 크기가 큰 폭탄 묶음을 찾아보자
def find_bfs():
    v = [[0] * (N+2) for _ in range(N+2)]
    mx_group = set()
    tlst = []

    for sr in range(1,N+1):
        for sc in range(1,N+1):
            if v[sr][sc] == 0 and 0<board[sr][sc]<=M:
                q = deque()
                groups = set()

                q.append((sr,sc))
                v[sr][sc] = 1
                groups.add((sr,sc))
                r_cnt = 0
                color = board[sr][sc]
                while q:
                    cr,cc = q.popleft()
                    for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                        nr,nc = cr + dr, cc + dc
                        if v[nr][nc] == 0 and (nr,nc) not in groups and (board[nr][nc] == color or board[nr][nc] == RED):
                            q.append((nr,nc))
                            groups.add((nr,nc))
                            if board[nr][nc] == 0:
                                r_cnt += 1
                            else:
                                v[nr][nc] = 1

                base_r,base_c = get_base(groups)
                tlst.append((len(groups),r_cnt,base_r,base_c,groups))
                if len(tlst) > 0:
                    tlst.sort(key=lambda x:(-x[0],x[1],-x[2],x[3]))
                    mx_group = tlst[0][-1]
    return mx_group
while True:
    # 최대 그룹 찾기
    bomb_group = find_bfs()
    if len(bomb_group) < 2:
        break
    ans += len(bomb_group) ** 2

    for br,bc in bomb_group:
        board[br][bc] = EMPTY

    gravity()
    board = list(map(list,zip(*board)))[::-1]
    gravity()

print(ans)