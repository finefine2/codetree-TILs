N,M = tuple(map(int,input().split()))
board = [[0 for _ in range(N+1)] for _ in range(N+1)] 
visited = [False for _ in range(N+1)]
cnt = 0 

for _ in range(M): 
    x,y = tuple(map(int,input().split()))
    board[x][y] = 1 
    board[y][x] = 1

def dfs(v): 
    global cnt 
    for curr_v in range(1,N+1): 
        if board[v][curr_v] and not visited[curr_v]: 
            visited[curr_v] = True 
            cnt += 1 
            dfs(v) 
visited[1] = True
dfs(1) 

print(cnt)