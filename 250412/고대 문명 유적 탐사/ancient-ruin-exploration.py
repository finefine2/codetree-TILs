K,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(5)]

treasures = list(map(int,input().split()))
def rotate(arr,sr,sc):
    narr = [x[:] for x in arr]
    for r in range(3):
        for c in range(3):
            narr[sr+r][sc+c] = arr[sr+3-c-1][sc+r]

    return narr
def count_clear(board,clr):
    v = [[0] * 5 for _ in range(5)]
    ans = 0
    for r in range(5):
        for c in range(5):
            if v[r][c] == 0:
                cnt = bfs(board,v,r,c,clr)
                ans += cnt
    return ans

def in_range(r,c):
    return 0<=r<5 and 0<=c<5
from collections import deque
def bfs(board,v,r,c,clr):
    q = deque()

    v[r][c] = 1
    q.append((r,c))

    collected = [(r,c)]

    while q:
        cr,cc = q.popleft()

        for dr,dc in ((-1,0),(0,1),(1,0),(0,-1)):
            nr,nc = cr + dr, cc + dc
            if in_range(nr,nc) and board[nr][nc] == board[r][c]:
                q.append((nr,nc))
                v[nr][nc] = 1
                collected.append((nr,nc))
    if len(collected) >= 3:
        if clr == 1:
            for xr,xc in collected:
                board[xr][xc] = 0
            return len(collected)
    return 0

res = []
for _ in range(K):
    # 유물 가치가 최대
    # 회전 각도는 작을수록
    # 회전 좌표 열이 작을수록
    # 행이 작을수록
    max_cnt = 0
    for rot in range(1,4):
        for sc in range(3):
            for sr in range(3):
                nboard = [x[:] for x in board]
                for _ in range(rot):
                    nboard = rotate(nboard,sr,sc)
                cnt = count_clear(nboard,0)
                if cnt > max_cnt:
                    max_cnt = cnt
                    best_board = nboard

    # 유물 획득 불가시 종료
    if max_cnt == 0:
        break
    # 그게 아니면 진행하자
    cnt = 0
    board = best_board
    while True:
        t = count_clear(board,1)
        if t == 0:
            break
        cnt += t 
        res.append(cnt) 
        for c in range(5):
            for r in range(4,-1,-1):
                if board[r][c] == 0:
                    board[r][c] = treasures.pop(0)

print(*res)