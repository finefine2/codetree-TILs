from collections import deque 
N, K = map(int,input().split()) 

board = [list(map(int,input().split())) for _ in range(N)] 
visited = [[0 for _ in range(N)] for _ in range(N)] 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 
def can_go(r,c): 
    if in_range(r,c) and board[r][c] == 0 and not visited[r][c]: 
        return True 
q = deque()

def bfs(): 
    while q: 
        r,c = q.popleft() 
        drs,dcs = [1,-1,0,0],[0,0,1,-1]

        for dr,dc in zip(drs,dcs): 
            new_r, new_c = r + dr, c + dc 
            if can_go(new_r,new_c): 
                q.append((new_r,new_c)) 
                visited[new_r][new_c] = 1

for _ in range(K): 
    r,c = map(int,input().split())
    q.append((r-1,c-1)) 
    visited[r-1][c-1] = 1
bfs()
cnt = 0 
for i in range(N): 
    for j in range(N): 
        if visited[i][j] == 1: 
            cnt += 1 
print(cnt)