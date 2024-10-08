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


ans = 0 
cnt = M 

def find_exit(board): 
    for r in range(N): 
        for c in range(N): 
            if board[r][c] == -11: 
                return r,c 

# 최소 정사각형 찾기 
def find_square(board): 
    # 한명 이상의 출구와 참가자를 포함한 정사각형 
    L = N 
    for r in range(N): 
        for c in range(N): 
            if -11<board[r][c]<0: 
                L = min(L, max(abs(er-r),abs(ec-c)))
    # 최단거리를 찾았으니 이제 시작좌표를 구해볼 시간임 
    for sr in range(N-L): 
        for sc in range(N-L): 
            # 출구가 포함되어있나?
            if sr<=er<=sr+L and sc<=ec<=sc+L: 
                # 참가자도 있나 
                for r in range(sr+L+1): 
                    for c in range(sc+L+1): 
                        if -11<board[r][c]<0: 
                            return sr,sc,L+1

for _ in range(K): 
    nboard = [x[:] for x in board]
    # 모든 참가자가 이동한다 
    for r in range(N): 
        for c in range(N): 
            if -11 < board[r][c] < 0: 
                dist = abs(er-r) + abs(ec-c) 
                for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)): 
                    nr,nc = r + dr, c + dc 
                    if 0<=nr<N and 0<=nc<N and board[nr][nc] <= 0 and (abs(nr-er)+abs(nc-ec) < dist): 
                        ans += board[r][c] # 이동한 참가자수만큼 거리 플러스 
                        nboard[r][c] -= board[r][c] #nboard는 board를 복사한 놈이기 때문에 지워도 됨 
                        if (nr,nc) == (er,ec): # 만약 출구에 도달했다면 
                            cnt += board[r][c] 
                        else: # 출구가 아니라 일반 칸 이라면 
                            nboard[nr][nc] += board[r][c] 
                        break 
    board = nboard

    if cnt == 0: 
        break 
    # 최소 정사각형을 찾는다 
    sr,sc,L = find_square(board) 
    # 최소 정사각형을 회전시키고 회전된 벽은 -1을 한다 
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