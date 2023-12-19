N = int(input()) 

graph = [] 

for _ in range(N): 
    graph.append(list(map(int,input().split())))

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def in_range(x,y): 
    return 0 <= x < N and 0 <= y < N 

ans = 0 
for x in range(N): 
    for y in range(N): 
        cnt = 0
        for dx, dy in zip(dxs, dys): 
            nx,ny = x + dx, y + dy
            if in_range(nx,ny) and graph[nx][ny] == 1: 
                cnt += 1 
        if cnt >= 3: 
            ans += 1
print(ans)