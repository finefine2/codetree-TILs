drs,dcs = [-1,0,1,0],[0,1,0,-1] 

N,M,Q = map(int,input().split())

board = [[2] * (N+2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(N)] + [[2] * (N+2)] 

units = {} 

init_k = [0] * (M+1) 

for m in range(1,M+1): 
    sr,sc,h,w,k = map(int,input().split()) 
    units[m] = [sr,sc,h,w,k] 
    init_k[m] = k 
from collections import deque 

def push_unit(start,d): 
    q = deque()
    pset = set() 
    damage = [0]* (M+1) 

    q.append(start) 
    pset.add(start) 

    while q: 
        cur = q.popleft() 
        cr,cc,h,w,k = units[cur] 

        nr,nc = cr + drs[d], cc + dcs[d] 
        for r in range(nr,nr+h): 
            for c in range(nc,nc+w): 
                if board[r][c] == 2: 
                    return 
                if board[r][c] == 1: 
                    damage[cur] += 1 
        for idx in units: 
            if idx in pset: continue 
            tr,tc,th,tw,tk = units[idx] 

            if nr<=tr+th-1 and nr+h-1 >= tr and tc<=nc+w-1 and nc<=tc+tw-1: 
                q.append(idx) 
                pset.add(idx) 
    damage[start] = 0 

    for idx in pset: 
        sr,sc,h,w,k = units[idx] 
        if damage[idx] >= k: 
            units.pop(idx) 
        else: 
            nr,nc = sr + drs[d], sc + dcs[d] 
            units[idx] = [nr,nc,h,w,k-damage[idx]] 

for _ in range(Q): 
    idx,d = map(int,input().split()) 
    if idx in units: 
        push_unit(idx,d) 
ans = 0 
for idx in units: 
    ans += init_k[idx] - units[idx][4] 
print(ans) 