N,r,c = tuple(map(int,input().split())) 
board = [list(map(int,input().split())) for _ in range(N)] 
start_r,start_c = r-1,c-1 

drs,dcs = [-1,1,0,0],[0,0,-1,1] 
def in_range(r,c): 
    return 0<=r<N and 0<=c<N 

def simulate(): 
    global start_r,start_c

    for dr,dc in zip(drs,dcs): 
        nr,nc = start_r+dr, start_c+dc
        if in_range(nr,nc) and board[nr][nc] > board[start_r][start_c]: 
            start_r,start_c = nr,nc
            return True
ans = [] 
ans.append(board[start_r][start_c])
while True: 
    can_move = simulate()
    if can_move: 
        ans.append(board[start_r][start_c]) 
    else: 
        break 
for a in ans: 
    print(a,end=" ")