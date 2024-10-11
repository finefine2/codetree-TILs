# 시뮬레이션 시키는대로
N,M,K = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
guns = [[[] for _ in range(N)] for _ in range(N)]
for r in range(N):
    for c in range(N):
        if board[r][c] > 0:
            guns[r][c].append(board[r][c])

board = [[0] * N for _ in range(N)]
# r,c,dir,power,gun,score
players = {}
for m in range(1,M+1):
    r,c,d,p = tuple(map(int,input().split()))
    players[m] = [r-1,c-1,d,p,0,0]
    board[r-1][c-1] = m

opp = {0:2,1:3,2:0,3:1}
drs,dcs = [-1,0,1,0],[0,1,0,-1]
def in_range(r,c):
    return 0<=r<N and 0<=c<N
def leave(num,cr,cc,cd,cp,cg,cs):
    for k in range(4): # 현재방향부터 시계방향 90도씩 빈칸 찾기
        nr,nc = cr + drs[(cd+k)%4], cc + dcs[(cd+k)%4]
        if in_range(nr,nc) and board[nr][nc] == 0:
            # 총이 있다면 가장 강한 총 획득
            if len(guns[nr][nc])>0:
                cg = max(guns[nr][nc])
                guns[nr][nc].remove(cg)
            board[nr][nc] = num # 정보 갱신 후 리턴
            players[num] = [nr,nc,(cd+k)%4,cp,cg,cs]
            return

for _ in range(K): # k round
    # 1 ~ m player
    for i in players:
        # [1] 한 칸 이동 (격자 벗어나면 반대)
        cr,cc,cd,cp,cg,cs = players[i]
        nr,nc = cr + drs[cd], cc + dcs[cd]
        if not in_range(nr,nc):
            cd =opp[cd]
            nr,nc = cr + drs[cd], cc + dcs[cd]
        board[cr][cc] = 0 # 이전 위치 제거

        # [2-1] 이동한 위치가 빈칸 -> 강한 총 획득
        if board[nr][nc] == 0:
            if len(guns[nr][nc]) > 0: # 총이 존재하면
                mx = max(guns[nr][nc])
                if mx > cg: # 더 강한 총이면 교체
                    if cg > 0: # 총이 있는 경우
                        guns[nr][nc].append(cg) # 내 총은 바닥에 반납
                    guns[nr][nc].remove(mx)
                    cg = mx
            board[nr][nc] = i # 위치이동
            players[i] = [nr,nc,cd,cp,cg,cs] # 정보갱신
        # [2-2] 빈칸이 아닌 경우
        else:
            enemy = board[nr][nc] # 상대방 번호 확인
            er,ec,ed,ep,eg,es = players[enemy]
            if cp + cg > ep + eg or (cp+cg==ep+eg and cp>ep): #내가 이기는 경우
                cs += (cp+cg) - (ep+eg) # 공격력 차이만큼 점수 획득
                leave(enemy,nr,nc,ed,ep,0,es) # 상대방은 총을 두고 떠남
                # 이긴 플레이어는 가장 강한 총 얻기
                if cg < eg:
                    if cg > 0:
                        guns[nr][nc].append(cg)
                    cg = eg
                else:
                    if eg > 0:
                        guns[nr][nc].append(eg)
                board[nr][nc] = i
                players[i] = [nr,nc,cd,cp,cg,cs]
            else: # 내가 지는 경우
                es += (ep+eg) - (cp+cg)
                leave(i,nr,nc,cd,cp,0,cs) # 내가 총 놓고 떠남
                # 이긴 플레이어는 가장 강한 총 획득
                if eg < cg:
                    if eg > 0:
                        guns[nr][nc].append(eg)
                    eg = cg
                else:
                    if cg > 0:
                        guns[nr][nc].append(cg)
                board[nr][nc] = enemy
                players[enemy] = [nr,nc,ed,ep,eg,es]
for i in players:
    print(players[i][5],end=" ")