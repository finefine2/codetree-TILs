N = int(input()) 

board = [list(map(int,input().split())) for _ in range(N)] 
visited = [[False for _ in range(N)] for _ in range(N)] 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

def can_go(r,c,num): 
    if not in_range(r,c): 
        return False 
    if visited[r][c] or board[r][c] != num: 
        return False 
    return True 

max_block, bomb_cnt = 0,0 
curr_num = 0 
def dfs(r,c): 
    global curr_num
    drs,dcs = [0,1,0,-1],[1,0,-1,0] 

    for dr, dc in zip(drs,dcs): 
        new_r, new_c = r + dr, c+ dc 
        if can_go(new_r,new_c,board[r][c]): 
            visited[new_r][new_c] = True 
            curr_num += 1 
            dfs(new_r,new_c) 

for i in range(N): 
    for j in range(N): 
        if not visited[i][j] and board[i][j]: 
            visited[i][j] = True 
            curr_num = 1 
            dfs(i,j) 

            if curr_num >= 4: 
                bomb_cnt += 1 
            max_block = max(max_block, curr_num) 
print(bomb_cnt, max_block)