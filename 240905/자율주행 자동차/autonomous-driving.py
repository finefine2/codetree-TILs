N,M = tuple(map(int,input().split()))
r,c,d = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

def in_range(r,c):
    return 0<=r<N and 0<=c<M

def can_move(r,c):
    return not visited[r][c] and board[r][c] == 0

def simulate():
    global r,c,d
    drs,dcs = [-1,0,1,0],[0,1,0,-1]
    for i in range(4):
        nd = (d-1) % 4
        nr,nc = r + drs[nd], c + dcs[nd]
        if in_range(nr,nc) and can_move(nr,nc):
            r,c = nr,nc
            d = nd
            visited[nr][nc] = 1
            return True
        else:
            d = nd
    nr,nc = r - drs[d], c - dcs[d]
    if board[nr][nc] == 1:
        return False
    else:
        return True


visited[r][c] = 1
while True:
    is_moved = simulate()
    if not is_moved:
        break
ans = sum(visited[i][j]
          for i in range(N)
          for j in range(M))
print(ans)