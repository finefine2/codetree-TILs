# 동일반경까지만 탐색하는 bfs 
# q 그리고 nq 의 활용법

N,M = tuple(map(int,input().split()))
board = [[1] * (N+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(N)] + [[1] * (N+2)]

# basecamp
basecamp = set()
for r in range(1,N+1):
    for c in range(1,N+1):
        if board[r][c] == 1:
            basecamp.add((r,c))
            board[r][c] =0

stores = {} # convenient store
for m in range(1,M+1):
    r,c = tuple(map(int,input().split()))
    stores[m] = (r,c)

from collections import deque

def find(sr,sc,dests):
    # 시작좌표에서 목적지들중 최단거리 동일반경 리스트를 모두 찾기
    q = deque()
    v = [[0] * (N+2) for _ in range(N+2)]
    tlst = []

    q.append((sr,sc))
    v[sr][sc] = 1
    while q:
        # 동일 반경을 탐색
        nq = deque()
        for cr,cc in q:
            if (cr,cc) in dests: # 목적지 찾음 -> 더 뻗어나갈 필요 없음
                tlst.append((cr,cc))
            else:
                # 4방향, 미방문, 벽이 아니면 board[][] == 0
                for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                    nr,nc = cr + dr, cc + dc
                    if v[nr][nc] == 0 and board[nr][nc] == 0:
                        nq.append((nr,nc))
                        v[nr][nc] = v[cr][cc] + 1
        # 목적지를 찾았다면 (여러개일지도) 리턴)
        if len(tlst) > 0:
            tlst.sort() # 행열 오름차순
            return tlst[0]
        q= nq
    return -1
def solve():
    q = deque()
    time = 1
    arrived = [0] * (M+1) # 0이면 미도착, >0이면 도착시간
    while q or time == 1: # 처음 또는 q에 데이터가 있는 동안(이동할 사람이 있는 동안)
        nq = deque()
        alst = []
        # 1. 모두 편의점 방향으로 최단거리 이동 (이번 time만, 같은 반경)
        for cr,cc,m in q:
            if arrived[m] == 0: # 도착하지 않은 사람만 처리
                # 편의점방향 최단거리 (우선순위) 한 칸 이동
                # 편의점에서 시작, 현재위치에서 상/하/좌/우 -> dests(set)
                sr,sc = stores[m]
                nr,nc = find(sr,sc,set(((cr-1,cc),(cr+1,cc),(cr,cc-1),(cr,cc+1))))
                if (nr,nc) == (sr,sc): # 최종 편의점에 도착
                    arrived[m] = time
                    alst.append((nr,nc)) #통행금지는 모두 이동한 다음에 처리할 것
                else:
                    nq.append((nr,nc,m)) # 계속 이도 ㅇ
        q = nq
        # 2. 편의점 도착처리 -> 이동불가처리
        if len(alst) > 0:
            for ar,ac in alst:
                board[ar][ac] = 1 # 이동불가
        # 3. 시간번호의 멤버가 베이스캠프로 순간이동
        if time <= M:
            sr,sc = stores[time]
            er,ec = find(sr,sc,basecamp) # 가장 가까운(우선순위 높은) 베이스 캠프 선택
            basecamp.remove((er,ec))
            board[er][ec] = 1 # 이동불가
            q.append((er,ec,time)) # 베이스캠프에서 이동시작
        time += 1
    return max(arrived)
ans = solve()
print(ans)