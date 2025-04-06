N,L,R = map(int,input().split()) 

board = [list(map(int,input().split())) for _ in range(N)]
def in_range(r,c): 
    return 0<=r<N and 0<=c<N 

def can_move(r1,c1,r2,c2): 
    diff = abs(board[r1][c1] - board[r2][c2]) 
    return L<=diff<=R 
from collections import deque 

# 이동횟수 구하기 
def bfs(sr,sc,v): 
    q = deque() 
    v[sr][sc] = 1 

    tlst = [(sr,sc)] 
    q.append((sr,sc)) 
    total = board[sr][sc] 

    while q: 
        cr,cc = q.popleft() 

        for dr,dc in ((-1,0),(1,0),(0,1),(0,-1)): 
            nr,nc = cr + dr, cc + dc 
            if in_range(nr,nc) and can_move(cr,cc,nr,nc) and visited[nr][nc] == 0: 
                q.append((nr,nc)) 
                total += board[nr][nc] 
                tlst.append((nr,nc)) 
                v[nr][nc] = 1 

    if len(tlst) > 1: 
        avg =  total // len(tlst) 
        group = tlst 
        return avg, group 
    else: 
        return None 

cnt = 0 
while True: 
    visited = [[0] * N for _ in range(N)] 
    changes = [] 
    for r in range(N): 
        for c in range(N): 
            if not visited[r][c]: 
                ans = bfs(r,c,visited) 
                if ans: 
                    changes.append(ans) 
    if not changes: 
        break 

    for avg, group in changes: 
        for r,c in group: 
            board[r][c] = avg   
    cnt += 1 
print(cnt) 