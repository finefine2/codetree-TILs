from collections import deque 

N,K,M = map(int,input().split()) 

board = [list(map(int,input().split())) for _ in range(N)] 

ans = 0 
s_pos = [] 
stone_pos = [(i,j) for i in range(N) for j in range(N) if board[i][j] == 1]

selected_stones = [] 
q = deque() 
visited = [[False for _ in range(N)] for _ in range(N)] 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

def can_go(r,c): 
    return in_range(r,c) and not board[r][c] and not visited[r][c] 

def bfs(): 
    while q : 
        r,c = q.popleft() 
        drs, dcs = [1,-1,0,0],[0,0,1,-1] 

        for dr, dc in zip(drs,dcs): 
            new_r, new_c = r + dr, c + dc 
            if can_go(new_r,new_c): 
                q.append((new_r, new_c)) 
                visited[new_r][new_c] = True 

def calc(): 
    for r,c in selected_stones: 
        board[r][c] = 0 
    for i in range(N): 
        for j in range(N): 
            visited[i][j] = False
    for r,c in s_pos: 
        q.append((r,c))
        visited[r][c] = True 

    bfs() 

    for r, c in selected_stones: 
        board[r][c] = 1 

    cnt = 0 
    for i in range(N): 
        for j in range(N): 
            if visited[i][j]: 
                cnt += 1
    return cnt 

def find_max(idx,cnt): 
    global ans 

    if idx == len(stone_pos): 
        if cnt == M: 
            ans = max(ans,calc()) 
        return 

    selected_stones.append(stone_pos[idx]) 
    find_max(idx+1, cnt+1) 
    selected_stones.pop() 

    find_max(idx+1,cnt) 
for _ in range(K): 
    r,c = map(int,input().split()) 
    s_pos.append((r-1,c-1))
find_max(0,0) 
print(ans)