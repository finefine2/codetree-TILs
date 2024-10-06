from collections import deque


R,C,K = tuple(map(int,input().split()))

golems = []
for _ in range(K):
    cc,dr = tuple(map(int,input().split()))
    golems.append((cc,dr))

board = [[-1] + [0] * C + [-1] for _ in range(R+3)] +[[-1] * (C+2)]
# 마지막에 도달하는 최대 행의 값
ans = 0
# N E S W
drs,dcs = [-1,0,1,0],[0,1,0,-1]
exit_set = set()
num = 2


def bfs(sr,sc):
    q = deque()
    v = [[0] * (C+2) for _ in range(R+4)]

    q.append((sr,sc))
    v[sr][sc] = 1
    max_r = 0
    while q:
        cr,cc = q.popleft()
        max_r = max(cr,max_r)

        # 미방문, 4방향, and 내가 만약 출구 좌표이고 다른 골렘과 인접했다면 이동
        for dr,dc in zip(drs,dcs):
            nr,nc = cr + dr, cc + dc
            if not v[nr][nc] and(board[cr][cc] == board[nr][nc] or ((cr,cc) in exit_set and board[nr][nc] > 1)):
                q.append((nr,nc))
                v[nr][nc] = 1
    return max_r - 2
# 일단은 모든 골렘을 움직인다
for cc,dr in golems:
    cr = 1 # 시작 행의 좌표 (정령)
    while True:
        # 일단 남쪽으로 쭉 내려간다
        # 출구 방향은 그대로 유지
        if board[cr+2][cc] + board[cr+1][cc+1] + board[cr+1][cc-1] == 0:
            cr += 1
        # 서쪽으로 회전한다
        elif board[cr][cc-2] + board[cr-1][cc-1] + board[cr+1][cc-1] + board[cr+1][cc-2] + board[cr+2][cc-1] == 0:
            cr += 1
            cc -= 1
            dr = (dr-1) % 4
        # 동쪽으로 회전하며 내려온다
        elif board[cr-1][cc+1] + board[cr][cc+2] + board[cr+1][cc+1] + board[cr+1][cc+2] + board[cr+2][cc+1] == 0:
            cr += 1
            cc += 1
            dr = (dr+1) % 4
        # 만약 더 이상 이동 못하는것일듯
        else:
            break

    # 만약 맵 바깥이라면 보드를 초기화 하자
    if cr < 4:
        board = [[-1] + [0] * C + [-1] for _ in range(R + 3)] + [[-1] * (C + 2)]
        exit_set = set()
        num = 2
    else: # 그게 아니라면 현재 보드 값들을 업데이트해주기
        # board값에 업데이트 및 출구 위치 또한 표기해준다
        board[cr][cc] = num
        board[cr-1][cc] = num
        board[cr][cc-1] = num
        board[cr][cc+1] = num
        board[cr+1][cc] = num
        exit_set.add((cr+drs[dr],cc+dcs[dr]))
        num += 1
        ans += bfs(cr,cc)
print(ans)