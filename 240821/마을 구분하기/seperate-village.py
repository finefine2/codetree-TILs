N = int(input())
board = [list(map(int,input().split())) for _ in range(N)] 
visited = [[False for _ in range(N)] for _ in range(N)] 

num = 0 
nums = []

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

def can_go(r,c): 
    if not in_range(r,c): 
        return False
    if visited[r][c] or board[r][c] == 0: 
        return False
    return True 

def dfs(r,c): 
    global num 
    drs,dcs = [0,1,0,-1], [1,0,-1,0] 
    for dr,dc in zip(drs,dcs): 
        nr,nc = r + dr, c + dc 
        if can_go(nr,nc): 
            visited[nr][nc] = True 
            num += 1 
            dfs(nr,nc) 

for i in range(N): 
    for j in range(N): 
        if can_go(i,j): 
            visited[i][j] = True 
            num = 1 
            dfs(i,j) 
            nums.append(num) 

nums.sort() 
print(len(nums)) 
for i in range(len(nums)): 
    print(nums[i])