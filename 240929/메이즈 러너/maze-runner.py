N,M,K = tuple(map(int,input().split())) 
board = [list(map(int,input().split())) for _ in range(N)] 

for _ in range(M): 
    r,c = tuple(map(int,input().split()))
    r -= 1 
    c -= 1 
    board[r][c] -= 1 
er,ec = tuple(map(int,input().split())) 
er -= 1 
ec -= 1 
board[er][ec] = -11 

def find_square(board): 
    #[1] 비상구와 모든 사람간 가장 짧은 가로 혹은 세로거리 
    min_dist = N 
    for r in range(N): 
        for c in range(N): 
            if -11<board[r][c]<0: 
                min_dist = min(min_dist,max(abs(er-r),abs(ec-c)))
    # [2] 0,0부터 순회하면서 길이 L인 정사각형에 비상구와 사람있나 체크 
    for sr in range(N-min_dist): 
        for sc in range(N-min_dist): 
            if sr<=er<=sr+min_dist and sc<=ec<=sc+min_dist: 
                for r in range(sr,sr+min_dist+1): 
                    for c in range(sc,sc+min_dist+1): 
                        if -11<board[r][c]<0: 
                            return sr,sc,min_dist+1 
def find_exit(board): 
    for r in range(N): 
        for c in range(N): 
            if board[r][c]==-11: 
                return r,c

ans = 0 
cnt = M 
drs,dcs = [-1,1,0,0],[0,0,-1,1]
# k턴 또는 모두 탈출할 때까지 모든 사람의 이동거리 누적, 모두 탈출하면 끝 
for _ in range(K): 
    # [1] 모든 참가자 동시에 한 칸 이동 
    # 출구 도착하면 탈출 
    nboard = [x[:] for x in board] 
    for r in range(N): 
        for c in range(N): 
            if -11<board[r][c]<0: 
                dist = abs(er-r) + abs(ec-c) 
                for dr,dc in zip(drs,dcs): 
                    nr,nc = r + dr, c + dc
                    if 0<=nr<N and 0<=nc<N and board[nr][nc] <= 0 and dist > (abs(er-nr)+abs(ec-nc)): 
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

    # [2] 미로회전 (출구와 한명 이상 참가자 포함하는 가장 작은 정사각형) 
    # 시계방향 90도 
    sr,sc,L = find_square(board) 
    nboard = [x[:] for x in board] 
    for r in range(L): 
        for c in range(L): 
            nboard[sr+r][sc+c] = board[sr+L-1-c][sc+r] 
            if nboard[sr+r][sc+c] > 0: 
                nboard[sr+r][sc+c] -= 1 
    board = nboard
    er,ec = find_exit(board) 
print(-ans) 
print(er+1,ec+1)