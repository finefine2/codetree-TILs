from collections import deque

N,M = tuple(map(int,input().split()))
r,c,d = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]


def in_range(r,c):
    return 0<=r<N and 0<=c<M

def can_move(r,c):
    return board[r][c] == 0
def bfs():
    drs,dcs = [-1,0,1,0],[0,1,0,-1]

    while q:
        r,c = q.popleft()
        for dr,dc in zip(drs,dcs):
            nr,nc = r + dr, c + dc
            if in_range(nr,nc) and can_move(nr,nc):
                visited[nr][nc] = 1
                q.append((nr,nc))

q = deque()
q.append((r,c))
visited[r][c] = 1
bfs()
ans = sum(visited[i][j]
          for i in range(N)
          for j in range(M))
print(ans)