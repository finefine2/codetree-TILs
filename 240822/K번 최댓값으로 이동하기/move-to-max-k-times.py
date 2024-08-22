from collections import deque 

N,K = tuple(map(int,input().split())) 
board = [list(map(int,input().split())) for _ in range(N)] 
r,c = tuple(map(int,input().split())) 

curr_pos = (r-1,c-1) 

visited = [[0] * N for _ in range(N)]
NOT_EXISTS = (-1,-1) 

def initialize(): 
    for r in range(N): 
        for c in range(N): 
            visited[r][c] = 0

def in_range(r,c): 
    return 0<=r<N and 0<=c<N 

def can_move(r,c,target_num): 
    return in_range(r,c) and not visited[r][c] and board[r][c] < target_num

q = deque() 

def bfs(): 
    drs, dcs = [1,0,-1,0],[0,1,0,-1]
    cr,cc = curr_pos
    q.append(curr_pos) 
    visited[cr][cc] = 1 
    target_num = board[cr][cc] 

    while q: 
        cr,cc = q.popleft() 
        for dr,dc in zip(drs,dcs): 
            nr,nc = cr + dr, cc + dc 

            if can_move(nr,nc,target_num): 
                q.append((nr,nc)) 
                visited[nr][nc] = 1 

def need_update(new_pos,best_pos): 
    if best_pos == NOT_EXISTS: 
        return True 
    nr,nc = new_pos
    br,bc = best_pos

    return (board[nr][nc],-nr,-nc) > (board[br][bc],-br,-bc) 

def move(): 
    global curr_pos
    initialize() 
    bfs() 
    best_pos = NOT_EXISTS

    for r in range(N): 
        for c in range(N): 
            if not visited[r][c] or (r,c) == curr_pos: 
                continue 
            new_pos = (r,c) 

            if need_update(new_pos, best_pos): 
                best_pos = new_pos
    if best_pos == NOT_EXISTS: 
        return False 
    else: 
        curr_pos = best_pos
        return True


for _ in range(K): 
    is_moved = move() 

    if not is_moved: 
        break 

fr, fc = curr_pos
print(fr+1,fc+1)