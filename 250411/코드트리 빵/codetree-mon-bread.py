drs,dcs = [-1,0,0,1],[0,-1,1,0]
N,M = map(int,input().split())
# 0 empty 1 basecamp
board = [[1] * (N+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(N)] + [[1]*(N+2)] 


basecamp = set()

for r in range(1,1+N):
    for c in range(1,1+N):
        if board[r][c] == 1:
            basecamp.add((r,c))
            board[r][c] = 0

stores = {}
for m in range(1,1+M):
    r,c = map(int,input().split())
    stores[m] = (r,c)  
    
from collections import deque
def find(sr,sc,dests):
    q = deque() 
    v = [[0] * (N+2) for _ in range(N+2)] 
    
    tlst = [] 
    q.append((sr,sc)) 
    v[sr][sc] = 1 
    while q: 
        nq = deque() 
        for cr,cc in q: 
            if (cr,cc) in dests: 
                tlst.append((cr,cc)) 
            else: 
                for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)): 
                    nr,nc = cr + dr, cc + dc 
                    if v[nr][nc] == 0 and board[nr][nc] == 0: 
                        nq.append((nr,nc)) 
                        v[nr][nc] = v[cr][cc] + 1 
        if len(tlst) > 0: 
            tlst.sort() 
            return tlst[0] 
        q = nq 
    return -1 
    
# 정확히 1,2,3 순서로 진행

from collections import deque
def solve():
    q = deque()
    arrived = [0] * (M+1)
    time = 1

    while q or time == 1:
        nq = deque() 
        alst = [] 
        for cr,cc,m in q:
            # [1] 격자 내부 사람들 모두 본인이 가고싶은 편의점 방향으로 1칸 움직인다 
            # 최단거리로 움직이는 게 상좌우하 우선순위 
            if arrived[m] == 0:
                nr,nc=find(stores[m][0],stores[m][1],set(((cr-1,cc),(cr+1,cc),(cr,cc-1),(cr,cc+1))))
                if (nr,nc) == stores[m]: 
                    arrived[m] = time 
                    alst.append((nr,nc)) 
                else: 
                    nq.append((nr,nc,m)) 
        q = nq

        # [2]편의점에 도착하면 해당 편의점에 멈추고, 해당 편의점은 벽으로 처리 

        if len(alst) > 0: 
            for ar,ac in alst: 
                board[ar][ac] = 1 
        
    # [3] 현재 시간이 t분이고, t <= M 이라면 
    # t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스캠프에 들어감 
    # 최단거리 이동ㅇ 
    
    # 가장 가까이 있는 베이스 캠프 우선순위 
    # 행이 작고 열이 작다 
        
    # 이때부터 이 칸은 벽으로 처리 
        if time <= M: 
            sr,sc = stores[time] 
            er,ec = find(sr,sc,basecamp) 
            basecamp.remove((er,ec)) 
            board[er][ec] = 1 
            q.append((er,ec,time)) 
    
        time += 1 
    return max(arrived)
ans = solve() 
print(ans) 