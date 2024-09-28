N,M,P,C,D = tuple(map(int,input().split())) 
v = [[0] * N for _ in range(N)] 

rr,rc = tuple(map(int,input().split())) 
rr -= 1 
rc -= 1 
v[rr][rc] = -1 

score = [0] * (P+1) 
alive = [1] * (P+1) 
alive[0] = 0 
wakeup_turn = [1] * (P+1) 

santa = [[N] * 2 for _ in range(P+1)] 

for _ in range(1,P+1): 
    n,r,c = tuple(map(int,input().split())) 
    santa[n] = [r-1,c-1] 
    v[r-1][c-1] = n 

def move_santa(cur,sr,sc,dr,dc,mul): 
    q = [(cur,sr,sc,mul)] 

    while q: 
        cur,cr,cc,mul=q.pop(0) 

        nr,nc = cr + dr*mul, cc + dc*mul 
        if 0<=nr<N and 0<=nc<N: 
            if v[nr][nc] == 0: 
                v[nr][nc] = cur 
                santa[cur] = [nr,nc] 
                return 
            else: 
                q.append((v[nr][nc],nr,nc,1)) 
                v[nr][nc] = cur 
                santa[cur] = [nr,nc] 
        else: 
            alive[cur] = 0 
            return
    
for turn in range(1,M+1): 
    # 0. 모두 탈락 시 
    if alive.count(1) == 0: 
        break 
    # 1-1 rudolf move, find the closest santa 
    min_dist = 2 * N ** 2 
    for idx in range(1,P+1): 
        if alive[idx] == 0: 
            continue 
        sr,sc = santa[idx] 
        dist = (rr-sr) ** 2 + (rc-sc) ** 2 
        if min_dist > dist: 
            min_dist = dist 
            mlst = [(sr,sc,idx)] 
        elif min_dist == dist: 
            mlst.append((sr,sc,idx)) 
    mlst.sort(reverse=True) 
    sr,sc,min_idx = mlst[0] 

    # 1-2 rudolf move to the santa 
    rdr = rdc = 0 
    if rr > sr: rdr = -1 
    elif rr < sr: rdr = 1 

    if rc > sc: rdc = -1 
    elif rc < sc: rdc = 1 
    v[rr][rc] = 0 
    rr,rc = rr+rdr,rc+rdc 
    v[rr][rc] = -1 

    # 1-3 rudolf and santa crash, move santa 
    if (rr,rc) == (sr,sc): 
        score[min_idx] += C 
        wakeup_turn[min_idx] = turn + 2 
        move_santa(min_idx,sr,sc,rdr,rdc,C) 

    # 2-1 move santa, those for wake up 
    for idx in range(1,P+1): 
        if alive[idx] == 0: continue
        if wakeup_turn[idx] > turn: continue

        sr,sc = santa[idx] 
        min_dist = (rr-sr) ** 2 + (rc-sc) ** 2 
        tlst = [] 
        # U R D L 
        drs,dcs = [-1,0,1,0],[0,1,0,-1] 
        for dr,dc in zip(drs,dcs): 
            nr,nc = sr + dr, sc + dc 
            dist = (rr-nr)**2 + (rc-nc)**2 

            if 0<=nr<N and 0<=nc<N and v[nr][nc] <= 0 and min_dist>dist: 
                min_dist = dist
                tlst.append((nr,nc,dr,dc)) 
        if len(tlst) == 0: continue
        nr,nc,dr,dc = tlst[-1] 

        # 2-2 after crash 
        if (rr,rc) == (nr,nc): 
            score[idx] += D 
            wakeup_turn[idx] = turn + 2 
            v[sr][sc] = 0 
            move_santa(idx,nr,nc,-dr,-dc,D) 
        else: 
            v[sr][sc] = 0 
            v[nr][nc] = idx 
            santa[idx] = [nr,nc] 
    for i in range(1,P+1): 
        if alive[i] == 1: 
            score[i] += 1 
print(*score[1:])