N,M = map(int,input().split()) 

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

visited = [False for _ in range(N+1)] 

v_cnt = 0 

def dfs(v): 
    global v_cnt
    for curr_v in range(1,N + 1): 
        if graph[v][curr_v] and not visited[curr_v]: 
            visited[curr_v] = True 
            v_cnt += 1
            dfs(curr_v)
for i in range(M): 
    x,y = map(int,input().split()) 
    graph[x][y] = 1
    graph[y][x] = 1 

visited[1] = True 
dfs(1) 
print(v_cnt)