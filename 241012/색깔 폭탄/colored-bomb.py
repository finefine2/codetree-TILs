from collections import deque
N,M = tuple(map(int,input().split()))
EMPTY = M+1
# -1 black, 0 red, 1~m color
board = [[-1] * (N+2)] + [[-1] + list(map(int,input().split())) + [-1] for _ in range(N)] + [[-1] * (N+2)]

def get_base(group):
    base_r, base_c = -1, N+1
    for (r,c) in group:
        if base_r < r or (base_r == r and base_c > c):
            base_r,base_c = r,c
    return base_r,base_c
ans = 0
# 가장 큰 폭탄묶음을 찾아야한다
def bfs():
    v = [[0] * (N+2) for _ in range(N+2)]
    mx_group = set()
    tlst = []
    for r in range(1,N+1):
        for c in range(1,N+1):
            if v[r][c] == 0 and M >= board[r][c] > 0: # 일반 색깔 폭탄에 대해서만 조사를 해보자고
                q = deque()
                groups = set() # 같은 그룹이면 추가하기

                v[r][c] = 1
                groups.add((r,c))
                q.append((r,c))
                r_cnt = 0 # 빨간 폭탄 세는 거
                color = board[r][c]
                while q:
                    cr,cc = q.popleft()
                    for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                        nr,nc = cr + dr, cc + dc
                        if v[nr][nc] == 0 and (nr,nc) not in groups and (board[nr][nc] == color or board[nr][nc] == 0):
                            groups.add((nr,nc))
                            q.append((nr,nc))
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

def gravity():
    for r in range(1,N):
        for c in range(1,N+1):
            cr,cc = r,c
            while 0<=board[cr][cc]<=M and board[cr+1][cc] == EMPTY:
                board[cr][cc],board[cr+1][cc] = board[cr+1][cc],board[cr][cc]
                cr -= 1
while True:

    bomb_group = bfs()
    if len(bomb_group) < 2:
        break
    ans += len(bomb_group) ** 2
    for br,bc in bomb_group:
        board[br][bc] = EMPTY

    gravity()
    board = list(map(list,zip(*board)))[::-1]
    gravity()
print(ans)