# 벽- 차가 지나갈 수 없고 
# 승객 - m 명 

# 승객을 태우러 가거나 태운 뒤 목적지로 이동할 때 항상 최단거리로 이동 
# 한 칸 이동당 배터리 -1 
# 승객을 목적지로 무사히 데려다주면 배터리 양 충전 

# 이동 중 배터리를 다 쓰면 그 즉시 종료 
# 만일 승객을 목적지로 이동시킨 뒤 배터리가 동시에 소모되면 소모한 배터리의 두 배만큼 충전되어 다시 운행 재개 

# 여러명의 승객 중 현재 위치에서 가장 가까운 승객을 먼저 태움 
# 여러명이라면 가장 위, 왼쪽에 있는 승객을 태움 ( 행, 열이 작은 순 ) 
from collections import deque
N,M,C = tuple(map(int,input().split())) 
board = [[1] * (N+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(N)] + [[1] * (N+2)] 
cr,cc = tuple(map(int,input().split())) 
start_pos = set() 
dest_pos = {} 
for m in range(1,M+1): 
    sr,sc,er,ec = tuple(map(int,input().split())) 
    start_pos.add((sr,sc)) 
    dest_pos[(sr,sc)] = (er,ec) 

def bfs_find(sr,sc): 
    q = deque() 
    v = [[0] * (N+2) for _ in range(N+2)] 

    tlst = [] 
    q.append((sr,sc)) 
    v[sr][sc] = 1 
    while q: 
        nq = deque() # 동일 반경 탐색한다 
        for cr,cc in q: 
            if (cr,cc) in start_pos: # 만약 승객을 태웠다면 
                tlst.append((cr,cc)) 
            for dr,dc in ((-1,0),(0,1),(1,0),(0,-1)): 
                nr,nc = cr + dr, cc + dc 
                if v[nr][nc] == 0 and board[nr][nc] == 0: # 미방문 + 벽 
                    nq.append((nr,nc)) 
                    v[nr][nc] = v[cr][cc] + 1 
        if len(tlst) > 0: 
            tlst.sort() 
            er,ec = tlst[0] 
            return er,ec,v[er][ec] - 1
        q = nq 
    return 0,0,-1 
def bfs(sr,sc,er,ec): 
    q = deque() 
    v = [[0] * (N+2) for _ in range(N+2)] 

    v[sr][sc] = 1 
    q.append((sr,sc)) 
    while q: 
        cr,cc = q.popleft() 
        if (cr,cc) == (er,ec): 
            return v[cr][cc] - 1 
        for dr,dc in ((-1,0),(0,1),(1,0),(0,-1)): 
            nr,nc = cr + dr, cc + dc 
            if v[nr][nc] == 0 and board[nr][nc] == 0: 
                v[nr][nc] = v[cr][cc] + 1 
                q.append((nr,nc)) 
    return -1 
for _ in range(M): 
    # 1 첫 승객을 태울 위치를 찾는다 
    sr,sc,dist = bfs_find(cr,cc)
    if dist == -1 or dist > C: 
        C = -1 
        break 
    # 승객을 태웠다면 연료 감소 + 승객 좌표 삭제 
    C -= dist 
    start_pos.remove((sr,sc)) 

    # 2 승객을 태우고 목적지로 이동한다 
    er,ec = dest_pos[(sr,sc)] 
    dist = bfs(sr,sc,er,ec) # 최단거리로 간다 
    if dist == -1 or dist > C: 
        C = -1 
        break 
    
    # 3 승객을 무사히 목적지로 보냈다면 
    C += dist 
    cr,cc = er,ec 
print(C)