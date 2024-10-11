# 루돌프
#조건들 체크 , 설명 -> 시간 순 정리
N,M,P,C,D = tuple(map(int,input().split()))
v = [[0] * N for _ in range(N)]

rr,rc = tuple(map(int,input().split()))
rr -= 1
rc -= 1
v[rr][rc] = -1 # 루돌프 표시
scores = [0] * (P+1)
alive = [1] * (P+1)
alive[0] = 0
wakeup_turn = [1] * (P+1)

santa = [[N] * 2 for _ in range(P+1)]
for _ in range(1,P+1):
    n,r,c = tuple(map(int,input().split()))
    santa[n] = [r-1,c-1]
    v[r-1][c-1] = n

def move_santa(cur,sr,sc,dr,dc,mul):
    # cur번 산타를 sr,sc 에서 dr,dc 방향으로 mul칸 이동시키기
    q = [(cur,sr,sc,mul)]

    while q:
        cur,cr,cc,mul = q.pop(0)
        # 진행방향 mul칸만큼 이동시켜서 범위내이고 산타있으면 q삽입 / 범위 밖 처리
        nr,nc = cr + dr * mul, cc + dc * mul
        if 0<=nr<N and 0<=nc<N: # 범위 내 산타 여부 체크
            if v[nr][nc] == 0: # 빈칸 -> 이동처리
                v[nr][nc] = cur
                santa[cur] = [nr,nc]
                return
            else: # 산타 있으면 연쇄이동
                q.append((v[nr][nc],nr,nc,1)) # 한 칸 이동, v[nr][nc]: 다음 산타번호
                v[nr][nc] = cur
                santa[cur] = [nr,nc]
        else: # 범위 밖 -> 탈락 -> 끝
            alive[cur] = 0
            return

for turn in range(1,M+1):
    # 모두 탈락하면 break
    if alive.count(1) == 0:
        break

    # [1-1] 루돌프 이동시키기 가장 가까운 산타찾기
    # 탈락하지 않은 산타대상
    min_dist = 2 * N ** 2
    for idx in range(1,P+1):
        if alive[idx] == 0: continue # 산타가 죽으면 패스
        sr,sc = santa[idx]
        dist = (rr-sr) ** 2 + (rc-sc) ** 2
        if min_dist > dist:
            min_dist = dist
            mlst = [(sr,sc,idx)] # 최소거리 -> 새리스트
        elif min_dist == dist:
            mlst.append((sr,sc,idx))
    mlst.sort(reverse=True) # r bigger, c bigger
    sr,sc,min_idx = mlst[0] # 목표 산타를 찾음

    # [1-2] 목표 산타 방향으로 루돌프 움직이기
    rdr = rdc = 0
    if rr > sr: rdr = -1
    elif rr < sr: rdr = 1
    if rc > sc: rdc = -1
    elif rc < sc: rdc = 1

    v[rr][rc] = 0 # 루돌프 현재자리 지우기
    rr,rc = rr + rdr, rc + rdc # 루돌프 이동시키기
    v[rr][rc] = -1 # 보드에 루돌프 표시

    # [1-3] 루돌프가 산타를 충돌 시 산타 밀리기
    if (rr,rc) == (sr,sc): # 충돌
        scores[min_idx] += C # 산타는 C점획득
        wakeup_turn[min_idx] = turn + 2 # 깨어날 턴 번호를 저장한다
        move_santa(min_idx,sr,sc,rdr,rdc,C) # 산타 C칸 이동

    # [2-1] 순서대로 기절 안하고 살아있는 산타 이동시키기
    for idx in range(1,P+1):
        if alive[idx] == 0: continue # 죽은 건 버려
        if wakeup_turn[idx] > turn: continue # 일어나지 않으면 버려

        sr,sc = santa[idx]
        min_dist = (rr-sr) ** 2 + (rc-sc) ** 2
        tlst = []

        # U R D L
        for dr, dc in ((-1,0),(0,1),(1,0),(0,-1)):
            nr,nc = sr + dr, sc + dc
            dist = (nr-rr) ** 2 + (nc - rc) ** 2
            # 범위내, 산타 없고 더 짧은 거리인 경우
            if 0<=nr<N and 0<=nc<N and v[nr][nc] <= 0 and dist < min_dist:
                min_dist = dist
                tlst.append((nr,nc,dr,dc))
        if len(tlst) == 0: continue # 이동할 위치 없음
        nr,nc,dr,dc = tlst[-1] # 마지막에 추가된 최단거리
        # [2-2] 루돌프와 충돌 시 처리
        if (rr,rc) == (nr,nc): # 루돌프와 충돌하면 반대로 튕겨나감
            scores[idx] += D
            wakeup_turn[idx] = turn+2
            v[sr][sc] = 0
            move_santa(idx,nr,nc,-dr,-dc,D)
        else:
            # 빈칸, 좌표갱신, 이동
            v[sr][sc] = 0
            v[nr][nc] = idx
            santa[idx] = [nr,nc]
    # [3] 점수획득 살아있는 산타 + 1
    for i in range(1,P+1):
        if alive[i] == 1:
            scores[i] += 1

for i in range(1,P+1):
    print(scores[i],end=" ")