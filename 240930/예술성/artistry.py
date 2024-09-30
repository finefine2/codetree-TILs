from collections import deque

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

def in_range(r,c):
    return 0<=r<N and 0<=c<N

def find_group(r,c):
    q = deque()
    q.append((r,c))
    v[r][c] = 1
    groups[-1].add((r,c))

    while q:
        cr,cc = q.popleft()
        for nr,nc in ((cr-1,cc),(cr+1,cc),(cr,cc-1),(cr,cc+1)):
            if in_range(nr,nc) and v[nr][nc] == 0 and board[cr][cc] == board[nr][nc]:
                q.append((nr,nc))
                v[nr][nc] = 1
                groups[-1].add((nr,nc))

def rotate(arr):
    narr = [x[:] for x in arr]

    N = len(arr)
    M = N // 2

    # 십자영역 회전
    for r in range(N):
        narr[r][M] = arr[M][N-r-1]
    for c in range(N):
        narr[M][c] = arr[c][M]

    # 4개 정사각형 회전
    for sr,sc in ((0,0),(0,M+1),(M+1,0),(M+1,M+1)):
        for r in range(M):
            for c in range(M):
                narr[sr+r][sc+c] = arr[sr+M-c-1][sc+r]

    return narr
ans = 0
for k in range(4):


    groups = []
    nums = []

    v = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if in_range(r, c) and not v[r][c]:
                groups.append(set())
                nums.append(board[r][c])
                find_group(r, c)
    CNT = len(nums)
    for r in range(CNT - 1):
        for c in range(r + 1, CNT):
            point = (len(groups[r]) + len(groups[c])) * nums[r] * nums[c]
            for cr, cc in groups[r]:
                for nr, nc in ((cr - 1, cc), (cr + 1, cc), (cr, cc + 1), (cr, cc - 1)):
                    if (nr, nc) in groups[c]:
                        ans += point
    if k == 3:
        break
    board = rotate(board)
print(ans)