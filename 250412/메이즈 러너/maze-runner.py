N,M,K = map(int,input().split()) 

board = [list(map(int,input().split())) for _ in range(N)] 
for _ in range(M): 
    r,c = map(int,input().split()) 
    board[r-1][c-1] -= 1 

er,ec = map(lambda x: int(x)-1,input().split())
board[er][ec] = -11 

def find_square(arr): 
    # 정사각형 길이 찾기
    # 출구와 모든 사람들 간 최단거리 구하기 
    mn = N 
    for r in range(N): 
        for c in range(N): 
            if -11 < arr[r][c] < 0:
                mn = min(mn,max(abs(er-r),abs(ec-c)))
    
    # 
    for sr in range(N-mn): 
        for sc in range(N-mn): 
            # 찾은 최소 사각형 내에 출구가 있따면
            if sr <= er <= sr + mn and sc <= ec <= sc + mn:
                # 사람도 있는지 확인해야지 
                for r in range(sr,sr+mn+1): 
                    for c in range(sc,sc+mn+1): 
                        if -11 < arr[r][c] < 0: 
                            return sr,sc,mn+1
    
    
def find_exit(board): 
    for r in range(N): 
        for c in range(N): 
            if board[r][c] == -11: 
                return r,c 
def in_range(r,c): 
    return 0<=r<N and 0<=c<N 
cnt = M 
ans = 0 
for _ in range(K): 
    # [1] 모든 참가자 동시에 한칸 이동 
    # 출구로 향하는 최단거리 방향
    # 출구 도착시 즉시 탈출 
    nboard = [x[:] for x in board] 
    for r in range(N): 
        for c in range(N): 
            if -11 < nboard[r][c] < 0: 
                dist = abs(er-r) + abs(ec-c) 
                for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)): 
                    nr,nc = r + dr, c + dc 
                    if in_range(nr,nc) and dist > (abs(nr-er)+abs(nc-ec)): 
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
    
    # [2] 미로회전 
    # 출구와 한 명 이상 참가자를 포함 
    # 시계 방향 90도 
    sr,sc,L = find_square(board) 
    
    for r in range(L): 
        for c in range(L): 
            nboard[sr+r][sc+c] = board[sr+L-c-1][sc+r] 
            if nboard[sr+r][sc+c] > 0: 
                nboard[sr+r][sc+c] -= 1
    board = nboard
    # 회전으로 출구 바뀌었으니 업뎃 
    er,ec = find_exit(board)
print(-ans) 
print(er+1,ec+1)