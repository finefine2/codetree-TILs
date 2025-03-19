# import sys
# sys.stdin = open("input.txt","r")

drs,dcs = [-1,-1,0,1,1,1,0,-1],[0,-1,-1,-1,0,1,1,1]

def in_range(r,c):
    return 0<=r<4 and 0<=c<4

def find(idx,v):
    for i in range(4):
        for j in range(4):
            if v[i][j][0] == idx: # 찾던 체스 번호면
                return i,j,v[i][j][1]
def dfs(sr,sc,sd,sm,v):
    global ans
    #[0] 정답 갱신: 종료조건 n 관련 명확하지 않음
    ans = max(ans,sm)
    # [1] 체스 이동 (1~16): 기준은 v[]이므로 r,c 좌표를 검색해야 함
    for idx in range(1,17):
        cr,cc,cd = find(idx,v)
        if cd == -1: continue # 체스가 없는 경우 스킵
        for j in range(8): # 현재 방향부터 8방향체크
            td =(cd+j) % 8
            nr,nc = cr+drs[td],cc+dcs[td]
            # 범위 내이고 술래가 아니면(빈칸 혹은 체스)
            if in_range(nr,nc) and (nr,nc) != (sr,sc):
                v[cr][cc][1] = td # 방향 적용 후 교환
                v[cr][cc],v[nr][nc] = v[nr][nc],v[cr][cc]
                break
    # [2] 술래의 이동 (1~3칸: 범위내이고 빈칸 아니면 이동)
    for mul in range(1,4):
        nr,nc = sr + drs[sd] * mul, sc + dcs[sd] * mul
        if in_range(nr,nc) and v[nr][nc][1] != -1:
            fn,fd = v[nr][nc]
            v[nr][nc][1] = -1 # 잡힘 처리
            nv = [[x[:] for x in lst] for lst in v] # 보드 복사

            dfs(nr,nc,fd,sm+fn,nv)
            v[nr][nc][1] = fd  # 원상복구
# [0] 체스 입력, v[] 초기화
v = [[[0] *2 for _ in range(4)] for _ in range(4)]
for i in range(4):
    chess_lst = list(map(int,input().split()))
    for j in range(4):
        v[i][j] = [chess_lst[j*2],chess_lst[j*2+1]-1]

# [1] 술래가 초기 위치 잡음
ans = 0
sn,sd = v[0][0]  # 술래 잡는 처리 주의 (방향.. =-1)
v[0][0][1] = -1  # (0,0)위치 잡힘 처리
dfs(0,0,sd,sn,v) # 술래위치, 방향, 초기점수, v[]전달
print(ans)