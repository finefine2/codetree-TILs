N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
def in_range(r,c):
    return 0<=r<N and 0<=c<N
from collections import deque

def bfs(sr,sc,value):
    q = deque()

    q.append((sr,sc))
    v[sr][sc] = 1

    group = set()
    group.add((sr,sc))

    while q:
        cr,cc = q.popleft()

        for nr,nc in ((cr-1,cc),(cr,cc+1),(cr+1,cc),(cr,cc-1)):
            if in_range(nr,nc) and v[nr][nc] == 0 and board[nr][nc] == value:
                group.add((nr,nc))
                v[nr][nc] = 1
                q.append((nr,nc))
    return group
def rotate(arr):
    narr = [x[:] for x in arr]
    N = len(arr)
    M = N // 2

    # 십자모양 회전
    for r in range(N):
        narr[M][r] = arr[r][M]
    for c in range(N):
        narr[c][M] = arr[M][N-c-1] 

    # 반시계모양 회전
    for sr,sc in ((0,0),(0,M+1),(M+1,0),(M+1,M+1)):
        for r in range(M):
            for c in range(M):
                narr[sr+r][sc+c] = arr[sr+M-c-1][sc+r]
    return narr

ans = 0
for k in range(4):
    score = 0
    groups = []
    nums = []
    v = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if v[r][c] == 0:
                count_group = bfs(r,c,board[r][c])
                groups.append(count_group)
                nums.append(board[r][c])

    # score 계산하는 법
    M = len(groups)
    for i in range(M-1):
        for j in range(i+1,M):
            for gr,gc in groups[i]:
                point = nums[i] * nums[j] * (len(groups[i]) + len(groups[j]))
                for nr,nc in ((gr-1,gc),(gr,gc+1),(gr+1,gc),(gr,gc-1)):
                    if (nr,nc) in groups[j]:
                        score += point

    ans += score
    if k == 3:
        break

    board = rotate(board)
print(ans)
