N,M,C = map(int,input().split())

board = [[1]*(N+2)] + [[1]+list(map(int,input().split()))+[1] for _ in range(N)] + [[1]*(N+2)]

cr,cc = map(int,input().split())

start_pos = set()
dest = {}

for _ in range(M):
    sr,sc,er,ec = map(int,input().split())
    start_pos.add((sr,sc))
    dest[(sr,sc)] = (er,ec)

from collections import deque
def bfs_find(cr,cc):
    q=deque()
    v = [[0] * (N+2) for _ in range(N+2)]

    q.append((cr,cc))
    v[cr][cc] = 1
    tlst = [] # 여러개를 담기 위해

    while q:
        nq = deque()
        for r,c in q:
            if (r,c) in start_pos:
                tlst.append((r,c))

            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                nr,nc = r + dr, c + dc
                if board[nr][nc] == 0 and v[nr][nc] == 0:
                    v[nr][nc] = v[r][c] + 1
                    nq.append((nr,nc))
        if len(tlst) > 0:
            tlst.sort()
            sr,sc = tlst[0]
            return sr,sc,v[sr][sc]-1
        q=nq
    return 0,0,-1

def bfs(sr,sc,er,ec):
    v =[[0]*(N+2) for _ in range(N+2)]
    q = deque()

    q.append((sr,sc))
    v[sr][sc] = 1

    while q:
        r,c = q.popleft()
        if (r,c) == (er,ec):
            return v[r][c] - 1
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr,nc = r + dr, c + dc
            if board[nr][nc] == 0 and v[nr][nc] == 0:
                v[nr][nc] = v[r][c] + 1
                q.append((nr,nc))
    return -1
for _ in range(M):
    sr,sc,dist = bfs_find(cr,cc)
    if dist == -1 or C < dist:
        C = -1
        break
    C -= dist 
    er,ec = dest[(sr,sc)]
    start_pos.remove((sr,sc))

    dist = bfs(sr,sc,er,ec)
    if dist == -1 or C < dist:
        C = -1
        break
    C += dist
    cr,cc = er,ec 
print(C)