from collections import deque 
from itertools import combinations 

N, K, U, D = map(int,input().split())
board = [] 
points = [] 
for i in range(N): 
    tmp = list(map(int,input().split()))
    board.append(tmp) 
    for j in range(N):
        points.append((i,j)) 
start_points = combinations(points, K) 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N

def can_go(r,c,num): 
    if in_range(r,c) and not visited[r][c] and U <= abs(num - board[r][c]) <= D and num != board[r][c]: 
        return True 
def bfs(): 
    drs,dcs = [1,0,-1,0],[0,1,0,-1] 
    global q, num 
    while q: 
        r,c = q.popleft() 
        for dr,dc in zip(drs,dcs): 
            new_r, new_c = r + dr, c + dc 
            if can_go(new_r, new_c, board[r][c]): 
                visited[new_r][new_c] = True 
                num += 1 
                q.append((new_r,new_c)) 
ans = 0 

for start in start_points: 
    num = 0 
    q = deque() 
    visited = [[False for _ in range(N)] for _ in range(N)] 

    for i,j in start: 
        if not visited[i][j]: 
            visited[i][j] = True 
            q.append((i,j)) 
            num += 1 
            bfs() 
    ans = max(num,ans) 
print(ans)