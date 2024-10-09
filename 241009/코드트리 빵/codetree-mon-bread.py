from collections import deque
N,M = tuple(map(int,input().split())) 
board = [[1] * (N+2)] + [[1] + list(map(int,input().split())) + [1] for _ in range(N)] + [[1]*(N+2)] 

basecamp = set() 
for r in range(1,N+1): 
    for c in range(1,N+1): 
        if board[r][c] == 1: 
            basecamp.add((r,c)) 
            board[r][c] = 0 
stores = {} 
for m in range(1,M+1): 
    r,c = tuple(map(int,input().split())) 
    stores[m] = (r,c) 
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
            for dr,dc in ((-1,0),(0,-1),(0,1),(1,0)): 
                nr,nc = cr + dr, cc+ dc 
                if v[nr][nc] == 0 and board[nr][nc] == 0: 
                    nq.append((nr,nc)) 
                    v[nr][nc] = v[cr][cc] + 1 
        if len(tlst) > 0:
            tlst.sort() 
            return tlst[0] 
        q = nq 
    return -1

def solve(): 
    arrived = [0] * (M+1) 
    q = deque() 

    alst = [] 
    time = 1 

    while q or time == 1: 
        nq = deque() 
        for cr,cc,m in q: 
            if arrived[m] == 0:
                sr,sc = stores[m] 
                nr,nc = find(sr,sc,set(((cr-1,cc),(cr,cc-1),(cr,cc+1),(cr+1,cc))))
                if (nr,nc) == (sr,sc):
                    arrived[m] = time 
                    alst.append((nr,nc))
                else: 
                    nq.append((nr,nc,m)) 
        q = nq 

        if len(alst) > 0: 
            for ar,ac in alst: 
                board[ar][ac] = 1 

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