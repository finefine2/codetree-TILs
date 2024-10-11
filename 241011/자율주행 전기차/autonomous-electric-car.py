# 정해진 반경만 탐색하는 bfs
N,M,C = tuple(map(int,input().split()))
board = [[1] * (N+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(N)] + [[1] * (N+2)]
cr,cc = tuple(map(int,input().split())) # 택시 시작위치

start_pos = set()
dest_pos = {}
for m in range(M):
    sr,sc,er,ec = tuple(map(int,input().split()))
    start_pos.add((sr,sc)) # 출발위치 쳌
    dest_pos[(sr,sc)] = (er,ec) # 출발위치에 따른 목적지

from collections import deque

# 시작지점에서 start_pos에 있는 좌표를 찾으면(같은거리의 출발지 모두 찾기 )
def find_bfs(sr,sc):
    q = deque()
    v = [[0] * (N+2) for _ in range(N+2)]
    tlst = []

    q.append((sr,sc))
    v[sr][sc] = 1

    while q:
        # 동일반경 단위 처리
        nq = deque()
        for cr,cc in q:
            if (cr,cc) in start_pos:
                tlst.append([cr,cc])
            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                nr,nc = cr + dr, cc + dc
                if v[nr][nc] == 0 and board[nr][nc] == 0: # 미방문 길이면
                    nq.append((nr,nc))
                    v[nr][nc] = v[cr][cc] + 1
        # 동일 거리 처리 후 tlst에 좌표가 있는 경우 종료
        if len(tlst) > 0:
            tlst.sort()
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
        if (cr,cc) == (er,ec): # 목적지를 찾은 경우
            return v[cr][cc] - 1
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr,nc = cr + dr, cc + dc
            if v[nr][nc] == 0 and board[nr][nc] == 0: # 미방문 길이라면
                q.append((nr,nc))
                v[nr][nc] = v[cr][cc] + 1
    # 목적지를 찾지 못한다면
    return -1

for _ in range(M):
    # 현재 위치로부터 제일 가까운 승객 찾기 (같은거리면 행/열 작은순)
    sr,sc,dist = find_bfs(cr,cc)
    if dist == -1 or dist > C: # 못찾았거나 연료가 부족할 경우
        C = -1
        break
    C -= dist
    start_pos.remove((sr,sc))

    # 출발지에서 목적지 탐색
    er,ec = dest_pos[(sr,sc)]
    dist = bfs(sr,sc,er,ec)
    if dist == -1 or dist > C: # 못찾거나 연료 부족
        C = -1
        break

    # 무사 도착시
    C += dist
    cr,cc = er,ec

print(C)