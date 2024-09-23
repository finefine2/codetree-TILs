N,M,K = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
for i in range(M):
    r,c = tuple(map(int,input().split()))
    board[r-1][c-1] = -1
e_r,e_c = tuple(map(int,input().split()))
e_r -= 1
e_c -= 1


def find_square(arr):
    # [1] 비상구와 모든 사람간의 가장 짧은 가로 혹은 세로거리 구하기
    mn = N
    for r in range(N):
        for c in range(N):
            if -11 < arr[r][c] <0:
                mn = min(mn,max(abs(e_r-r),abs(e_c-c)))
    # [2] (0,0) 부터 순회하면서 길이 L인 정사각형에 비상구와 사람이 있나 체크
    # 가능한 모든 시작위치
    for sr in range(N-mn):
        for sc in range(N-mn):
            if sr<=e_r<=sr+mn and sc<=e_c<=sc+mn: # 비상구가 포함된 사각형
                for r in range(sr,sr+mn+1):
                    for c in range(sc,sc+mn+1):
                        if -11 < board[r][c] < 0:
                            return sr,sc,mn+1
                        
def find_exit(arr): 
    for r in range(N): 
        for c in range(N): 
            if arr[r][c] == -11: 
                return r,c 
ans = 0
cnt = M
drs,dcs = [-1,1,0,0],[0,0,-1,1]
for _ in range(K):
    # [1] 모든 참가자 동시에 한 칸 이동 (출구 최단거리 방향 상/하 우선)
    # 출구 도달시 즉시 탈출
    nboard = [x[:] for x in board]

    for r in range(N):
        for c in range(N):
            # 사람인 경우
            if -11 < board[r][c] < 0:
                dist = abs(e_r-r) + abs(e_c-c)
                for dr,dc in zip(drs,dcs):
                    nr,nc = r + dr, c + dc
                    if 0<=nr<N and 0<=nc<N and board[nr][nc] <=0 and dist > (abs(e_r-nr)+abs(e_c-nc)):
                        ans += board[r][c]
                        nboard[r][c] -= board[r][c]
                        if board[nr][nc] == -11:
                            cnt += board[r][c]
                        else:
                            nboard[nr][nc] += board[r][c]
                        break
    board = nboard
    if cnt==0:
        break

    # [2] 미로회전
    # 90 rotate
    sr,sc,L = find_square(board)
    nboard = [x[:] for x in board]
    for r in range(L):
        for c in range(L):
            nboard[sr+r][sc+c] = board[sr+L-c-1][sc+r]
            if nboard[sr+r][sc+c] > 0:
                nboard[sr+r][sc+c] -= 1
    board = nboard
    e_r,e_c = find_exit(board)
print(-ans)
print(e_r+1,e_c+1)