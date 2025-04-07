K,M = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(5)]
treasures = list(map(int,input().split()))
ans = []

def rotate(board,sr,sc):
    nboard = [x[:] for x in board]

    for r in range(3):
        for c in range(3):
            nboard[sr+r][sc+c] = board[sr+3-c-1][sc+r]
    return nboard

from collections import deque
def bfs(board,v,sr,sc,clr):
    q = deque()

    q.append((sr,sc))
    v[sr][sc] = 1

    connected = {(sr,sc)}
    while q:
        cr,cc = q.popleft()

        for dr,dc in ((-1,0),(1,0),(0,1),(0,-1)):
            nr,nc = cr + dr, cc + dc
            if 0<=nr<5 and 0<=nc<5 and v[nr][nc] == 0 and board[nr][nc] == board[cr][cc]:
                q.append((nr,nc))
                connected.add((nr,nc))
                v[nr][nc] = 1
    if len(connected) >= 3:
        if clr == 1:
            for xr,xc in connected:
                board[xr][xc] = 0
        return len(connected)
    return 0

def count_clear(board,clr):
    v = [[0] * 5 for _ in range(5)]
    ans = 0
    for r in range(5):
        for c in range(5):
            if v[r][c] == 0:
                t = bfs(board,v,r,c,clr)
                ans += t
    return ans

result = []
for _ in range(K):
    # [1] 최적의 회전 찾기
    max_cnt = 0

    for rot in range(1,4):
        for sc in range(3):
            for sr in range(3):
                nboard = [x[:] for x in board]

                for _ in range(rot):
                    nboard = rotate(nboard,sr,sc)

                t = count_clear(nboard,0)
                if t > max_cnt:
                    max_cnt = t
                    best_board = nboard
    if max_cnt == 0:
        break

    board = best_board
    cnt = 0
    # 연쇄획득
    while True:
        t = count_clear(board,1)
        if t == 0:
            break
        cnt += t

        for c in range(5):
            for r in range(4,-1,-1):
                if board[r][c] == 0:
                    board[r][c] = treasures.pop(0)
    result.append(cnt)

for r in result:
    print(r,end=" ")