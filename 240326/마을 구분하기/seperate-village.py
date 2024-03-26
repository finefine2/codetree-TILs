N = int(input()) 

board = [list(map(int,input().split())) for _ in range(N)] 
visited = [[False for _ in range(N)] for _ in range(N)] 

cnt = 0 
cnt_list = list() 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

def can_go(r,c): 
    if not in_range(r,c): 
        return False
    if visited[r][c] or board[r][c] == 0: 
        return False 
    return True 

def dfs(r,c): 
    global cnt 

    drs,dcs = [0,1,0,-1],[1,0,-1,0] 

    for dr,dc in zip(drs,dcs): 
        new_r, new_c = r + dr, c + dc 

        if can_go(new_r,new_c): 
            visited[new_r][new_c] = True
            cnt += 1 
            dfs(new_r,new_c) 
    
for i in range(N): 
    for j in range(N): 
        if can_go(i,j): 
            visited[i][j] = True
            cnt = 1

            dfs(i,j) 
            cnt_list.append(cnt) 
cnt_list.sort() 
print(len(cnt_list)) 
for c in cnt_list: 
    print(c)