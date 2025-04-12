# 1-P 번 산타
# 루돌프가 반란

N,M,P,C,D = map(int,input().split())
rr,rc = map(int,input().split())
rr -= 1
rc -= 1

board = [[0] * N for _ in range(N)]
board[rr][rc] = -1

santas = {}
alive = [1] * (P+1)
scores = [0] * (P+1)
wakeup_turn = [0] * (P+1)
for _ in range(P):
    num, sr,sc = map(int,input().split())
    santas[num] = (sr-1,sc-1)
    board[sr-1][sc-1] = num

def in_range(r,c):
    return 0<=r<N and 0<=c<N

# move_santa(idx, sr, sc, rdr, rdc, C)
from collections import deque
def move_santa(num,cr,cc,dr,dc,mul):
    q = deque()

    q.append((num,cr,cc,mul))
    while q:
        cur,cr,cc,mul = q.popleft()
        nr,nc = cr + dr * mul, cc + dc * mul
        if in_range(nr,nc):
            if board[nr][nc] == 0:
                board[nr][nc] = cur
                santas[cur] = (nr,nc)
                return 
            elif board[nr][nc] > 0:
                idx = board[nr][nc]
                q.append((idx,nr,nc,1))
                board[nr][nc] = cur
                santas[cur] = (nr,nc)

        elif not in_range(nr,nc):
            alive[num] = 0
            return

for turn in range(1,M+1):
    if alive.count(1) == 0:
        break
    # rudolf 먼저 움직이고 그 이후에 1-p번 산타들이 순차적으로 이동
    # [1] 루돌프의 이동

    min_dist = 2 * (N**2)
    for idx in santas:
        # 탈락하지 않은 산타를 대상
        if alive[idx] == 0: continue
        sr,sc = santas[idx]
        dist = (sr-rr) ** 2 + (sc-rc) ** 2

        if dist < min_dist:
            min_dist = dist
            tlst = [(sr,sc,idx)]
        elif dist == min_dist:
            tlst.append((sr,sc,idx))

    tlst.sort(reverse=True)
    sr,sc,idx = tlst[0]
            # 목표 확인
        # 방향 찾기
    rdr = rdc = 0
    if rr > sr:
        rdr = -1
    elif rr < sr:
        rdr = 1
    if rc > sc:
        rdc = -1
    elif rc < sc:
        rdc = 1
    board[rr][rc] = 0
    rr,rc = rr + rdr, rc + rdc
    board[rr][rc] = -1
        # 충돌한다면?
    if (rr,rc) == (sr,sc):
        scores[idx] += C
        wakeup_turn[idx] = turn + 2
        move_santa(idx, sr, sc, rdr, rdc, C)

    # [2] 산타의 이동
    for idx in santas:
        # 기절했거나 탈락한 산타는 제외
        if wakeup_turn[idx] > turn or alive[idx] == 0: continue

        sr,sc = santas[idx]
        min_dist = (sr-rr) ** 2 + (sc-rc) ** 2
        tlst = []
        for dr,dc in ((-1,0),(0,1),(1,0),(0,-1)):
            nr,nc = sr + dr, sc + dc
            dist = (nr-rr) ** 2 + (nc-rc) ** 2
            if in_range(nr,nc) and board[nr][nc] <= 0 and dist < min_dist:
                min_dist = dist
                tlst.append((nr,nc,dr,dc))
        if len(tlst) == 0: continue
        nr,nc,dr,dc = tlst[-1]
        # 루돌프와 충돌 시
        if (nr,nc) == (rr,rc):
            wakeup_turn[idx] = turn +  2
            scores[idx] += D
            board[sr][sc] = 0
            move_santa(idx,nr,nc,-dr,-dc,D)

        else:
            board[sr][sc] = 0
            board[nr][nc] = idx
            santas[idx] = (nr,nc)
    for idx in santas:
        if alive[idx] == 1:
            scores[idx] += 1
print(*scores[1:],end=" ")