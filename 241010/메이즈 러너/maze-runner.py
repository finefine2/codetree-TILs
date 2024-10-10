# 보면서 구현하는 것
# 다만 사람 여러명일때 어떻게 관리를 해야할지에 대한 고민을 하면 좋을듯 
# 3차원 board에 담을지 아니면, 사람 dict를 활용할지, 혹은 2차원 board에 계속해서 누적되는 방향으로 갈지 
N,M,K = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
for _ in range(M):
    r,c = tuple(map(int,input().split()))
    r -= 1
    c -= 1
    board[r][c] = -1 # 사람을 -1로 처리 (같은 위치에 여러명 있을 수 있음)

er,ec = tuple(map(int,input().split()))
er -= 1
ec -= 1
board[er][ec] = -11 # 비상구 -11

def find_exit(arr):
    for r in range(N):
        for c in range(N):
            if arr[r][c] == -11:
                return r,c
def find_square(arr):
    # [1] 비상구와 모든 사람 간의 가장 짧은 가로 혹은 세로 거리 구하기
    L = N
    for r in range(N):
        for c in range(N):
            if -11 < arr[r][c] < 0: # 사람인 경우
                L = min(L,max(abs(er-r),abs(ec-c)))
    # [2] (0,0)부터 순회하며 길이 L 정사각형에 비상구와 사람있는지 체크 -> 리턴 L+1
    for sr in range(N-L):
        for sc in range(N-L): # 가능한 모든 시작위치
            if sr <= er <= sr + L and sc <= ec <= sc + L: # 비상구가 포함된 사각형
                for r in range(sr,sr+L+1):
                    for c in range(sc,sc+L+1):
                        if -11 < arr[r][c] < 0:
                            #사람인 경우 리턴
                            return sr,sc,L+1

# K turn 혹은 모두 탈출까지의 모든 사람의 이동거리 누적, 모두 탈출하면 종료
ans = 0
cnt = M
for _ in range(K):
    # [1] 모든 참가자가 동시에 한 칸 이동한다 (출구 최단거리 방향 상,하 우선)
    # 출구 도착시 즉시 탈출
    nboard = [x[:] for x in board]
    for r in range(N):
        for c in range(N):
            if -11 < board[r][c] < 0: # 사람의 경우
                dist = abs(er-r) + abs(ec-c)
                # 4방향(상하우선), 범위내, 벽 아니고 <=0 거리가 dist보다 작음
                for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                    nr,nc = r + dr, c + dc
                    if 0<=nr<N and 0<=nc<N and board[nr][nc] <= 0 and dist > (abs(er-nr)+abs(ec-nc)):
                        ans += board[r][c] # 현재 인원수가 이동하므로 이동거리에 누적
                        nboard[r][c] -= board[r][c] # 이동처리
                        if board[nr][nc] == -11: #비상구에 도착
                            cnt += board[r][c] # escape
                        else: # 일반 빈칸 또는 사람 있는 자리
                            nboard[nr][nc] += board[r][c] # 들어온 인원 추가
                        break
    board = nboard
    if cnt == 0:
        break # M명 모두 탈출하면 그 즉시 끝

    # [2] 미로회전 (출구와 한 명 이상 참가자를 포함하는 가장 작은 정사각형)
    # 시계방향 90도: 같은 크기 -> 좌상단행렬, 내구도 -1
    sr,sc,L = find_square(board)
    nboard = [x[:] for x in board]
    for r in range(L):
        for c in range(L):
            nboard[sr+r][sc+c] = board[sr+L-1-c][sc+r]
            if nboard[sr+r][sc+c] > 0: #벽이면 회전시 1감소
                nboard[sr+r][sc+c] -= 1
    board = nboard
    # 회전으로 달라졌으므로 비상구 위치 저장
    er,ec = find_exit(board)
print(-ans)
print(er+1,ec+1)