# simulation -> 시키는대로 진행
N,M,K = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
guns = [[[] for _ in range(N)] for _ in range(N)]
for r in range(N):
    for c in range(N):
        if board[r][c] > 0:
            guns[r][c].append(board[r][c])

board = [[0] * N for _ in range(N)]
# r,c,dir,power,gun,score
# dirs: U R D L
players = {}
for m in range(1,M+1):
    r,c,d,p = tuple(map(int,input().split()))
    players[m] = [r-1,c-1,d,p,0,0]
    board[r-1][c-1] = m

opp = {0:2,1:3,2:0,3:1}
#dirs U R D L
drs, dcs = [-1,0,1,0],[0,1,0,-1]

def leave(num,cr,cc,cd,cp,cg,cs):
    for k in range(4): # 현재 방향부터 90도씩 빈칸 찾기 (최소한 내가 온 칸은 비어있음)
        nr,nc = cr + (cd+k) % 4, cc + (cd+k) % 4
        if in_range(nr,nc) and board[nr][nc] == 0:
            # 총이 있다면 가장 강한 총을 획득
            if len(guns[nr][nc]) > 0:
                cg = max(guns[nr][nc])
                guns[nr][nc].remove(cg)
        players[num] = [nr,nc,(cd+k)%4,cp,cg,cs]# 내 정보들을 갱신한 후 리턴
        board[nr][nc] = num
        return
def in_range(r,c):
    return 0<=r<N and 0<=c<N
for _ in range(K): # K 라운드 동안 경기 진행
    # 1 ~ M players 번호순대로 처리
    for i in players:
    # 1 한 칸 이동
        cr,cc,cd,cp,cg,cs = players[i]
        nr,nc = cr + drs[cd], cc + dcs[cd]
        if not in_range(nr,nc): # 범위를 벗어나면
            cd = opp[cd]  # 방향은 반대로 하고 한 칸 이동
            nr,nc = cr + drs[cd], cc + dcs[cd]
        board[cr][cc] = 0 # 이전 위치에서 플레이어 제거

        # 2-1 이동한 위치가 빈칸인 경우 -> 제일 강한 총 획득
        if board[nr][nc] == 0:
            if len(guns[nr][nc]) > 0: # 총이 있는 경우
                mx = max(guns[nr][nc])
                if mx > cg: # 더 강한 총이면 교체
                    if cg > 0: # 내가 만약 총을 들고 있다면?
                        guns[nr][nc].append(cg) # 내 총은 바닥에 반납
                guns[nr][nc].remove(mx)
                cg = mx
            board[nr][nc] = i # 위치 이동
            players[i] = [nr,nc,cd,cp,cg,cs] # 정보 업데이트

        # 2-2 빈 칸이 아닌 경우 -> 싸울 상대방이 존재함
        else:
            enemy = board[nr][nc] # 상대방 번호 확인
            er,ec,ed,ep,eg,es = players[enemy]
            if cp + cg > ep + eg or (cp+cg==ep+eg and cp > ep): #내가 이기는 경우
                cs += (cp+cg) - (ep+eg) # 공격력 차이만큼 점수 획득
                leave(enemy,nr,nc,ed,ep,0,es) # 상대방은 총을 놓고 떠남

                # 이긴 플레이어(나)는 가장 강한 총 얻기: 상대방총 vs 내총
                if cg < eg:
                    if cg > 0:
                        guns[nr][nc].append(cg)
                    cg = eg
                else:
                    if eg > 0:
                        guns[nr][nc].append(eg)
                board[nr][nc] = i
                players[i] = [nr,nc,cd,cp,cg,cs]
            else: # 내가 지는 경우 - 상대방이 이기는 경우
                es += (ep+eg) - (cp+cg) # 공격력 차이만큼 점수 획득
                leave(i,nr,nc,cd,cp,0,cs) # 내가 총을 두고 떠남

                # 이긴 플레이어(상대)는 가장 강한 총 획득
                if cg > eg:
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