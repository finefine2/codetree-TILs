N = int(input()) 
board = [list(map(int,input().split())) for _ in range(N)] 

M = N//2 

from collections import deque 
def bfs(sr,sc): 
    q = deque() 

    q.append((sr,sc)) 
    v[sr][sc] = 1 
    groups[-1].add((sr,sc)) 

    while q: 
        cr,cc = q.popleft() 
        for nr,nc in ((cr-1,cc),(cr+1,cc),(cr,cc-1),(cr,cc+1)): 
            if 0<=nr<N and 0<=nc<N and v[nr][nc] == 0 and board[cr][cc] == board[nr][nc]: 
                q.append((nr,nc)) 
                v[nr][nc] = 1 
                groups[-1].add((nr,nc)) 
ans = 0 
for k in range(4): 
    groups = [] 
    nums = [] 

    v = [[0]*N for _ in range(N)] 
    for r in range(N): 
        for c in range(N): 
            if v[r][c] == 0: 
                groups.append(set()) 
                nums.append(board[r][c]) 
                bfs(r,c) 
    CNT = len(nums) 
    for i in range(0,CNT-1): 
        for j in range(i+1,CNT): 
            point = (len(groups[i]) + len(groups[j]))*nums[i]*nums[j]
            for cr,cc in groups[i]: 
                for nr,nc in ((cr-1,cc),(cr+1,cc),(cr,cc-1),(cr,cc+1)): 
                    if (nr,nc) in groups[j]: 
                        ans += point
    if k == 3: 
        break 
    nboard = [x[:] for x in board] 
    for r in range(N): 
        nboard[M][r] = board[r][M] 
    for c in range(N): 
        nboard[c][M] = board[M][N-c-1] 

    for (sr,sc) in ((0,0),(0,M+1),(M+1,0),(M+1,M+1)): 
        for r in range(M): 
            for c in range(M): 
                nboard[sr+r][sc+c] = board[sr+M-c-1][sc+r] 
    board = nboard
print(ans)