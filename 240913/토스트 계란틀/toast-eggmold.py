# 모든 좌표를 돌면서 bfs를 수행하자
from collections import deque

N,L,R = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

def initialize_visit():
    for i in range(N):
        for j in range(N):
            visited[i][j] = 0
def in_range(r,c):
    return 0<=r<N and 0<=c<N

def can_move(r,c,num):
    return in_range(r,c) and not visited[r][c] and L <= abs(board[r][c]-num) <= R

egg_groups = []
def bfs():
    drs,dcs = [1,0,-1,0],[0,1,0,-1]
    while q:
        r,c = q.popleft()
        for dr,dc in zip(drs,dcs):
            nr,nc = r + dr, c + dc
            if can_move(nr,nc,board[r][c]):
                q.append((nr,nc))
                visited[nr][nc] = 1
                egg_groups.append([nr,nc])

def change_egg():
    egg_amount = 0
    for r,c in egg_groups:
        egg_amount += board[r][c]

    for r,c in egg_groups:
        board[r][c] = int(egg_amount / len(egg_groups))

q = deque()
def move():
    global egg_groups
    initialize_visit()
    is_changed = False

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                egg_groups = []
                q.append((r,c))
                egg_groups.append([r,c])
                visited[r][c] = 1

                bfs()

                if len(egg_groups) > 1:
                    is_changed = True
                change_egg()
    return is_changed
cnt = 0
while True:
    is_moved = move()
    if is_moved:
        cnt += 1
    else:
        break
print(cnt)