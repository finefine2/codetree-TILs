N = int(input()) 

board = [list(map(int,input().split())) for _ in range(N)] 

cnt = 0 
people_nums = [] 

visited = [[0] * N for _ in range(N)] 

def in_range(r,c): 
    return 0<=r<N and 0<=c<N
def dfs(r,c): 
    global cnt 
    drs,dcs = [0,1,0,-1],[1,0,-1,0]

    visited[r][c] = 1 
    for dr,dc in zip(drs,dcs): 
        nr,nc = r + dr, c + dc 
        if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] == 1: 
            visited[nr][nc] = 1 
            cnt += 1 
            dfs(nr,nc) 

for r in range(N): 
    for c in range(N): 
        if not visited[r][c] and board[r][c] == 1: 
            cnt = 1 
            visited[r][c] = 1 
            dfs(r,c) 
            people_nums.append(cnt) 
people_nums.sort() 
print(len(people_nums))
for p in people_nums: 
    print(p)