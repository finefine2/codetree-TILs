N,M,K = tuple(map(int,input().split())) 
board = [list(map(int,input().split())) for _ in range(N)] 
guns = [[[] for _ in range(N)] for _ in range(N)]
for r in range(N): 
    for c in range(N): 
        if board[r][c] > 0: 
            guns[r][c].append(board[r][c]) 
board = [[0] * N for _ in range(N)]

players = {} 
for m in range(1,M+1): 
    r,c,d,p = tuple(map(int,input().split())) 
    # r c dir power gun score
    players[m] = [r-1,c-1,d,p,0,0]
    board[r-1][c-1] = m 
def in_range(r,c): 
    return 0<=r<N and 0<=c<N


def leave(num,cr,cc,cd,cp,cg,cs): 
    # 총을 뺏긴 패배자가 오는 곳임 
    for k in range(4): 
        nr,nc = cr + drs[(cd+k)%4], cc + dcs[(cd+k)%4]
        if in_range(nr,nc) and board[nr][nc] == 0: 
            if len(guns[nr][nc]): 
                cg = max(guns[nr][nc]) 
                guns[nr][nc].remove(cg) 
            board[nr][nc] = num 
            players[num] = [nr,nc,(cd+k)%4,cp,cg,cs]
            return 

opp = {0:2,1:3,2:0,3:1} 
drs,dcs = [-1,0,1,0],[0,1,0,-1] 
# K turn - M players 
for _ in range(K): 
    for i in players: 
        # 순차적으로 플레이어들이 이동 
        cr,cc,cd,cp,cg,cs = players[i] 
        nr,nc = cr + drs[cd], cc + dcs[cd]
        if not in_range(nr,nc): 
            cd = opp[cd] 
            nr,nc = cr + drs[cd], cc + dcs[cd] 
        board[cr][cc] = 0 # 이동처리 

        # 2-1 
        # 이동한 곳에 플레이어가 없다 
        if board[nr][nc] == 0: 
            # 총이 있는지 확인
            if len(guns[nr][nc]) > 0: 
                mx = max(guns[nr][nc]) 

                if mx > cg: 
                    if cg > 0:
                        guns[nr][nc].append(cg) 
                cg = mx 
                guns[nr][nc].remove(mx) 
            board[nr][nc] = i
            players[i] = [nr,nc,cd,cp,cg,cs]
        # 2-2 플레이어가 존재한다 
        else: 
            # 상대방의 정보를 조회하자 
            enemy = board[nr][nc]
            er,ec,ed,ep,eg,es = players[enemy]
            # 싸움을 시작한다 
            # 내가 이기는 경우 
            if cp + cg > ep + eg or (cp + cg == ep + eg and cp > ep): 
                leave(enemy,nr,nc,ed,ep,0,es) 
                cs += (cp+cg) - (ep+eg) 
                if eg > cg: 
                    if cg > 0: 
                        guns[nr][nc].append(cg) 
                    else: 
                        guns[nr][nc].append(eg) 
                    cg = eg 
                board[nr][nc] = i 
                players[i] = [nr,nc,cd,cp,cg,cs] 
            # 상대가 이기는 경우
            else: 
                leave(i,nr,nc,cd,cp,0,cs) 
                es += (ep+eg) - (cp+cg) 
                if cg > eg: 
                    if eg > 0: 
                        guns[nr][nc].append(eg) 
                    else: 
                        guns[nr][nc].append(cg) 
                    eg = cg 
                board[nr][nc] = enemy
                players[enemy] = [nr,nc,ed,ep,eg,es] 
for p in players: 
    print(players[p][5],end=" ")