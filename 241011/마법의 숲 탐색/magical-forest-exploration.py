# 조건 - 문제 설명대로 보면서 디버깅
# bfs 활용 2차원 보드를 탐색
R,C,K = tuple(map(int,input().split()))
units = [list(map(int,input().split())) for _ in range(K)]  # sr sc dr
board = [[1] + [0] * C + [1] for _ in range(R+3)] + [[1] * (C+2)]
exit_set = set()

# U R D L
drs,dcs = [-1,0,1,0],[0,1,0,-1]
from collections import deque
def bfs(sr,sc):
    q = deque()
    v = [[0] * (C+2) for _ in range(R+4)]
    mx_r = 0

    q.append((sr,sc))
    v[sr][sc] = 1

    while q:
        cr,cc = q.popleft()
        mx_r = max(mx_r,cr)
        # 4 방향, 미방문, 조건: 같은값 또는 내가 출구 - 상대방이 골렘
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr,nc = cr + dr, cc + dc
            if v[nr][nc] == 0 and (board[cr][cc] == board[nr][nc] or ((cr,cc) in exit_set and board[nr][nc] > 1)):
                q.append((nr,nc))
                v[nr][nc] = 1
    return mx_r - 2
ans = 0
num = 2
# 골렘 입력 좌표 / 방향에 따라 남쪽 이동 및 정령 최대좌표 계산 및 누적
for cc,dr in units:
    cr = 1
    # [1] 남쪽으로 최대한 이동 ( 남 - 서 - 동)
    while True:
        # 남쪽으로 한칸 이동
        if board[cr+1][cc-1] +board[cr+2][cc] + board[cr+1][cc+1] == 0: # 비어있음
            cr += 1
        # west
        elif board[cr-1][cc-1] + board[cr][cc-2] + board[cr+1][cc-1] + board[cr+1][cc-2] + board[cr+2][cc-1] == 0:
            cr += 1
            cc -= 1
            dr = (dr-1) % 4
        # east
        elif board[cr-1][cc+1] + board[cr][cc+2] + board[cr+1][cc+1] + board[cr+1][cc+2] + board[cr+2][cc+1] == 0:
            cr += 1
            cc += 1
            dr = (dr+1) % 4
        else:
            break
    if cr < 4: # 몸이 범위밖(새롭게 탐색, board 초기화)
        board = [[1] + [0] * C + [1] for _ in range(R+3)] + [[1] * (C+2)]
        exit_set = set()
        num = 2
    else:
        # 골렘을 표시하고 비상구위치 추가
        board[cr+1][cc] = num
        board[cr-1][cc] = num
        board[cr][cc-1] = num
        board[cr][cc] = num
        board[cr][cc+1] = num
        num += 1

        exit_set.add((cr+drs[dr],cc+dcs[dr]))
        ans += bfs(cr,cc)
print(ans)