# 단골 부분 회전 
# 마찬가지로 어떻게 맞닿은 면에 대한 계산을 할 것인지 생각을 해볼것

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
M = N // 2

from collections import deque
def bfs(sr,sc):
    q = deque()

    q.append((sr,sc))
    v[sr][sc] = 1
    groups[-1].add((sr,sc))

    while q:
        cr,cc = q.popleft()
        for nr,nc in ((cr-1,cc),(cr+1,cc),(cr,cc-1),(cr,cc+1)):
            # 4방향, 범위내, 미방문 같은 값?
            if 0<=nr<N and 0<=nc<N and v[nr][nc] == 0 and board[nr][nc] == board[cr][cc]:
                q.append((nr,nc))
                v[nr][nc] = 1
                groups[-1].add((nr,nc)) 
ans = 0
for k in range(4):
    #[1] 예술 점수 구하기, 그룹을 나누고 가능한 2그룹의 점수 누적
    groups = []
    nums = []
    # [1-1] 미방문 숫자를 만나면 bfs - 같은 그룹 좌표를 set에 추가하기
    v = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if v[r][c] == 0: # 미방문
                groups.append(set())
                nums.append(board[r][c])
                bfs(r,c)
    # [1-2] 각 그룹간 점수 계산 (누적)
    CNT = len(nums)
    for i in range(0,CNT-1):
        for j in range(i+1,CNT): # CNT개에서 2개를 뽑는 가능한 모든 조합
            # 인접면 1개당 더해질 점수
            point = (len(groups[i]) + len(groups[j])) * nums[i] * nums[j]
            for cr,cc in groups[i]:
                for nr,nc in ((cr-1,cc),(cr+1,cc),(cr,cc-1),(cr,cc+1)):
                    if (nr,nc) in groups[j]: # 인접한 좌표가 그룹j에 있다면 두 그룹은 인접
                        ans += point

    if k == 3:
        break
    # [2] 회전시키기 십자 부분 반시계 90 , 나머지 시계 90
    nboard = [x[:] for x in board]
    for r in range(N):
        nboard[M][r] = board[r][M]
    for c in range(N):
        nboard[c][M] = board[M][N-c-1]

    for (sr,sc) in ((0,0),(M+1,0),(0,M+1),(M+1,M+1)):
        for r in range(M):
            for c in range(M):
                nboard[sr+r][sc+c] = board[sr+M-c-1][sc+r]
    board = nboard
print(ans)