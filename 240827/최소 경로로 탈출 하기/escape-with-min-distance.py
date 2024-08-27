import sys 
from collections import deque 

INT_MAX = sys.maxsize
N,M = tuple(map(int,input().split())) 
board = [list(map(int,input().split())) for _ in range(N)]

q = deque() 
visited = [[0] * M for _ in range(N)] 
steps = [[0] * M for _ in range(N)] 

ans = INT_MAX
def in_range(r,c): 
    return 0<=r<N and 0<=c<M 

def can_move(r,c): 
    return in_range(r,c) and board[r][c] and not visited[r][c] 

def push(new_r,new_c,new_step): 
    q.append((new_r,new_c)) 
    visited[new_r][new_c] = 1 
    steps[new_r][new_c] = new_step

def find_min(): 
    global ans 
    drs,dcs = [1,0,-1,0],[0,1,0,-1] 
    while q: 
        r,c = q.popleft() 
        for dr,dc in zip(drs,dcs): 
            nr,nc = r + dr, c + dc 
            if can_move(nr,nc): 
                push(nr,nc,steps[r][c]+1) 
    if visited[N-1][M-1]: 
        ans = steps[N-1][M-1] 
push(0,0,0) 
find_min() 
if ans == INT_MAX: 
    ans = -1
print(ans)