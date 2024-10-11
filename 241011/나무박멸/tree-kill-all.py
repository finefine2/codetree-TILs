# 음수 처리 및 동시 실행 -> 복사 후 대입
INF = -10000
N,M,K,C = tuple(map(int,input().split()))
C = -(C+1) # 제초제는 음수처리
board = [[INF] * (N+2)] + [[INF] + list(map(int,input().split())) + [INF] for _ in range(N)] + [[INF] * (N+2)]

for r in range(1,N+1):
    for c in range(1,N+1):
        if board[r][c] == -1:
            board[r][c] = INF # 건물을 영구적인 제초제 처리 (나무 못자라고, 제초제 못 뻗)

ans = 0
for _ in range(M): #M년
    # [0] 제초제 감소
    for r in range(1,N+1):
        for c in range(1,N+1):
            if board[r][c] < 0: # 제초제가 뿌려져있으면 감소 (건물은 절대 0 안됨)
                board[r][c] += 1
    # [1] 인접 4칸 중 나무있는 칸수만큼 동시에 성장
    nboard = [x[:] for x in board]
    for r in range(1,N+1):
        for c in range(1,N+1):
            if board[r][c] > 0: # 나무가 있다면, 인접 나무 수만큼 성장
                for nr,nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if board[nr][nc] > 0:
                        nboard[r][c] += 1
    board = nboard
    # 인접 빈칸에 번식 (동시)
    nboard = [x[:] for x in board]
    for r in range(1,N+1):
        for c in range(1,N+1):
            if board[r][c] > 0: # 내가 나무면 번식
                tlst = [] # 빈칸 좌표 저장
                for nr,nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if board[nr][nc] == 0:
                        tlst.append((nr,nc))
                if len(tlst) > 0: # 빈칸이있으면 번식
                    d = board[r][c] // len(tlst)
                    for tr,tc in tlst:
                        nboard[tr][tc] += d
    board = nboard

    # 가장 많이 박멸되는 칸을 찾기
    mx,mx_r,mx_c = 0,0,0
    for r in range(1,N+1):
        for c in range(1,N+1):
            if board[r][c] > 0: # 나무 있는 칸에 뿌려야 제초제 확산
                cnt = board[r][c] # 내 자리 포함
                for dr,dc in ((-1,-1),(-1,1),(1,-1),(1,1)):
                    for k in range(1,K+1): # 뻗어가며 처리
                        nr,nc = r + dr * k, c + dc * k
                        if board[nr][nc] <= 0: # 빈땅, 제초제 , 건물
                            break
                        else:
                            cnt += board[nr][nc]
                if cnt > mx:
                    mx,mx_r,mx_c = cnt,r,c
    if mx == 0:
        break
    ans += mx

    # 제초제 살포
    # 전파되는 도중 벽이 있거나 나무가 아예 없으면
    # 그 칸까지는 뿌려지지만 그 이후로는 전파되지않음
    board[mx_r][mx_c] = C # 중앙에 제초제
    for dr,dc in ((-1,-1),(-1,1),(1,-1),(1,1)):
        for k in range(1,K+1): # 뻗어가면서 처리
            nr,nc = mx_r + dr * k , mx_c + dc * k
            if board[nr][nc] <= 0:
                if board[nr][nc] >= C:
                    board[nr][nc] = C
                break
            else:
                board[nr][nc] = C
print(ans)