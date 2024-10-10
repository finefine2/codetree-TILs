# 변수를 관리할 때 어떻게 해줄 것인지에 대한 고민을 해보자 
# 이 경우에는 spray 배열을 따로 안 해주고 보드에 한꺼번에 처리해버림 
# 음수 처리 및 동시 실행 -> 복사 후 대입
INF = -10000
N,M,K,C = tuple(map(int,input().split()))
C = -(C+1) # 제초제는 음수처리(C+1년 뒤 사라짐)
board = [[INF] * (N+2)] + [[INF] + list(map(int,input().split())) + [INF] for _ in range(N)] + [[INF] * (N+2)]

for r in range(1,N+1):
    for c in range(1,N+1):
        if board[r][c] == -1:
            board[r][c] = INF # 건물을 영구적인 제초제 처리 (나무 못 자라고, 제초제 못 뻗어가게)

ans = 0
for _ in range(M): # while M years
    # [0] 제초제 감소
    for r in range(1,N+1):
        for c in range(1,N+1):
            if board[r][c] < 0: # 제초제가 뿌려져 있다면 감소 (건물-벽은 절대 0이 되지않음)
                board[r][c] += 1

    # [1] 인접한 네칸 중 나무있는 칸 수만큼 동시 성장
    nboard = [x[:] for x in board]
    for r in range(1,N+1):
        for c in range(1,N+1):
            if board[r][c] > 0: # 나무가 있다면 인접 나무수만큼 성장
                for nr,nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if board[nr][nc] > 0:
                        nboard[r][c] += 1
    board = nboard

    # [2] 인접한 빈칸에 번식 (나무수 // 빈칸수 -> 동시)
    nboard = [x[:] for x in board]
    for r in range(1,N+1):
        for c in range(1,N+1):
            if board[r][c] > 0: # 내가 나무면 번식
                tlst = [] # 빈칸 좌표 저장
                for nr,nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if board[nr][nc] == 0:
                        tlst.append((nr,nc))
                if len(tlst) > 0: #빈 칸이 있는 경우 -> 번식
                    d = board[r][c] // len(tlst)
                    for tr,tc in tlst:
                        nboard[tr][tc] += d
    board = nboard

    # [3-1] 가장 많이 박멸되는 칸 찾기
    mx,mx_r,mx_c = 0,0,0
    for r in range(1,N+1):
        for c in range(1,N+1):
            if board[r][c] > 0: # 나무 있는 칸에 뿌려야 제초제 확산됨
                cnt = board[r][c] # 내 자리 포함
                for dr,dc in ((-1,-1),(-1,1),(1,-1),(1,1)):
                    for k in range(1,K+1): # 뻗어가면서 처리
                        nr,nc = r + dr*k, c + dc*k
                        if board[nr][nc] <= 0: # 빈 땅 제초제 건물
                            break # stop
                        else: # 나무 있는 경우
                            cnt += board[nr][nc]
                # 최댓값이면 갱신
                if cnt > mx:
                    mx,mx_r,mx_c = cnt,r,c
    # 제거할 나무가 하나도 없는것 -> break
    if mx == 0:
        break
    ans += mx

    # [3-2] 제초제 살포
    # 전파도중 벽이 있거나 나무가 아예 없는 칸이 있는 경우,
    # 그 칸까지는 제초제가 뿌려지고 이후의 칸으로는 제초제가 전파되지 않음
    board[mx_r][mx_c] = C # 중앙 자리에 제초제 뿌림
    for dr,dc in ((-1,-1),(-1,1),(1,-1),(1,1)):
        for k in range(1,K+1): # 뻗어가면서 처리하기
            nr,nc = mx_r + dr * k, mx_c + dc * k
            # 벽에 제초제 뿌린 뒤 건물이 시간지나면 빈땅이됨
            if board[nr][nc] <= 0: # 뻗어나가는 것이 종료되느 ㄴ조건: 빈땅, 제초제 뿌려진 빈땅 그리고 벽을 제외
                if board[nr][nc] >= C:
                    board[nr][nc] = C #뿌리고
                break
            else: # 나무면
                board[nr][nc] = C
print(ans)