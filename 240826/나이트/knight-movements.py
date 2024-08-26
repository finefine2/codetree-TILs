from collections import deque

N = int(input())
r1,c1,r2,c2 = tuple(map(int,input().split()))
r1 -= 1
r2 -= 1
c1 -= 1
c2 -= 1
board = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def in_range(r,c):
    return 0<=r<N and 0<=c<N

def bfs():
    drs,dcs = [2,2,1,1,-2,-2,-1,-1], [1,-1,2,-2,1,-1,2,-2]
    while q:
        r,c = q.popleft()
        for dr,dc in zip(drs,dcs):
            nr,nc = r + dr, c + dc
            if in_range(nr,nc) and not visited[nr][nc]:
                q.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1
q = deque()
q.append((r1,c1))
visited[r1][c1] = 1
bfs()
if visited[r2][c2] == 0:
    print(-1)
else:
    print(visited[r2][c2]-1)