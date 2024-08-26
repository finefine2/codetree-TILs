from collections import deque 

N,M = tuple(map(int,input().split())) 

board = [list(map(int,input().split())) for _ in range(N)] 
# steps = [[0] * M for _ in range(N)] 
visited = [[0] * M for _ in range(N)] 

def in_range(r,c): 
    return 0<=r<N and 0<=c<M 

def bfs(): 
    drs,dcs = [1,0,-1,0],[0,1,0,-1]
    while q: 
        r,c = q.popleft() 
        for dr,dc in zip(drs,dcs): 
            nr,nc = r + dr, c + dc 
            if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] == 1: 
                visited[nr][nc] = visited[r][c] + 1 
                q.append((nr,nc))


q = deque() 
q.append((0,0)) 
visited[0][0] = 1
bfs()


if visited[N-1][M-1] == 0: 
    print(-1) 
else: 
    print(visited[N-1][M-1]-1)