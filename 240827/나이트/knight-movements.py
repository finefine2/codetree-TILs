from collections import deque 
import sys 

INT_MAX = sys.maxsize

N = int(input()) 
r1,c1,r2,c2 = tuple(map(int,input().split())) 
r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1 

q = deque() 
visited = [[0] * N for _ in range(N)] 
steps = [[0] * N for _ in range(N)] 
ans = INT_MAX

def in_range(r,c): 
    return 0<=r<N and 0<=c<N 

def can_go(r,c): 
    return in_range(r,c) and not visited[r][c] 

def push(nr,nc,new_step): 
    q.append((nr,nc)) 
    visited[nr][nc] = 1 
    steps[nr][nc] = new_step

def find_min(): 
    global ans 
    drs,dcs = [-2,-2,-1,-1,1,1,2,2], [-1,1,-2,2,2,-2,1,-1] 
    while q: 
        r,c = q.popleft() 
        for dr,dc in zip(drs,dcs): 
            nr,nc = r + dr, c + dc 
            if can_go(nr,nc): 
                push(nr,nc,steps[r][c]+1) 
    if visited[r2][c2]: 
        ans = steps[r2][c2] 
push(r1,c1,0) 
find_min() 

if ans == INT_MAX: 
    ans = -1 
print(ans)