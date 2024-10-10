# 정해진 반경만 탐색하는 bfs
# 항상 최단거리 위주로 이동? -> bfs

N,M,C = tuple(map(int,input().split()))
board = [[1] * (N+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(N)] + [[1] * (N+2)]

# 전기차의 출발지점
cr,cc = tuple(map(int,input().split()))
start_pos = set()
dest_pos = {}
for m in range(M):
    sr,sc,er,ec = tuple(map(int,input().split()))
    start_pos.add((sr,sc)) # 출발위치 체크용
    dest_pos[(sr,sc)] = (er,ec) # 출발위치에 따른 목적지

from collections import deque
def bfs_find(sr,sc):
    q = deque()
    v = [[0] * (N+2) for _ in range(N+2)]
    tlst = []

    q.append((sr,sc))
    v[sr][sc] =1

    while q:
        # 동일반경 단위의 처리 진행
        nq = deque()
        for cr,cc in q:
            if (cr,cc) in start_pos:
                tlst.append([cr,cc])
            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                nr,nc = cr + dr, cc + dc
                if v[nr][nc] == 0 and board[nr][nc] == 0: # 미방문 길이면 (벽이 아니면)
                    nq.append((nr,nc))
                    v[nr][nc] = v[cr][cc] + 1
        # 동일거리 처리후 tlst에 좌표가 있으면 종료
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
        if (cr,cc) == (er,ec): # 목적지 도착
            return v[cr][cc] - 1
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr,nc = cr + dr, cc + dc
            if v[nr][nc] == 0 and board[nr][nc] == 0:
                q.append((nr,nc))
                v[nr][nc] = v[cr][cc] + 1
    return -1

# 정답은 남은 연료량 도착못하면 -1출력 (m명 모두에 대해 처리 )
for _ in range(M):
    #[1] 출발지를 검색(같은거리면 행/열 작은순)
    sr,sc,dist = bfs_find(cr,cc)
    if dist == -1 or dist > C: # 출발지를 하나도 못 찾았거나 연료가 부족시
        C = -1
        break
    C -= dist
    start_pos.remove((sr,sc))

    # 출발지에서 목적지 탐색
    er,ec = dest_pos[(sr,sc)]
    dist = bfs(sr,sc,er,ec)
    if dist == -1 or dist > C:
        C = -1
        break
    # 목적지까지 무사도착
    C += dist
    cr,cc = er,ec
print(C)