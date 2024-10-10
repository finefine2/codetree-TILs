from collections import deque 
N = int(input()) 
board = [list(map(int,input().split())) for _ in range(N)] 

ans = 0 
def rotate(board): 
    nboard = [x[:] for x in board] 
    M = N // 2 
    # counter clockwise rot for cross 
    for r in range(N): 
        nboard[r][M] = board[M][N-r-1] 
    for c in range(N): 
        nboard[M][c] = board[c][M] 
    
    # clockwise rot for square region 
    for sr,sc in ((0,0),(0,M+1),(M+1,0),(M+1,M+1)): 
        for r in range(M): 
            for c in range(M): 
                nboard[sr+r][sc+c] = board[sr+M-c-1][sc+r] 
    return nboard

def in_range(r,c): 
    return 0<=r<N and 0<=c<N 

def find_bfs(r,c): 
    q = deque() 

    v[r][c] = 1 
    q.append((r,c)) 
    groups[-1].add((r,c)) 

    while q: 
        cr,cc = q.popleft() 

        for nr,nc in ((cr-1,cc),(cr,cc+1),(cr+1,cc),(cr,cc-1)): 
            if in_range(nr,nc) and v[nr][nc] == 0 and board[nr][nc] == board[cr][cc]: 
                q.append((nr,nc)) 
                groups[-1].add((nr,nc)) 
                v[nr][nc] = 1 
ans = 0
for k in range(4): 
    groups = [] 
    nums = [] 
    v = [[0] * N for _ in range(N)] 

    for r in range(N): 
        for c in range(N): 
            if v[r][c] == 0: 
                groups.append(set()) 
                nums.append(board[r][c]) 
                find_bfs(r,c) 
    CNT = len(nums) 

    for i in range(0,CNT-1): 
        for j in range(i+1,CNT): 
            point = (len(groups[i])+len(groups[j])) * nums[i] * nums[j] 
            for cr,cc in groups[i]: 
                for nr,nc in ((cr-1,cc),(cr,cc-1),(cr+1,cc),(cr,cc+1)): 
                    if (nr,nc) in groups[j]: 
                        ans += point
    if k == 3: 
        break 
    board = rotate(board) 

print(ans)