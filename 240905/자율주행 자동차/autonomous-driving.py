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
    # 4방향에 대해서 모두 탐색을 진행한다
    for i in range(4):
        nd = (d-1) % 4 
        nr,nc = r + drs[nd], c + dcs[nd] 
        if in_range(nr,nc) and can_move(nr,nc): 
            visited[nr][nc] = 1 
            r,c = nr,nc 
            d = nd
            return True
        else: 
            d = nd
    # 만약 못 가면 후진
    nr,nc = r - drs[d], c - dcs[d] 
    # 후진하게 되면 좌표 변경 
    if board[nr][nc] == 1: 
        return False 
    else: 
        r,c = nr,nc
        return True
    
visited[r][c] = 1
while True: 
    is_moved = simulate() 
    if not is_moved: 
        break 
        
ans = sum(visited[i][j]
          for i in range(N)
          for j in range(M))