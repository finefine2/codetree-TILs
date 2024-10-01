from collections import deque 

N,M = tuple(map(int,input().split())) 
RED = 0 
ROCK = -1 
EMPTY = M+1 
EMPTY_BUNDLE = (-1,-1,-1,-1) 
board = [list(map(int,input().split())) for _ in range(N)] 

q = deque() 
visited = [[0] * N for _ in range(N)] 
ans = 0 

def in_range(r,c): 
    return 0<=r<N and 0<=c<N 

def can_go(r,c,color): 
    return in_range(r,c) and not visited[r][c] and (board[r][c] == color or board[r][c] == RED) 

def bfs(sr,sc,color): 
    # initialize visited 
    for r in range(N): 
        for c in range(N): 
            visited[r][c] = 0 
    visited[sr][sc] = 1 
    q.append((sr,sc)) 

    drs,dcs = [0,1,0,-1],[1,0,-1,0] 
    while q: 
        cr,cc = q.popleft() 
        for dr,dc in zip(drs,dcs): 
            nr,nc = cr + dr, cc + dc 
            if can_go(nr,nc,color): 
                q.append((nr,nc)) 
                visited[nr][nc] = 1 
def get_bundle(sr,sc): 
    bfs(sr,sc,board[sr][sc]) 

    bomb_cnt,red_cnt = 0,0 
    standard = (-1,-1) 
    for r in range(N): 
        for c in range(N): 
            if not visited[r][c]: 
                continue 
            bomb_cnt += 1 
            if board[r][c] == RED: 
                red_cnt += 1 
            elif (r,-c) > standard: 
                standard = (r,-c) 
    std_r,std_c = standard
    return (bomb_cnt,-red_cnt,std_r,std_c) 

def find_best_bundle(): 
    best_bundle = EMPTY_BUNDLE
    for r in range(N): 
        for c in range(N): 
            if board[r][c] >= 1: 
                bundle = get_bundle(r,c) 
                if bundle > best_bundle: 
                    best_bundle = bundle
    return best_bundle

def remove(): 
    for r in range(N): 
        for c in range(N): 
            if visited[r][c]: 
                board[r][c] = EMPTY 

def gravity(): 
    for sr in range(0,N-1): 
        for sc in range(N): 
            cr,cc = sr,sc 
            while in_range(cr,cc) and 0<=board[cr][cc]<=M and board[cr+1][cc] == EMPTY: 
                board[cr][cc],board[cr+1][cc] = board[cr+1][cc], board[cr][cc] 
                cr -= 1

def clean(r,c): 
    bfs(r,c,board[r][c]) 
    remove() 
    gravity()
ans = 0 
while True: 
    best_bundle = find_best_bundle() 
    bomb_cnt,_,r,c = best_bundle
    if best_bundle == EMPTY_BUNDLE or bomb_cnt <= 1: 
        break 
    ans += bomb_cnt ** 2 
    clean(r,-c) 
    board = list(map(list,zip(*board)))[::-1] 
    gravity() 
print(ans)