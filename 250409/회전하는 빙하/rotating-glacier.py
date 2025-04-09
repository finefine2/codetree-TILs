from collections import deque
dir = [(1,0),(-1,0),(0,1),(0,-1)]
N, Q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(2**N)]
orderlist = list(map(int, input().split()))

def rotate(level):
    if level == 0: return
    n = len(graph)//(2**level)

    for i in range(n):
        for j in range(n):
            x = i*(2**level)
            y = j*(2**level)
            tempgraph = []
            for k in range(2**(level-1)):
                tempgraph.append(graph[x+k][y:y+2**(level-1)])
            for k in range(2**(level-1)):
                graph[x+k][y:y+2**(level-1)] = graph[x+2**(level-1)+k][y:y+2**(level-1)]
            for k in range(2**(level-1)):
                graph[x+2**(level-1)+k][y:y+2**(level-1)] = graph[x+2**(level-1)+k][y+2**(level-1):y+2**level]
            for k in range(2**(level-1)):
                graph[x+2**(level-1)+k][y+2**(level-1):y+2**level] = graph[x+k][y+2**(level-1):y+2**level]
            for k in range(2**(level-1)):
                graph[x+k][y+2**(level-1):y+2**level] = tempgraph[k]

def melt():
    tempgraph = {}
    for i in range(2**N):
        for j in range(2**N):
            if graph[i][j] == 0: continue
            cnt = 0
            for k in range(4):
                nx, ny = i+dir[k][0], j+dir[k][1]
                if 0<=nx<2**N and 0<=ny<2**N and graph[nx][ny]>0:
                    cnt += 1
            if cnt<3:
                tempgraph[i,j] = 0
    for x, y in tempgraph:
        graph[x][y] -= 1

def check():
    visited = [[False]*(2**N) for _ in range(2**N)]
    total = 0
    maxcnt = 0
    for i in range(2**N):
        for j in range(2**N):
            if graph[i][j] == 0:
                visited[i][j] = True
            elif not visited[i][j]:
                visited[i][j] = True
                q = deque([(i,j)])
                total += graph[i][j]
                cnt = 1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x+dir[k][0], y+dir[k][1]
                        if 0<=nx<2**N and 0<=ny<2**N and not visited[nx][ny] and graph[nx][ny]>0:
                            total += graph[nx][ny]
                            visited[nx][ny] = True
                            q.append((nx,ny))
                            cnt += 1
                maxcnt = max(cnt, maxcnt)
    print(total)
    print(maxcnt)

for rot in orderlist:
    rotate(rot)
    melt()
check()