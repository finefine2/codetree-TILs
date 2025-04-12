N,M,K = map(int,input().split())

board = []
guns = [[[] for _ in range(N)] for _ in range(N)]

for r in range(N):
    board.append(list(map(int,input().split())))
    for c in range(N):
        if board[r][c] > 0:
            guns[r][c].append(board[r][c])
            board[r][c] = 0

drs,dcs = [-1,0,1,0],[0,1,0,-1]
players = {}
for m in range(1,M+1):
    r,c,d,s = map(int,input().split())
    players[m] = (r-1,c-1,d,s,0,0)
    board[r-1][c-1] = m 
opp = {0:2,1:3,2:0,3:1}
def in_range(r,c): 
    return 0<=r<N and 0<=c<N

# leave(enemy, er, ec, ed, es, 0, ep)
def leave(num,cr,cc,cd,cs,cg,cp): 
    for k in range(4): 
        nr,nc = cr + (cd+k) % 4, cc + (cd+k) % 4
        if in_range(nr,nc) and board[nr][nc] == 0: 
            board[cr][cc] = 0
            if len(guns[nr][nc]) > 0:
                cg = max(guns[nr][nc]) 
                guns[nr][nc].remove(mx_g) 
            board[nr][nc] = num 
            players[num] = [nr,nc,(cd+k)%4,cs,cg,cp]
            return 
for _ in range(K): 
    # 순차적으로 이동 
    # 1-1 첫 플레이어부터 본인 방향대로 한 칸 이동 
    # 맵 밖으로 빠지게 되면 방향은 반대로
    for idx in players: 
        cr,cc,cd,cs,cg,cp = players[idx] 
        nr,nc = cr + drs[cd], cc + dcs[cd] 
        if not in_range(nr,nc): 
            cd = opp[cd] 
            nr,nc = cr + drs[cd], cc + dcs[cd] 
        
        board[cr][cc] = 0 
        
        #2-1 이동한 곳에 플레이어가 없다
        if board[nr][nc] == 0:
            # 총이 있는지 체크 
            if len(guns[nr][nc]) > 0: 
                mx_g = max(guns[nr][nc]) 
                if cg < mx_g: 
                    if cg > 0: 
                        guns[nr][nc].append(cg) 
                    guns[nr][nc].remove(mx_g) 
                    cg = mx_g
            board[nr][nc] = idx 
            players[idx] = [nr,nc,cd,cs,cg,cp]
        #2-2-1 이동한 곳에 플레이어가 있다
        else:
            # fight
            enemy = board[nr][nc] 
            er,ec,ed,es,eg,ep = players[enemy] 
            if (cs+cg) > (es+eg) or ((cs+cg)==(es+eg) and cs > es): 
            # 내가 이긴다
                cp += (cs+cg) - (es+eg)
                leave(enemy,er,ec,ed,es,0,ep) 
                if eg > cg: 
                    if cg > 0: 
                        guns[nr][nc].append(cg) 
                    cg = eg
                else: 
                    if eg > 0: 
                        guns[nr][nc].append(eg) 
                board[nr][nc] = idx 
                players[idx] = [nr,nc,cd,cs,cg,cp] 
            else: 
            # 쟤가 이긴다 
                ep += (es+eg) - (cs+cg) 
                leave(idx,nr,nc,cd,cs,0,cp) 
                if cg > eg: 
                    if eg > 0: 
                        guns[nr][nc].append(eg) 
                    eg = cg 
                else: 
                    if cg > 0:
                        guns[nr][nc].append(cg) 
                board[nr][nc] = enemy
                players[enemy] = [nr,nc,ed,es,eg,ep]
                
for p in players: 
    print(p[5],end=" ") 
