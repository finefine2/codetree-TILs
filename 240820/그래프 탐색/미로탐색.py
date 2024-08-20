from collections import deque
N, M = tuple(map(int,input().split()))
board = [list(map(int,input())) for _ in range(N)]

def in_range(r,c):
    return 0<=r<N and 0<=c<M
# consider start pos and end pos simultaneously
# 4 방향 탐색
drs, dcs = [0,1,0,-1],[1,0,-1,0]
def bfs(sr,sc,er,ec):
    # q초기데이터 삽입
    q = deque()
    q.append((sr,sc))
    visited = [[0] * M for _ in range(N)]
    visited[sr][sc] = 1

    while q:
        cr, cc = q.popleft()
        # 종료조건?
        # 끝 지점에 도달하면 종료
        if (cr,cc) == (er,ec):
            return visited[er][ec]
        for dr,dc in zip(drs,dcs):
            nr,nc = cr + dr, cc + dc
            if in_range(nr,nc) and visited[nr][nc] == 0 and board[nr][nc] == 1:
                q.append((nr,nc))
                visited[nr][nc] = visited[cr][cc] + 1
ans = bfs(0,0,N-1,M-1)

print(ans)
