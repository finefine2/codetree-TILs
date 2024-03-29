# N,M = map(int,input().split()) 

# board = [list(map(int,input().split())) for _ in range(N)] 

# def in_range(r,c): 
#     return 0 <= r < N and 0 <= c < M
# visited = [[0] * M for _ in range(N)] 

# def can_go(r,c): 
#     if not in_range(r,c): 
#         return False 
#     if visited[r][c] or board[r][c] == 0: 
#         return False
#     return True 


# def dfs(r,c): 
#     drs, dcs = [1,0], [0,1] 
#     for dr,dc in zip(drs, dcs): 
#         new_r, new_c = r + dr, c + dc 
#         if can_go(new_r,new_c): 
#             visited[new_r][new_c] = 1 
#             dfs(new_r,new_c) 

# visited[0][0] = 1 
# dfs(0,0) 

# print(visited[N-1][M-1])

N,M = map(int,input().split()) 

board = [list(map(int,input().split())) for _ in range(N)] 
visited = [[0 for _ in range(M)] for _ in range(N)] 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < M 

def can_go(r,c): 
    if not in_range(r,c): 
        return False
    if visited[r][c] or board[r][c] == 0: 
        return False 
    return True 

def dfs(r,c): 
    drs, dcs = [0,1],[1,0] 

    visited[r][c] = 1 
    for dr, dc in zip(drs,dcs): 
        new_r, new_c = r + dr, c + dc  
        if can_go(new_r,new_c): 
            dfs(new_r,new_c) 
dfs(0,0) 
print(visited[N-1][M-1])