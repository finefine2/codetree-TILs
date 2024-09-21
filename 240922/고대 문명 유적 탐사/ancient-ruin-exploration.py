from collections import deque

K,M = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(5)]
treasures = list(map(int,input().split()))
ans = []

def in_range(r,c):
    return 0<=r<5 and 0<=c<5
def rotate(arr,sr,sc):
    narr = [x[:] for x in arr]
    for r in range(3):
        for c in range(3):
            narr[sr+r][sc+c] = arr[sr+3-c-1][sc+r]
    return narr

def bfs(board,v,r,c,clr):
    drs,dcs = [1,0,-1,0],[0,1,0,-1]
    q = deque()
    sset = set()
    cnt = 0

    q.append((r,c))
    v[r][c] = 1
    sset.add((r,c))
    cnt += 1

    while q:
        cr,cc = q.popleft()
        for dr,dc in zip(drs,dcs):
            nr,nc = cr + dr, cc + dc
            if in_range(nr,nc) and not v[nr][nc] and board[nr][nc] == board[cr][cc]:
                q.append((nr,nc))
                v[nr][nc] = 1
                sset.add((nr,nc))
                cnt += 1
    if cnt >= 3:
        if clr == 1:
            for r,c in sset:
                board[r][c] = 0
        return cnt
    else:
        return 0


def count_clear(arr,clr):
    v = [[0] * 5 for _ in range(5)]
    cnt = 0
    for r in range(5):
        for c in range(5):
            if v[r][c] == 0:
                t = bfs(arr,v,r,c,clr)
                cnt += t
    return cnt

for _ in range(K):
    # 1. 탐색 진행
    max_cnt = 0
    for rot in range(1,4):
        for c in range(3):
            for r in range(3):
                nboard = [x[:] for x in board]
                for _ in range(rot):
                    nboard = rotate(nboard,r,c)
                t = count_clear(nboard,0)
                if max_cnt < t:
                    max_cnt = t
                    marr = nboard
    if max_cnt == 0:
        break
    # 2. 연쇄 획득
    cnt = 0
    board = marr
    while True:
        t = count_clear(board,1)
        if t == 0:
            break
        cnt += t
        for c in range(5):
            for r in range(4,-1,-1):
                if board[r][c] == 0:
                    board[r][c] = treasures.pop(0)
    ans.append(cnt)
for a in ans:
    print(a,end=" ")