N,M,K,C = tuple(map(int,input().split())) 

board = [list(map(int,input().split())) for _ in range(N)] 
nboard = [x[:] for x in board]
spray = [[0] * N for _ in range(N)] 

ans = 0 
def in_range(r,c): 
    return 0<=r<N and 0<=c<N 
def grow():
    drs,dcs= [1,-1,0,0],[0,0,1,-1] 
    for r in range(N): 
        for c in range(N): 
            cnt = 0 
            if board[r][c] > 0: 
                for dr,dc in zip(drs,dcs): 
                    nr,nc = r + dr, c + dc 
                    if in_range(nr,nc) and board[nr][nc] > 0: 
                        cnt += 1 
            board[r][c] += cnt
def spread(): 
    drs,dcs = [1,-1,0,0],[0,0,1,-1] 
    for r in range(N): 
        for c in range(N): 
            nboard[r][c] = 0 
    for r in range(N): 
        for c in range(N): 
            if board[r][c] > 0: 
                tree_cnt = 0 
                tlst = [] 
                for dr,dc in zip(drs,dcs): 
                    nr,nc = r + dr, c + dc 
                    if in_range(nr,nc) and board[nr][nc] == 0 and spray[nr][nc] == 0: 
                        tree_cnt +=1 
                        tlst.append([nr,nc]) 
                for nnr,nnc in tlst: 
                    nboard[nnr][nnc] += board[r][c] // tree_cnt
    for r in range(N): 
        for c in range(N): 
            board[r][c] += nboard[r][c]
def remove(): 
    global ans 
    frs,fcs = [1,-1,1,-1],[1,1,-1,-1] 
    max_del,max_r,max_c = 0,0,0
    for r in range(N): 
        for c in range(N): 
            if board[r][c] > 0: 
                cnt = board[r][c] 
                for fr,fc in zip(frs,fcs): 
                    for i in range(1,K+1): 
                        nr,nc = r + fr*i, c + fc*i 
                        if in_range(nr,nc): 
                            if board[nr][nc] > 0: 
                                cnt += board[nr][nc] 
                            else: 
                                break 
                if max_del < cnt: 
                    max_del = cnt 
                    max_r,max_c = r,c 
    ans += max_del
    for fr,fc in zip(frs,fcs): 
        start_r,start_c = max_r,max_c
        board[start_r][start_c] = 0 
        spray[start_r][start_c] = C 
        for i in range(1,K+1): 
            nr,nc = start_r + fr * i, start_c + fc * i 
            if in_range(nr,nc): 
                if board[nr][nc] == -1: 
                    break 
                elif board[nr][nc] == 0: 
                    spray[nr][nc] = C 
                    break 
                elif board[nr][nc] > 0: 
                    spray[nr][nc] = C 
                    board[nr][nc] = 0 
def decrease(): 
    for r in range(N): 
        for c in range(N): 
            if spray[r][c] > 0: 
                spray[r][c] -= 1
for i in range(M): 
    grow() 
    spread() 
    decrease() 
    remove() 

print(ans)