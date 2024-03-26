N = int(input()) 
board = [list(map(int,input().split())) for _ in range(N)] 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

visited = [[0 for _ in range(N)] for _ in range(N)] 

# wall -> 0 
def can_go(r,c): 
    if not in_range(r,c): 
        return False 
    if board[r][c] == 0 or visited[r][c]: 
        return False 
    return True 
cnt = 0 
ans = []
def dfs(r,c): 
    global cnt 
    drs,dcs = [1,0,-1,0],[0,1,0,-1] 

    visited[r][c] = 1 
    for dr, dc in zip(drs,dcs): 
        new_r, new_c = r + dr, c + dc 

        if can_go(new_r,new_c): 
            visited[new_r][new_c] = 1 
            cnt += 1 
            dfs(new_r, new_c) 
for i in range(N): 
    for j in range(N): 
        if can_go(i,j): 
            visited[i][j] =1 
            cnt = 1 
            dfs(i,j) 
            ans.append(cnt) 
ans.sort() 

print(len(ans)) 
for a in ans: 
    print(a)