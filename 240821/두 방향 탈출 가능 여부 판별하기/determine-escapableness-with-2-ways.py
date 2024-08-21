N,M = tuple(map(int,input().split())) 
board = [list(map(int,input().split())) for _ in range(N)] 
visited = [[0] * M for _ in range(N)] 

# 뱀이 없으면 1 있으면 0
drs, dcs = [1,0],[0,1] 


def dfs(r,c):
    visited[r][c] = 1 
    for dr,dc in zip(drs,dcs): 
        nr, nc = r + dr, c + dc 

        if 0<=nr<N and 0<=nc<M and board[nr][nc] == 1 and not visited[nr][nc]: 
            
            visited[nr][nc] = 1
            dfs(nr,nc) 
dfs(0,0) 
visited[0][0] = 1 
print(visited[N-1][M-1])