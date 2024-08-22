from collections import deque 

N,K = tuple(map(int,input().split())) 

board = [list(map(int,input().split())) for _ in range(N)] 
visited = [[0] * N for _ in range(N)]
q = deque() 

def in_range(r,c): 
    return 0<=r<N and 0<=c<N 

def bfs(): 
    drs,dcs = [1,0,-1,0],[0,1,0,-1]
    while q: 
        r,c = q.popleft() 
        for dr,dc in zip(drs,dcs): 
            nr,nc = r + dr, c + dc 
            if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] == 0: 
                q.append((nr,nc)) 
                visited[nr][nc] = 1 
for _ in range(K): 
    r,c = tuple(map(int,input().split()))
    visited[r-1][c-1] = 1 
    q.append((r-1,c-1)) 
bfs()

ans = sum([
    visited[r][c] 
    for r in range(N) 
    for c in range(N)
])
print(ans)