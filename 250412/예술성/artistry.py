N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
from collections import deque
def in_range(r,c):
    return 0<=r<N and 0<=c<N

def bfs(sr,sc):
    q = deque()
    group = set()

    q.append((sr,sc))
    group.add((sr,sc))
    v[sr][sc] = 1

    while q:
        cr,cc = q.popleft()
        for nr,nc in ((cr-1,cc),(cr,cc+1),(cr+1,cc),(cr,cc-1)):
            if in_range(nr,nc) and v[nr][nc] == 0 and board[nr][nc] == board[cr][cc]:
                q.append((nr,nc))
                v[nr][nc] = 1
                group.add((nr,nc))
    return group

def rotate(arr):
    narr = [x[:] for x in arr]
    N = len(arr)
    M = N // 2

    # 십자모양 반시계 90도
    for r in range(N):
        narr[r][M] = arr[M][N-r-1]
    for c in range(N):
        narr[M][c] = arr[c][M]

    # 그 외 영역 부분회전 90도 시계
    for sr,sc in ((0,0),(M+1,0),(0,M+1),(M+1,M+1)):
        for r in range(M):
            for c in range(M):
                narr[sr+r][sc+c] = arr[sr+M-c-1][sc+r]
    arr = narr
    return arr
ans = 0
for k in range(4):
    nums = []
    groups = []
    v = [[0] * N for _ in range(N)]
    for r in range(5):
        for c in range(5):
            if v[r][c] == 0:
                count_group = bfs(r,c)
                groups.append(count_group)
                nums.append(board[r][c])

    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            point = (len(groups[i])+len(groups[j])) * nums[i] * nums[j]
            for gr,gc in groups[i]:
                for nr,nc in ((gr-1,gc),(gr+1,gc),(gr,gc-1),(gr,gc+1)):
                    if (nr,nc) in groups[j]:
                        ans += point

    if k == 3:
        break

    board = rotate(board)
print(ans)