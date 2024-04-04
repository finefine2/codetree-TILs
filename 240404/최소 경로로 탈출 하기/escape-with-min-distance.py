import sys
from collections import deque 
INT_MAX = sys.maxsize
N, M = map(int,input().split()) 

board = [list(map(int,input().split())) for _ in range(N)] 

visited = [[False for _ in range(M)] for _ in range(N)] 
step = [[0 for _ in range(M)] for _ in range(N)] 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < M 

def can_go(r,c): 
    if in_range(r,c) and not visited[r][c] and board[r][c] == 1: 
        return True

def push(r,c,s): 
    q.append((r,c))
    visited[r][c] = True
    step[r][c] = s 

ans = INT_MAX
q = deque() 
def bfs(): 
    drs, dcs = [0,1,0,-1],[1,0,-1,0] 
    while q: 
        r,c = q.popleft() 
        for dr, dc in zip(drs,dcs): 
            new_r,new_c = r + dr, c + dc 
            if can_go(new_r,new_c): 
                push(new_r,new_c,step[r][c] + 1) 

    if visited[N-1][M-1]: 
        ans = step[N-1][M-1] 
    
push(0,0,0) 
bfs() 
if ans == INT_MAX:
    ans = -1 
print(ans)