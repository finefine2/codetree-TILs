N,M,K = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]

for _ in range(M):
    r,c = map(int,input().split())
    board[r-1][c-1] -= 1

er,ec = map(int,input().split())
er -= 1
ec -= 1
board[er][ec] = -11

def find_square(arr):
    # sr,sc,L
    mn = 2 * N
    for r in range(N):
        for c in range(N):
            if -11 < arr[r][c] < 0:
                mn = min(mn,max(abs(er-r),abs(ec-c)))

    # mn을 찾았으면 이제 참가자 한명 포함하는 정사각형 찾기
    for sr in range(N-mn):
        for sc in range(N-mn):
            if sr <= er <= sr+mn and sc <= ec <= ec + mn:
                for r in range(sr,sr+mn+1):
                    for c in range(sc,sc+mn+1):
                        if -11 < arr[r][c] < 0:
                            return sr,sc, mn+1
def find_exit(arr):
    for r in range(N):
        for c in range(N):
            if arr[r][c] == -11:
                return r,c
def in_range(r,c):
    return 0<=r<N and 0<=c<N
# 모든 참가자 동시 움직인다 -> nboard
cnt = M
ans = 0
# 모든 참가자 탈출 시 break
for _ in range(K):
    nboard = [x[:] for x in board]
    # 1 모든 참가자가 한칸씩 동시에 움직임
        # 상하 좌우
        # 현재 거리보다
        # 벽 없는 곳으로 이동
    for r in range(N):
        for c in range(N):
            if -11<board[r][c]<0:
                dist = abs(er-r) + abs(ec-c)
                for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                    nr,nc = r + dr, c + dc
                    if in_range(nr,nc) and board[nr][nc] <= 0 and dist > (abs(er-nr)+abs(ec-nc)):
                        ans += board[r][c]
                        nboard[r][c] -= board[r][c]
                        if board[nr][nc] == -11:
                            cnt += board[r][c]
                        else:
                            nboard[nr][nc] += board[r][c]
                        break
    board = nboard
    if cnt == 0:
        break

    # 미로 회전
    # 참가자와 출구 찾는 가장 작은 정사각형 찾기
    sr,sc,L = find_square(board)
    nboard = [x[:] for x in board]
    for r in range(L):
        for c in range(L):
            nboard[sr+r][sc+c] = board[sr+L-c-1][sc+r]
            if nboard[sr+r][sc+c] > 0:
                nboard[sr+r][sc+c] -= 1
    board = nboard

    er,ec = find_exit(board)

print(-ans)
print(er+1,ec+1) 