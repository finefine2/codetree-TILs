N,M,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
guns = [[[] for _ in range(N)] for _ in range(N)]

for r in range(N):
    for c in range(N):
        if board[r][c] > 0:
            guns[r][c].append(board[r][c])
board = [[0] * N for _ in range(N)]

players = {}
for m in range(1,M+1):
    r,c,d,p = map(int,input().split())
    players[m] = [r-1,c-1,d,p,0,0]
    board[r-1][c-1] = m
opp = {0:2,1:3,2:0,3:1}
drs,dcs = [-1,0,1,0],[0,1,0,-1]
def in_range(r,c):
    return 0<=r<N and 0<=c<N
def leave(num,cr,cc,cd,cp,cg,cs):
    for k in range(4):
        nr,nc = cr + drs[(cd+k)%4], cc + dcs[(cd+k)%4]
        if in_range(nr,nc) and board[nr][nc] == 0:
            if len(guns[nr][nc]) > 0:
                cg = max(guns[nr][nc])
                guns[nr][nc].remove(cg)
            board[nr][nc] = num
            players[num] = [nr,nc,(cd+k)%4,cp,cg,cs]
            return
for _ in range(K):
    for p in players:
        cr,cc,cd,cp,cg,cs = players[p]
        nr,nc = cr + drs[cd], cc + dcs[cd]
        if not in_range(nr,nc):
            cd = opp[cd]
            nr,nc = cr + drs[cd], cc + dcs[cd]
        board[cr][cc] = 0

        if board[nr][nc] == 0:
            if len(guns[nr][nc])>0:
                max_g = max(guns[nr][nc])
                if max_g > cg:
                    if cg > 0:
                        guns[nr][nc].append(cg)
                    guns[nr][nc].remove(max_g)
                    cg = max_g
            board[nr][nc] = p
            players[p] = [nr,nc,cd,cp,cg,cs]

        else: # 빈칸이 아닐경우
            enemy = board[nr][nc]
            er,ec,ed,ep,eg,es = players[enemy]
            if cp+cg > ep+eg or (cp+cg==ep+eg and cp>ep):
                cs += (cp+cg) - (ep+eg)
                leave(enemy,nr,nc,ed,ep,0,es)

                if eg > cg:
                    if cg > 0:
                        guns[nr][nc].append(cg)
                    cg = eg
                else:
                    if eg > 0:
                        guns[nr][nc].append(eg)
                board[nr][nc] = p
                players[p] = [nr,nc,cd,cp,cg,cs]
            else:
                es += (ep+eg) - (cp+cg)
                leave(p,nr,nc,cd,cp,0,cs)

                if eg < cg:
                    if eg > 0:
                        guns[nr][nc].append(eg)
                    eg = cg
                else:
                    if cg > 0:
                        guns[nr][nc].append(cg)
                board[nr][nc] = enemy
                players[enemy]=[nr,nc,ed,ep,eg,es]
for p in players:
    print(players[p][5],end=" ")