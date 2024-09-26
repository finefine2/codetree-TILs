from collections import deque

N,M,C = tuple(map(int,input().split()))

# 0 road, 1 wall
board = [[1]*(N+2)] + [[1] + list(map(int,input().split())) +[1] for _ in range(N)] + [[1]*(N+2)]

cr,cc = tuple(map(int,input().split()))
start_pos = set()
dest_pos = {}
for i in range(M):
    sr,sc,er,ec = tuple(map(int,input().split()))
    start_pos.add((sr,sc))
    dest_pos[(sr,sc)] = (er,ec)

def bfs_find(sr,sc):
    q = deque()
    v = [[0] * (N+2) for _ in range(N+2)]

    v[sr][sc]=1
    q.append((sr,sc))
    tlst = []
    drs,dcs = [-1,1,0,0],[0,0,-1,1]
    while q:
        nq = deque()
        # cr,cc = q.popleft()
        for cr,cc in q:

            if (cr,cc) in start_pos:
                tlst.append([cr,cc])

            for dr,dc in zip(drs,dcs):
                nr,nc = cr + dr, cc + dc
                if v[nr][nc] == 0 and board[nr][nc] == 0:
                    nq.append((nr,nc))
                    v[nr][nc] = v[cr][cc] + 1
        if len(tlst) > 0:
            tlst.sort()
            er,ec = tlst[0]

            return er,ec,v[er][ec] - 1
        q = nq
    return 0,0,-1

# 해당 운전자가 정해진 목적지로 이동
def bfs(sr,sc,er,ec):
    q = deque()
    v = [[0] * (N+2) for _ in range(N+2)]

    v[sr][sc] = 1
    q.append((sr,sc))
    drs,dcs = [-1,1,0,0],[0,0,-1,1]

    while q:
        cr,cc = q.popleft()
        if (cr,cc) == (er,ec):
            return v[cr][cc] - 1

        for dr,dc in zip(drs,dcs):
            nr,nc = cr + dr, cc + dc

            if v[nr][nc] == 0 and board[nr][nc] == 0:
                q.append((nr,nc))
                v[nr][nc] = v[cr][cc] + 1

    return -1

# 승객 M 명에 대해서 다 조사를 하자
for _  in range(M):
    # 1. 현재 스타트지점에서 가장 가까운 승객을 찾는다
    sr,sc,dist = bfs_find(cr,cc)
    # 만약 도달할 수 없다면? (연료 부족땜에)
    if dist == -1 or dist > C:
        C = -1
        break
    # 그게 아니라면
    C -= dist
    # 들어가있는 승객 좌표도 삭제
    start_pos.remove((sr,sc))

    # 승객을 찾았으면 목적지까지
    er,ec = dest_pos[(sr,sc)]

    # 최단거리 발견하기 시작점 - 도착점간
    dist = bfs(sr,sc,er,ec)
    if dist == -1 or dist > C:
        C = -1
        break

    C += dist
    cr,cc = er,ec

print(C)