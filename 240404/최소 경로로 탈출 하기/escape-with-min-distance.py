from collections import deque
N,M =map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)] 

def in_range(r,c): 
    return 0<=r<N and 0<=c<M 
def can_go(r,c): 
    if in_range(r,c) and not visited[r][c] and board[r][c] == 1: 
        return True

def bfs(): 
    drs, dcs = [0,1,0,-1],[1,0,-1,0]
    while q: 
        r,c = q.popleft() 
        for dr,dc in zip(drs,dcs): 
            new_r, new_c = r + dr, c + dc
            if can_go(new_r,new_c): 
                visited[new_r][new_c] = visited[new_r][new_c] + 1 
                q.append((new_r,new_c)) 

q = deque()
visited = [[0] * M for _ in range(N)]
visited[0][0] = 0
q.append((0,0))
bfs()

if visited[N-1][M-1] == 0 or visited[N-1][M-1] == 1: 
    print(-1) 
else: 
    print(visited[N-1][M-1])