# 중력 처리 + bfs 변형 
from collections import deque
N,M = tuple(map(int,input().split()))
EMPTY = M+1
# -1 black, 0 red, 1~m color
# 4방향을 -1로 둘러싸기 (범위체크 필요없음)
board = [[-1] * (N+2)] + [[-1] + list(map(int,input().split())) + [-1] for _ in range(N)] + [[-1] * (N+2)]

def get_base(group):
    base_r, base_c = -1, N+1
    for (r,c) in group:
        if board[r][c] != 0: 
            if base_r < r or (base_r == r and base_c > c):
                base_r,base_c = r,c
    return base_r,base_c
ans = 0
# 가장 큰 폭탄묶음을 찾아야한다
# 미방문 일반블럭에서 bfs 확산 (가장 큰 묶음 찾기)
def bfs():
    v = [[0] * (N+2) for _ in range(N+2)]
    mx_group = set()
    tlst = []
    for r in range(1,N+1):
        for c in range(1,N+1):
            if v[r][c] == 0 and M >= board[r][c] > 0: # 일반 색깔 폭탄에 대해서만 조사를 해보자고
                q = deque()
                groups = set() # 같은 그룹이면 추가하기

                v[r][c] = 1
                groups.add((r,c))
                q.append((r,c))
                r_cnt = 0 # 빨간 폭탄 세는 거
                color = board[r][c]
                while q:
                    cr,cc = q.popleft()
                    for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                        nr,nc = cr + dr, cc + dc
                        # 4방향, 미방문(일반블럭 혹은 빨강), 같은 색 혹은 빨강
                        if v[nr][nc] == 0 and (nr,nc) not in groups and (board[nr][nc] == color or board[nr][nc] == 0):
                            groups.add((nr,nc))
                            q.append((nr,nc))
                            if board[nr][nc] == 0: # 빨강이면
                                r_cnt += 1
                            else: # 일반블럭이면
                                v[nr][nc] = 1

                base_r,base_c = get_base(groups)
                tlst.append((len(groups),r_cnt,base_r,base_c,groups))
                # 그룹개수가 클수록, 빨강폭탄은 적을수록, 행은 클수록, 열은 작을수록 
                if len(tlst) > 0:
                    tlst.sort(key=lambda x:(-x[0],x[1],-x[2],x[3]))
                    mx_group = tlst[0][-1]
    return mx_group

def gravity():
    # 전체 블럭을 순회
    for r in range(1,N):
        for c in range(1,N+1):
            cr,cc = r,c
            # 내 위치이고, 아래칸이 빈칸이면 교환 (위로 반복) )
            while 0<=board[cr][cc]<=M and board[cr+1][cc] == EMPTY:
                board[cr][cc],board[cr+1][cc] = board[cr+1][cc],board[cr][cc]
                cr -= 1
while True:
    # 미방문 일반블럭 기준으로 블럭그룹 찾기 
    bomb_group = bfs()
    # 선택한 그룹개수가 2개미만이면 종료
    if len(bomb_group) < 2:
        break
    ans += len(bomb_group) ** 2
    # 선택한 블럭 삭제 (점수에 추가)
    for br,bc in bomb_group:
        board[br][bc] = EMPTY
    # 중력
    gravity()
    # 반시계 90도 회전
    board = list(map(list,zip(*board)))[::-1]
    # 중력
    gravity()
print(ans)