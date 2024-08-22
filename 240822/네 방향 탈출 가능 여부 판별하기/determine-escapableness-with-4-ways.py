from collections import deque

N,M = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

q = deque()

def in_range(r,c):
    return 0<=r<N and 0<=c<M

def bfs():
    while q:
        r,c = q.popleft()
        drs,dcs = [0,1,0,-1],[1,0,-1,0]
        for dr,dc in zip(drs,dcs):
            nr,nc = r+dr, c+dc
            if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] == 1:
                q.append((nr,nc)) 
                visited[nr][nc] = 1 
q.append((0,0)) 
visited[0][0] = 1 
bfs() 
ans = 1 if visited[N-1][M-1] else 0 
print(ans)