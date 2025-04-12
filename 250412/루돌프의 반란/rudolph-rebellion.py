from collections import deque

N, M, P, C, D = map(int, input().split())
v = [[0] * N for _ in range(N)]

# 루돌프 초기 위치
rr, rc = map(lambda x: int(x)-1, input().split())
v[rr][rc] = -1

# 초기화
scores = [0] * (P+1)
alive = [1] * (P+1)
alive[0] = 0
wakeup_turn = [1] * (P+1)

# 산타 위치 정보
santa = [[N] * 2 for _ in range(P+1)]
for _ in range(1, P+1):
    n, r, c = map(int, input().split())
    santa[n] = [r-1, c-1]
    v[r-1][c-1] = n

def move_santa(cur, sr, sc, dr, dc, mul):
    q = deque([(cur, sr, sc, mul)])
    v[sr][sc] = 0  # 현재 위치 비우기

    while q:
        cur, cr, cc, mul = q.popleft()
        nr, nc = cr + dr * mul, cc + dc * mul
        
        if 0 <= nr < N and 0 <= nc < N:
            if v[nr][nc] == 0:  # 빈칸
                v[nr][nc] = cur
                santa[cur] = [nr, nc]
                return
            else:  # 다른 산타가 있는 경우
                next_santa = v[nr][nc]
                v[nr][nc] = cur
                santa[cur] = [nr, nc]
                q.append((next_santa, nr, nc, 1))
        else:  # 범위 밖
            alive[cur] = 0
            return

# 게임 진행
for turn in range(1, M+1):
    # 모든 산타가 탈락했는지 확인
    if alive.count(1) == 0:
        break

    # 루돌프가 가장 가까운 산타 찾기
    min_dist = 2 * N * N
    mlst = []
    
    for idx in range(1, P+1):
        if not alive[idx]:
            continue
        sr, sc = santa[idx]
        dist = (rr-sr)**2 + (rc-sc)**2
        
        if dist < min_dist:
            min_dist = dist
            mlst = [(sr, sc, idx)]
        elif dist == min_dist:
            mlst.append((sr, sc, idx))
    
    mlst.sort(key=lambda x: (-x[0], -x[1]))  # r이 크고, c가 큰 순
    sr, sc, min_idx = mlst[0]

    # 루돌프 이동
    rdr = rdc = 0
    if rr > sr: rdr = -1
    elif rr < sr: rdr = 1
    if rc > sc: rdc = -1
    elif rc < sc: rdc = 1

    v[rr][rc] = 0
    rr, rc = rr + rdr, rc + rdc
    v[rr][rc] = -1

    # 충돌 체크
    if (rr, rc) == (sr, sc):
        scores[min_idx] += C
        wakeup_turn[min_idx] = turn + 2
        move_santa(min_idx, sr, sc, rdr, rdc, C)

    # 산타 이동
    for idx in range(1, P+1):
        if not alive[idx] or wakeup_turn[idx] > turn:
            continue

        sr, sc = santa[idx]
        min_dist = (rr-sr)**2 + (rc-sc)**2
        tlst = []

        for dr, dc in ((-1,0), (0,1), (1,0), (0,-1)):
            nr, nc = sr + dr, sc + dc
            if 0 <= nr < N and 0 <= nc < N and v[nr][nc] <= 0:
                dist = (rr-nr)**2 + (rc-nc)**2
                if dist < min_dist:
                    min_dist = dist
                    tlst = [(nr, nc, dr, dc)]

        if not tlst:
            continue
            
        nr, nc, dr, dc = tlst[-1]
        
        if (rr, rc) == (nr, nc):  # 루돌프와 충돌
            scores[idx] += D
            wakeup_turn[idx] = turn + 2
            v[sr][sc] = 0
            move_santa(idx, nr, nc, -dr, -dc, D)
        else:  # 일반 이동
            v[sr][sc] = 0
            v[nr][nc] = idx
            santa[idx] = [nr, nc]

    # 생존 산타 점수 추가
    for i in range(1, P+1):
        if alive[i]:
            scores[i] += 1

# 결과 출력
print(*scores[1:])