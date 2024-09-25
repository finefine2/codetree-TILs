N,M,C = tuple(map(int,input().split()))
board = [[1] * (N+2)] + [[1] + list(map(int,input().split())) +[1] for _ in range(N)] + [[1] * (N+2)]

start_pos = set()
dest_pos = {}
cr,cc = tuple(map(int,input().split()))
for i in range(M):
    sr,sc,er,ec = tuple(map(int,input().split())) # 택시 시작(현재)위치
    start_pos.add((sr,sc))# 출발위치 체크용
    dest_pos[(sr,sc)]=(er,ec)# 출발위치에 따른 목적지

from collections import deque
# 시작지점에서 start_pos에 있는 좌표를 찾으면(같은거리의 출발지 모두 찾기)
def bfs_find(sr,sc):
    q = deque()
    v = [[0] * (N+2) for _ in range(N+2)]

    tlst = []
    q.append((sr,sc))
    v[sr][sc] = 1

    drs,dcs = [-1,1,0,0],[0,0,-1,1]
    while q:
        nq = deque()
        for cr,cc in q:
            if (cr,cc) in start_pos:
                tlst.append([cr,cc])
        # 동일반경 단위의 처리진행
            for dr,dc in zip(drs,dcs):
                nr,nc = cr + dr, cc + dc
                # not visited and not a wall
                if v[nr][nc] == 0 and board[nr][nc]==0:
                    nq.append((nr,nc))
                    v[nr][nc] = v[cr][cc] + 1
        # 동일거리 처리후 tlst에 좌표가 있는경우 종료
        if len(tlst) > 0:
            # 행/열 오름차순 정렬
            tlst.sort()
            er,ec = tlst[0]
            return er,ec,v[er][ec]-1
        q = nq
         # 못찾은 경우
    return 0,0,-1

def bfs(sr,sc,er,ec):
    q = deque()
    v = [[0] * (N+2) for _ in range(N+2)]

    q.append((sr,sc))
    v[sr][sc] = 1
    drs,dcs = [-1,1,0,0],[0,0,-1,1]
    while q:
        cr,cc = q.popleft()
  # 목적지를 찾은경우
        if (cr,cc) == (er,ec):
            return v[cr][cc] -1
        for dr,dc in zip(drs,dcs):
            nr,nc = cr + dr, cc + dc
           # 미방문 길이면(벽이아니면)
            if v[nr][nc] == 0 and board[nr][nc] == 0:
                q.append((nr,nc))
                v[nr][nc] = v[cr][cc] + 1
    # 목적지를 찾지 못한 경우
    return -1

# 정답은 남은 연료량, 도착못하면 -1출력 (M명에대해서 처리)
for _ in range(M):
    sr,sc,dist = bfs_find(cr,cc)
    # [1] 출발지를 검색(같은 거리면 행/열 작은 순으로)
    # 출발지를 하나도 못 찾았거나 연료가 부족한 경우
    if dist == -1 or dist > C:
        C = -1
        break
    C -= dist
    start_pos.remove((sr,sc))
    # [2] 출발지에서 목적지 탐색
    er,ec = dest_pos[(sr,sc)]
    dist = bfs(sr,sc,er,ec)
    # 목적지 못찾거나 연료 부족시
    if dist == -1 or dist > C:
        C = -1
        break

    # [3] 목적지까지 무사히 도착
    C += dist
    cr,cc = er,ec
print(C)