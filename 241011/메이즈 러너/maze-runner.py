# pythonic 보면서 구현하기
# board에 뭘 기록할지?
N,M,K = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
for _ in range(M):
    r,c = tuple(map(int,input().split()))
    r-=1
    c-=1
    board[r][c] -= 1 # 사람은 -1 같은 위치에 여러 명 둘 수 있음
er,ec = tuple(map(int,input().split()))
er -= 1
ec -= 1
board[er][ec] = -11 # 비상구

def find_square(board):
    # [1] 비상구와 모든 사람간 가장 짧은 가로 혹은 세로거리 구하기
    L = N
    for r in range(N):
        for c in range(N):
            if -11 < board[r][c] < 0: #사람인 경우
                L = min(L,max(abs(er-r),abs(ec-c)))
    # [2] 0,0부터 순회하면서 길이 L인 정사각형에 사람있는지 확인하기
    for sr in range(N-L):
        for sc in range(N-L):
            if sr<=er<=sr+L and sc<=ec<=sc+L: # 비상구가 포함
                for r in range(sr,sr+L+1):
                    for c in range(sc,sc+L+1):
                        if -11<board[r][c]<0: #사람의 경우 리턴
                            return sr,sc,L+1

def find_exit(board):
    for r in range(N):
        for c in range(N):
            if board[r][c] == -11:
                return r,c
# K turn 혹은 모두 탈출까지 모든 사람의 이동거리 누적, 모두 탈출하면 종료
ans = 0
cnt = M
for _ in range(K):
    # [1] 모든 참가자가 동시에 한칸 이동 출구쪽 최단거리, 상/하 우선
    # 출구 도착하면 즉시 아웃
    nboard = [x[:] for x in board]
    for r in range(N):
        for c in range(N):
            if -11 < board[r][c] < 0: # 사람인 경우
                dist = abs(er-r) + abs(ec-c)
                # 4 방향(상하우선), 범위내, 벽이 아니고, 거리가 dist보다 작으면
                for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                    nr,nc = r + dr, c + dc
                    if 0<=nr<N and 0<=nc<N and board[nr][nc] <= 0 and dist > (abs(er-nr) + abs(ec-nc)):
                        ans += board[r][c] # 현재 인원수가 이동하므로 이동거리 누적
                        nboard[r][c] -= board[r][c] # 이동처리
                        if board[nr][nc] == -11: # 비상구라면
                            cnt += board[r][c] # 탈출시키기
                        else: #일반 빈칸 혹은 사람이 있으면
                            nboard[nr][nc] += board[r][c]
                        break
    board = nboard
    if cnt == 0:
        break

    #[2] 미로회전(출구와 한명이상 참가자를 포함하는 가장작은 정사각형)
    # 시계 90도회전: 같은 크기 -> 좌상단, 내구도 -1
    sr,sc,L = find_square(board)
    nboard = [x[:] for x in board]
    for r in range(L):
        for c in range(L):
            nboard[sr+r][sc+c] = board[sr+L-c-1][sc+r]
            if nboard[sr+r][sc+c] > 0:
                nboard[sr+r][sc+c] -= 1
    board = nboard
    # 회전했으므로 비상구 위치도 업데이트를 해준다
    er,ec = find_exit(board)
print(-ans)
print(er+1,ec+1)