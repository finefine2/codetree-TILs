# 시뮬레이션 -> 시키는대로
# 같은값 n개이상인 블럭 bfs 돌려서 묶기
K,M = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(5)]
treasures = list(map(int,input().split()))
ans = []
def rotate(board,sr,sc): # 90 도 부분회전
    nboard = [x[:] for x in board]
    for r in range(3):
        for c in range(3):
            nboard[sr+r][sc+c] = board[sr+3-c-1][sc+r]
    return nboard
def bfs(board,v,sr,sc,clr):
    q = []
    sset = set() # 같은 유물로 묶이는 좌표들인데, 중복방지
    cnt = 0
    drs,dcs = [1,0,-1,0],[0,1,0,-1]

    q.append((sr,sc))
    v[sr][sc] = 1
    sset.add((sr,sc))
    cnt += 1
    while q:
        cr,cc = q.pop(0)
        # 4방향, 범위내, 미방문, 조건: 같은 값이면
        for dr,dc in zip(drs,dcs):
            nr,nc = cr + dr, cc + dc
            if 0<=nr<5 and 0<=nc<5 and v[nr][nc] == 0 and board[cr][cc] == board[nr][nc]:
                q.append((nr,nc))
                v[nr][nc] = 1
                sset.add((nr,nc))
                cnt += 1

    # cnt 개수가 3개이상이면 유물이고, clr가 필요할때만 0으로 클리어하는 게 조건
    if cnt >= 3: # 유물이면
        if clr == 1: #0으로 초기화해야하는 경우
            for r,c in sset:
                board[r][c] = 0
        return cnt
    else: # 3개미만이면
        return 0


def count_clear(board,clr):  #clr = 1인 경우 3 개이상의 값들을 0으로
    v = [[0] * 5 for _ in range(5)]
    cnt = 0
    for r in range(5):
        for c in range(5): # 미방문인 경우에 대해서만
            if v[r][c] == 0:
                # 같은 값이면 3개이상인 경우에만
                t = bfs(board,v,r,c,clr)
                cnt += t
    return cnt
# k턴을 진행한다. 만약 유물이 없으면 즉시종료
for _ in range(K):
    # [1] 탐사진행
    mx_cnt = 0
    for rot in range(1,4):
        for sc in range(3):
            for sr in range(3):
                # rot 횟수만큼 90도 시계방향 회전
                nboard = [x[:] for x in board]
                for _ in range(rot):
                    nboard = rotate(nboard,sr,sc)
                # 유물개수 카운트
                t = count_clear(nboard,0)
                if t > mx_cnt:
                    mx_cnt = t
                    mboard = nboard
    # 유물이 없는 경우 즉시 종료
    if mx_cnt == 0:
        break

    # [2] 연쇄획득
    cnt = 0
    board = mboard
    while True:
        t = count_clear(board,1)
        if t == 0:
            break # 연쇄 획득 종료 -> 다음 턴
        cnt += t # 획득한 유물 개수 누적
        # arr의 0인 부분 리스트에서 순서대로 채워넣기
        for c in range(5):
            for r in range(4,-1,-1):
                if board[r][c] == 0:
                    board[r][c] = treasures.pop(0)
    ans.append(cnt) # 이번 턴 연쇄획득한 개수를 추가


for a in ans:
    print(a,end=" ")