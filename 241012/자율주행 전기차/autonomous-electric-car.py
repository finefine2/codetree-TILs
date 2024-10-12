# 정해진 반경만 탐색하는 bfs
# 항상 최단거리 위주로 이동? -> bfs
from collections import deque
N,M,C = tuple(map(int,input().split()))
board = [[1] * (N+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(N)] + [[1] * (N+2)]
cr,cc = tuple(map(int,input().split())) # 전기차 시작위치 
start_pos = set()
dest_pos = {}

for m in range(1,M+1):
    sr,sc,er,ec = tuple(map(int,input().split()))
    start_pos.add((sr,sc)) # 출발위치 체크용
    dest_pos[(sr,sc)] = (er,ec) # 출발위치에 따른 목적지 저장용

def bfs(sr,sc,er,ec): # 출발지에서 목적지까지의 최단거리를 계산
    q = deque()
    v = [[0] * (N+2) for _ in range(N+2)]

    q.append((sr,sc))
    v[sr][sc] = 1
    while q:
        
        cr,cc = q.popleft()
        if (cr,cc) == (er,ec): # 도착해버린다면
            return v[cr][cc] - 1

        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr,nc = cr + dr, cc + dc
            if v[nr][nc] == 0 and board[nr][nc] == 0:
                q.append((nr,nc))
                v[nr][nc] = v[cr][cc] + 1
    return -1
# 손님을 태우기 위해 최단거리로 가는 것
def find_bfs(sr,sc):
    q = deque()
    v = [[0] * (N+2) for _ in range(N+2)]
    tlst = []

    q.append((sr,sc))
    v[sr][sc] = 1
    while q:
        # 동일반경 단위의 처리 
        nq = deque()
        for cr,cc in q:
            if (cr,cc) in start_pos: # 승객 위치에 도달한다면?
                tlst.append((cr,cc))
            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                nr,nc = cr + dr, cc + dc
                if v[nr][nc] == 0 and board[nr][nc] == 0: # 미방문 길
                    nq.append((nr,nc))
                    v[nr][nc] = v[cr][cc] + 1
        if len(tlst) > 0:
            tlst.sort() # 행,열 오름차순 정렬
            er,ec = tlst[0]

            return v[er][ec]-1,er,ec
        q = nq
    return -1,0,0 #못찾은 경우 
for _ in range(M):
    dist,sr,sc = find_bfs(cr,cc)
    if dist == -1 or dist > C: # 출발지를 하나도 못 찾았거나, 연료가 부족한 경우
        C = -1
        break

    C -= dist
    start_pos.remove((sr,sc))

    # 출발지에 지정된 목적지 탐색
    er,ec = dest_pos[(sr,sc)]
    dist = bfs(sr,sc,er,ec)
    if dist == -1 or dist > C: # 목적지 못찾거나 연료 부족할시
        C = -1
        break

    # 목적지까지 무사히 도착
    C += dist
    cr,cc = er,ec

print(C)