N,M,C = map(int,input().split())
board = [[1] * (N+2)] + [[1]+list(map(int,input().split()))+[1] for _ in range(N)] + [[1] * (N+2)]

cr,cc = map(int,input().split())
dests = {}
start_pos = set()
for m in range(1,M+1):
    sr,sc,er,ec = map(int,input().split())
    start_pos.add((sr,sc))
    dests[(sr,sc)] = (er,ec)

from collections import deque
def bfs_find(sr,sc):
    v = [[0] * (N+2) for _ in range(N+2)]
    q = deque()

    q.append((sr,sc))
    v[sr][sc] = 1
    tlst = []
    while q:
        nq = deque()

        for cr,cc in q:
            if (cr,cc) in start_pos:
                tlst.append((cr,cc))

            for dr,dc in ((-1,0),(0,1),(1,0),(0,-1)):
                nr,nc = cr + dr, cc + dc
                if v[nr][nc] == 0 and board[nr][nc] == 0:
                    nq.append((nr,nc))
                    v[nr][nc] = v[cr][cc] + 1
        if len(tlst) > 0:
            tlst.sort(key=lambda x: (x[0],x[1]))
            er,ec = tlst[0]
            return er,ec,v[er][ec]-1
        q = nq
    return 0,0,-1

def bfs(sr,sc,er,ec):
    q = deque()
    v = [[0] * (N+2) for _ in range(N+2)]

    q.append((sr,sc))
    v[sr][sc] = 1

    while q:
        cr,cc = q.popleft()
        if (cr,cc) == (er,ec):
            return v[cr][cc] -1

        for dr,dc in ((-1,0),(0,1),(1,0),(0,-1)):
            nr,nc = cr + dr, cc + dc
            if v[nr][nc] == 0 and board[nr][nc] == 0:
                q.append((nr,nc))
                v[nr][nc] = v[cr][cc] + 1
    return -1


while True:
    # 출발지를 찾아본다
    sr,sc,dist = bfs_find(cr,cc)
    # 만약 모두를 데려다주지 못하면 break
    if dist == -1 or dist > C:
        C = -1 
        break
    # 데려다줄 수 잇따면?
    # 출발지에서 목적지까지의 최단거리를 계산한다
    C -= dist
    start_pos.remove((sr,sc))

    er,ec = dests[(sr,sc)]
    dist = bfs(sr,sc,er,ec)

    if dist == -1 or dist > C:
        C = - 1
        break

    # 데려다줄 수 있다면
    C += dist
    cr,cc = er,ec
print(C)