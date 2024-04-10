import sys 
from collections import deque 

INT_MAX = sys.maxsize 
EMPTY = (-1,-1) 

N,M = tuple(map(int,input().split())) 
board = [list(map(int,input().split())) for _ in range(N)]

store_list = [] 
for _ in range(M): 
    r,c = tuple(map(int,input().split()))
    store_list.append((r-1,c-1)) 

people = [EMPTY] * M 
curr_t = 0 
# U L R D 
drs, dcs = [-1,0,0,1],[0,-1,1,0] 
step = [[0] * N for _ in range(N)] 
visited = [[False] * N for _ in range(N)] 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 
def can_go(r,c): 
    return in_range(r,c) and not visited[r][c] and board[r][c] != 2

def bfs(start_pos): 
    for i in range(N): 
        for j in range(N): 
            visited[i][j] = False
            step[i][j] = 0 
    q = deque() 
    q.append(start_pos) 
    sr, sc = start_pos
    visited[sr][sc] = True 
    step[sr][sc] = 0 

    while q: 
        r,c = q.popleft() 
        for dr, dc in zip(drs, dcs): 
            nr, nc = r + dr, c + dc 
            if can_go(nr,nc): 
                visited[nr][nc] = True 
                step[nr][nc] = step[r][c] + 1 
                q.append((nr,nc)) 

def simulate(): 
    # step1 - let those who stay in the grid move toward store direction 
    for i in range(M): 
        if people[i] == EMPTY or people[i] == store_list[i]: 
            continue 
        bfs(store_list[i]) 
        pr, pc = people[i] 
        min_dist = INT_MAX
        min_r, min_c = -1,-1 

        for dr, dc in zip(drs, dcs): 
            nr,nc = pr + dr, pc + dc 
            if in_range(nr,nc) and visited[nr][nc] and min_dist > step[nr][nc]:
                min_dist = step[nr][nc] 
                min_r, min_c = nr,nc 
        people[i] = (min_r, min_c) 
    for i in range(M): 
        if people[i] == store_list[i]: 
            pr, pc = people[i] 
            board[pr][pc] = 2
    if curr_t > M: 
        return 
    bfs(store_list[curr_t-1]) 

    min_dist = INT_MAX
    min_r, min_c = -1,-1 
    for i in range(N): 
        for j in range(N): 
            if visited[i][j] and board[i][j] == 1 and min_dist > step[i][j]: 
                min_dist = step[i][j]
                min_r, min_c = i,j 
    people[curr_t - 1] = (min_r, min_c) 
    board[min_r][min_c] = 2 
def end(): 
    for i in range(M): 
        if people[i] != store_list[i]: 
            return False 
    return True 
while True: 
    curr_t += 1
    simulate() 
    if end(): 
        break 
print(curr_t)