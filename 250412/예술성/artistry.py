# # 단골 부분회전 -> 목적지 좌표 기준
# # groups nums
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
M = N // 2

from collections import deque

def in_range(r,c):
    return 0<=r<N and 0<=c<N

def rotate_board(arr):
    narr = [x[:] for x in arr]
    # 십자모양
    for r in range(N):
        narr[M][r] = arr[r][M]
    for c in range(N):
        narr[c][M] = arr[M][N-c-1]

    # 그 외의 영역들
    for sr,sc in ((0,0),(M+1,0),(0,M+1),(M+1,M+1)):
        for r in range(M):
            for c in range(M):
                narr[sr+r][sc+c] = arr[sr+M-c-1][sc+r]
    
    return narr

def bfs(sr,sc,value):
    q = deque()
    v[sr][sc] = 1
    group = set()

    group.add((sr,sc))
    q.append((sr,sc))

    while q:
        cr,cc = q.popleft()

        for nr,nc in ((cr-1,cc),(cr,cc+1),(cr+1,cc),(cr,cc-1)):
            if in_range(nr,nc) and v[nr][nc] == 0 and board[nr][nc] == value:
                q.append((nr,nc))
                v[nr][nc] = 1
                group.add((nr,nc))
    return group


ans = 0
for k in range(4):
    nums = []
    groups = []
    v = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if v[r][c] == 0:
                count_group = bfs(r,c,board[r][c])
                groups.append(count_group)
                nums.append(board[r][c])



    score = 0
    for i in range(len(groups)-1):
        for j in range(i+1,len(groups)):
            point = (len(groups[i])+len(groups[j])) * nums[i] * nums[j]
            for cr,cc in groups[i]:
                for nr,nc in ((cr-1,cc),(cr+1,cc),(cr,cc-1),(cr,cc+1)):
                    if (nr,nc)  in groups[j]:
                        score += point
    ans += score
    if k == 3:
        break


    board = rotate_board(board)

print(ans)
