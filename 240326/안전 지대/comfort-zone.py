N,M = map(int,input().split()) 

board = [list(map(int,input().split())) for _ in range(N)] 
visited = [[False for _ in range(M)] for _ in range(N)] 

zone_num = 0 
def initialize_visited(): 
    for i in range(N): 
        for j in range(M): 
            visited[i][j] = False 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < M 

def can_go(r,c,k): 
    if not in_range(r,c): 
        return False 
    if visited[r][c] or board[r][c] <= k: 
        return False 
    return True 

def dfs(r,c,k): 
    drs, dcs = [0,1,0,-1],[1,0,-1,0] 
    for dr,dc in zip(drs,dcs): 
        new_r, new_c = r + dr, c + dc 

        if can_go(new_r, new_c, k): 
            visited[new_r][new_c] = True 
            dfs(new_r, new_c, k) 

def get_zone_num(k):
    global zone_num
    zone_num = 0 
    initialize_visited() 

    for i in range(N): 
        for j in range(M): 
            if can_go(i,j,k): 
                visited[i][j] = True 
                zone_num += 1
                dfs(i,j,k) 

max_zone_num = -1 
ans_k = 0 
max_height = 100 
for k in range(1,max_height+1): 
    get_zone_num(k) 
    if zone_num > max_zone_num: 
        max_zone_num, ans_k = zone_num, k 
print(ans_k, max_zone_num)