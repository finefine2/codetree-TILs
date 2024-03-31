from collections import deque 

N, K = map(int,input().split()) 

board = [list(map(int,input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)] 


q = deque() 
def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

def can_go(r,c): 
    if in_range(r,c) and not visited[r][c] and board[r][c] == 0:
        return True
def bfs():
    drs,dcs = [0,1,0,-1],[1,0,-1,0] 

    while q: 
        r,c = q.popleft() 

        for dr, dc in zip(drs,dcs): 
            new_r, new_c = r + dr, c + dc 
            if can_go(new_r,new_c): 
                visited[new_r][new_c] = True 
                q.append((new_r,new_c))

for _ in range(K): 
    r,c = map(int,input().split())
    q.append((r-1,c-1)) 
    visited[r-1][c-1] = True 
cnt = 0 
bfs() 

for i in range(N): 
    for j in range(N): 
        if visited[i][j] == True: 
            cnt += 1 
print(cnt)