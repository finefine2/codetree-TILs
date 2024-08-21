from copy import deepcopy 

N,M = tuple(map(int,input().split())) 
board = [list(map(int,input().split())) for _ in range(N)] 
visited = [[0] * M for _ in range(N)] 

def initialize_visited(): 
    for r in range(N): 
        for c in range(M): 
            visited[r][c] = False 
zone_num = 0 

def in_range(r,c): 
    return 0<=r<N and 0<=c<M 

def dfs(r,c,k): 
    drs, dcs = [0,1,0,-1],[1,0,-1,0] 

    for dr,dc in zip(drs,dcs): 
        nr,nc = r + dr, c + dc 

        if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] > k: 
            visited[nr][nc] = True 
            dfs(nr,nc,k) 
def get_zone_num(k): 
    global zone_num
    zone_num =0 
    initialize_visited() 

    for r in range(N): 
        for c in range(M): 
            if in_range(r,c) and not visited[r][c] and board[r][c] > k: 
                visited[r][c] = 1 
                zone_num += 1 
                dfs(r,c,k) 

max_zone_num = -1 
ans_k = 0 
max_height = 100 
for k in range(1,max_height+1): 
    get_zone_num(k) 

    if zone_num > max_zone_num: 
        max_zone_num, ans_k = zone_num, k 
print(ans_k, max_zone_num)