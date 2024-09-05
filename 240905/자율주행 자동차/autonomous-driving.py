N,M = tuple(map(int,input().split()))
r,c,d = tuple(map(int,input().split()))

board = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def in_range(r,c):
    return 0<=r<N and 0<=c<M

cnt = 0
def move():

    global r,c,d,cnt
    visited[r][c] = 1
    # N E S W
    drs,dcs = [-1,0,1,0],[0,1,0,-1]
    # 4 방향을 먼저 탐색한다
    for i in range(4):
        nd = (d-1) % 4
        nr,nc = r + drs[nd], c + dcs[nd]
        if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] == 0:
            r,c = nr,nc
            d = nd
            return True
        else:
            d = nd
    # 만약 불가능하다면 후진을 시도한다
    nr,nc = r - drs[d], c - dcs[d]
    if board[nr][nc] == 0:
        r,c = nr,nc
        return True
    else:
        return False

while True:
    moved = move()

    if not moved:
        break
    else:
        cnt += 1
print(cnt)