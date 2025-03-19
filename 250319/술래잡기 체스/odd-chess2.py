drs,dcs = [-1,-1,0,1,1,1,0,-1],[0,-1,-1,-1,0,1,1,1]
#
def in_range(r,c):
    return 0<=r<4 and 0<=c<4
#
def find(idx,v):
    for i in range(4):
        for j in range(4):
            if v[i][j][0] == idx: # 찾던 체스 번호면
                return i,j,v[i][j][1]
def dfs(sr,sc,sd,sm,board):
    global ans
      #[0] 정답 갱신: 종료조건 n 관련 명확하지 않음
    ans = max(ans,sm)
      # [1] 체스 이동 (1~16): 기준은 v[]이므로 r,c 좌표를 검색해야 함
    for idx in range(1,17):
        cr,cc,cd = find(idx,board)
        if cd == -1: continue # 체스가 없는 경우 스킵
        for i in range(8): # 현재 방향부터 8방향체크
            nd = (cd + i) % 8 # 범위 내이고 술래가 아니면(빈칸 혹은 체스)
            nr,nc = cr + drs[nd], cc + dcs[nd]
            if in_range(nr,nc) and nd != -1:
                board[cr][cc][1] = nd # 방향 적용해준 뒤에 교환할 것
                board[nr][nc],board[cr][cc] = board[cr][cc],board[nr][nc]
                break
    # [2] 술래의 이동 (1~3칸: 범위내이고 빈칸 아니면 이동)
    for mul in range(1,4):
        nr,nc = sr + drs[sd] * mul, sc + dcs[sd] * mul
        if in_range(nr,nc) and board[nr][nc][1] != -1:
            tn,td = board[nr][nc]
            board[nr][nc][1] = -1 # 잡힘 처리
            nboard = [[x[:] for x in lst] for lst in board]
            dfs(nr,nc,td,sm+tn,nboard)# [0] 체스 입력, v[] 초기화
            board[nr][nc][1] = td #원상복구
board = [[[0]*2 for _ in range(4)] for _ in range(4)]
for i in range(4):
    chess_lst = list(map(int,input().split()))
    for j in range(4):
        board[i][j] = [chess_lst[2*j],chess_lst[2*j+1]-1]

# [1] 술래가 초기 위치 잡음
ans = 0
n, d = board[0][0]
board[0][0][1] = -1 # 술래 잡는 처리 주의 (방향.. =-1)
dfs(0,0,d,n,board) # 술래위치, 방향, 초기점수, v[]전달
print(ans)



