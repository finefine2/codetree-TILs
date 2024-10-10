# 조건들 -> 체크, 설명은 시간 순으로 정리하기 
# 연쇄이동하는 대상들은 q에 넣기? 
# N x N board
# r,c

# Rudolf
# 가장 가까운 산타를 향해 1칸 돌진
# 단 탈락하지 않은 산타에게만
# 가장 가까운 산타가 2명이상이면, r c 가 클수록
# 상하좌우 대각선 포함 8방향으로 이동
# 산타랑 가까와지는 방향으로


# Santa
# 1 ~ P번까지 순차적으로 움직임
# 기절하거나 탈락한 산타는 제외
# 산타도 루돌프에게 가까와지는 방향으로 1칸 이동
# 다른 산타가 있는 칸이나 게임판 밖은 놉
# 인접 4방향 상하좌우

# 충돌
# if rudolf == santa
# rudolf 가 움직여서 충돌 -> 산타 + C
# 산타가 움직여서 충돌 -> 산타 +D



N,M,P,C,D = tuple(map(int,input().split()))

rr,rc = tuple(map(int,input().split()))
santa = [[N] * 2 for _ in range(P+1)]

rr -= 1
rc -= 1
board = [[0] * N for _ in range(N)]
board[rr][rc] = -1 # 루돌프!

score = [0] * (P+1)
wakeup_turn = [0] * (P+1)
alive = [1] * (P+1)
alive[0] = 0
for _ in range(P):
    n,r,c = tuple(map(int,input().split()))
    santa[n] = [r-1,c-1]
    board[r-1][c-1] = n # 몇번 산타가 존재하는지만 표기용
def move_santa(cur,sr,sc,dr,dc,mul): # cur번 산타를 sr,sc 에서 dr,dc 방향으로 mul칸 이동 
    q = [(cur,sr,sc,mul)] 
    
    while q: 
        cur,cr,cc,mul = q.pop(0) 
        # 진행방향 mul칸 만큼 이동시켜 범위내이고, 산타있으면 q삽입 / 범위 밖 처리 
        nr,nc = cr + dr * mul, cc + dc *mul
        if 0<=nr<N and 0<=nc<N: # 범위 내 산타 체크 
            if board[nr][nc] == 0: #빈칸-> 이동
                board[nr][nc] = cur 
                santa[cur] = [nr,nc] 
                return 
            else: # 산타가 있다면 연쇄 이동 
                q.append((board[nr][nc],nr,nc,1)) # 한 칸 이동, 
                board[nr][nc] = cur
                santa[cur] = [nr,nc] 
        else: #범위 밖 -> 탈락 
            alive[cur] = 0 
            return 
for turn in range(1,M+1):
    # turn을 다 돌거나 모두 탈락하면 끝!
    if alive.count(1) == 0:
        break
    # 루돌프의 이동
    # 가장 가까운 산타에게 돌격
    min_dist = 2 * N ** 2
    # 모든 산타를 대상으로 조사해야겠네
    for idx in range(1,P+1): # 1~P 산타
        # 탈락한 산타는 아웃
        if alive[idx] == 0:
            continue
        sr,sc = santa[idx]

        dist = (rr-sr) ** 2 + (rc-sc) ** 2
        if min_dist > dist:
            min_dist = dist
            mlst = [(sr,sc,idx)] # 최소 거리 -> 새 리스트
        elif min_dist == dist:
            mlst.append((sr,sc,idx))
    mlst.sort(reverse=True) # 행 큰 -> 열 큰
    sr,sc,mn_idx = mlst[0] # 돌격 목표 산타!

    # 대상 산타방향으로 루돌프 이동
    rdr = rdc = 0
    if rr > sr: rdr = -1
    elif rr < sr: rdr = 1
    if rc > sc: rdc = -1
    elif rc < sc: rdc = 1

    board[rr][rc] = 0 # 루돌프 현재 자리 지우기
    rr,rc = rr + rdr, rc + rdc # 루돌프 움직이기
    board[rr][rc] = -1 # 이동한 자리에 루돌프 표시
    
    # 루돌프와 산타가 충돌 시 산타가 밀리는 처리 
    if (rr,rc) == (sr,sc): 
        score[mn_idx] += C # 산타는 C점 획득
        wakeup_turn[mn_idx] = turn + 2 # 꺠어날 턴 저장
        move_santa(mn_idx,sr,sc,rdr,rdc,C) # 산타 C칸 이동 
    # 순서대로 산타이동: 기절하지 않은 경우 (산타의 턴 <= turn)
    for idx in range(1,P+1):
        if alive[idx] == 0: continue # 탈락한 경우 스킵
        if wakeup_turn[idx] > turn: continue # 깨어날 턴이 아직 아닌 경우

        sr,sc = santa[idx]
        mn_dist = (rr-sr) ** 2 + (rc-sc) ** 2
        tlst = []
        # U R D L
        for dr,dc in ((-1,0),(0,1),(1,0),(0,-1)):
            nr,nc = sr + dr, sc + dc
            dist = (nr-rr) ** 2 + (rc-nc) ** 2
            # 범위 내 산타 없고 더 짧은 거리인 경우
            if 0<=nr<N and 0<=nc<N and board[nr][nc] <= 0 and mn_dist > dist:
                mn_dist = dist
                tlst.append((nr,nc,dr,dc))
        if len(tlst) == 0: continue #이동할 위치 없음
        nr,nc,dr,dc = tlst[-1] # 마지막에 추가된 더 짧은 거리
    # 루돌프와 추돌하게 되면
        if (rr,rc) == (nr,nc):
            score[idx] += D
            wakeup_turn[idx] = turn + 2
            board[sr][sc] = 0
            move_santa(idx,nr,nc,-dr,-dc,D)
        else: # 빈칸이면 좌표갱신 및 이동 처리 
            board[sr][sc] = 0
            board[nr][nc] = idx
            santa[idx] = [nr,nc] 
    for i in range(1,P+1): 
        if alive[i] == 1: 
            score[i] += 1 
print(*score[1:])