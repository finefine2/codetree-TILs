from collections import deque 

N = int(input()) 
board = [list(map(int,input().split())) for _ in range(N)] 

def in_range(r,c): 
    return 0<=r<N and 0<=c<N 

def rotate(arr): 
    narr = [x[:] for x in arr] 
    N = len(arr) 
    M = N // 2
    # 십자 반시계 90도 
    for r in range(N): 
        narr[r][M] = arr[M][N-r-1]

    for c in range(N): 
        narr[M][c] = arr[c][M]

    # 4개 정사각형 90도 
    for sr,sc in ((0,0),(0,M+1),(M+1,0),(M+1,M+1)): 
        for r in range(M): 
            for c in range(M): 
                narr[sr+r][sc+c] = arr[sr+M-c-1][sc+r]

    return narr 

def bfs_find(r,c): 
    q = deque() 

    q.append((r,c)) 
    v[r][c] = 1

    groups[-1].add((r,c)) 
    while q: 
        cr,cc = q.popleft() 
        for dr,dc in zip(drs,dcs): 
            nr,nc = cr + dr, cc + dc
            if in_range(nr,nc) and v[nr][nc] == 0 and board[nr][nc] == board[cr][cc]: 
                groups[-1].add((nr,nc)) 
                v[nr][nc] = 1 
                q.append((nr,nc)) 
    
ans = 0 

for k in range(4): 
    nums = [] 
    groups = []
    v = [[0] * N for _ in range(N)] 
    drs,dcs = [-1,1,0,0],[0,0,-1,1]
    for r in range(N): 
        for c in range(N): 
            if v[r][c] == 0: 
                groups.append(set()) 
                nums.append(board[r][c]) 
                bfs_find(r,c) 

    CNT = len(nums) 
    for i in range(CNT-1):
        for j in range(i+1,CNT):
            point = (len(groups[i])+len(groups[j]))*nums[i]*nums[j]
            for cr,cc in groups[i]: 
                for dr,dc in zip(drs,dcs): 
                    nr,nc = cr + dr, cc + dc 
                    if (nr,nc) in groups[j]: 
                        ans += point 

    if k == 3: break 

    board = rotate(board) 

print(ans)