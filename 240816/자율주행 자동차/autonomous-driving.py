N,M = map(int,input().split()) 

r,c,d = map(int,input().split()) 

board = [list(map(int,input().split())) for _ in range(N)]

# N E S W 
drs, dcs = [-1,0,1,0], [0,1,0,-1] 

cnt = 0 

def clean(r,c,d): 
    global cnt

    if board[r][c] == 0: 
        board[r][c] = 2 
        cnt += 1 

    for _ in range(4): 
        nd = (d+3) % 4 
        nr,nc = r + drs[nd], c + dcs[nd] 

        if board[nr][nc] == 0: 
            clean(nr,nc,nd) 
            return 
        d = nd 

    nr, nc = r - drs[d], c - dcs[d] 
    if board[nr][nc] == 1: 
        return 
    else: 
        clean(nr,nc,d) 
clean(r,c,d) 
print(cnt)