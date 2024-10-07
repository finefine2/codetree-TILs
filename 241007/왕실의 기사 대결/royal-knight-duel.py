from collections import deque 
L,N,Q = tuple(map(int,input().split())) 

board = [[2] * (L+2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(L)] + [[2] * (L+2)] 

units = {} 
init_k = [0] * (N+1)
for n in range(1,N+1): 
    r,c,h,w,k = tuple(map(int,input().split())) 
    units[n] = [r,c,h,w,k]
    init_k[n] = k 
def push_unit(start,dr): 
    q = deque() 
    pset = set() 
    damage = [0] * (1+N) 
    drs,dcs = [-1,0,1,0],[0,1,0,-1] 

    q.append(start) 
    pset.add(start) 
    
    while q: 
        s = q.popleft() 
        sr,sc,h,w,k = units[s] 

        nr,nc = sr + drs[dr], sc + dcs[dr] 
        for r in range(nr,nr+h): 
            for c in range(nc,nc+w): 
                # 벽이라면 끝 
                if board[r][c] == 2: 
                    return 
                if board[r][c] == 1: 
                    damage[s] += 1 # 현재 번호의 기사 데미지 누적
        # 겹치는 다른 유닛이 있는지 확인하기 
        for idx in units: 
            if idx in pset: continue 
            tr,tc,th,tw,tk = units[idx] 
            if tr <= nr+h-1 and tc <= nc+w-1 and nr <= tr+th-1 and nc <= tc+tw-1: 
                q.append(idx) 
                pset.add(idx) 
    # 명령받은 기사는 데미지 0 
    damage[start] = 0 
    # 움직여야 하는 기사들에 대해서 
    for p in pset: 
        sr,sc,h,w,k = units[p] 
        if damage[p] >= k: 
            units.pop(p) 
        else: 
            nr,nc = sr+drs[dr],sc+dcs[dr] 
            units[p] = (nr,nc,h,w,k-damage[p]) 
        


for _ in range(Q): 
    idx,dr = tuple(map(int,input().split())) 
    if idx in units: 
        push_unit(idx,dr) 
ans = 0 
for idx in units: 
    ans += init_k[idx] - units[idx][4] 
print(ans)