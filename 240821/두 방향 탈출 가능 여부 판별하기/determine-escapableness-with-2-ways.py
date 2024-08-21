N,M = tuple(map(int,input().split())) 
board = [list(map(int,input().split())) for _ in range(N)] 
visited = [[False] * M for _ in range(N)] 

# 뱀이 없으면 1 있으면 0

start_r, start_c = 0,0 
end_r, end_c = N-1, M-1 
drs, dcs = [1,0],[0,1] 

possible = False 
def dfs(r,c):
    visited[r][c] = True 
    for dr,dc in zip(drs,dcs): 
        nr, nc = r + dr, c + dc 

        if 0<=nr<N and 0<=nc<M and board[nr][nc] == 1 and not visited[nr][nc]: 
            
            visited[nr][nc] = True
            start_r, start_c = nr,nc 
            dfs(nr,nc) 
dfs(0,0) 
if (start_r, start_c) == (end_r, end_c): 
    print(1)
else: 
    print(0)