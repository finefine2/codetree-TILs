from collections import deque

MAX_N = 31
MAX_L = 41
drs,dcs = [-1,0,1,0],[0,1,0,-1]

info = [[0 for _ in range(MAX_L)] for _ in range(MAX_L)]
bef_k = [0 for _ in range(MAX_N)]
r = [0 for _ in range(MAX_N)]
c = [0 for _ in range(MAX_N)]
h = [0 for _ in range(MAX_N)]
w = [0 for _ in range(MAX_N)]
k = [0 for _ in range(MAX_N)]
nr = [0 for _ in range(MAX_N)]
nc = [0 for _ in range(MAX_N)]
dmg = [0 for _ in range(MAX_N)]
is_moved = [False for _ in range(MAX_N)]

def try_move(idx, dir):
    q = deque()
    is_pos = True

    for i in range(1, N+1):
        dmg[i] = 0
        is_moved[i] = False
        nr[i] = r[i]
        nc[i] = c[i]
    q.append(idx)
    is_moved[idx] = True

    while q:
        x = q.popleft()
        nr[x] += drs[dir]
        nc[x] += dcs[dir]
        # 경계 넘나 체크
        if nr[x] < 1 or nc[x] < 1 or nr[x] + h[x] -1 > L or nc[x] + w[x] -1 > L:
            return False
        for i in range(nr[x], nr[x] + h[x]):
            for j in range(nc[x], nc[x] + w[x]):
                if info[i][j] == 1:
                    dmg[x] += 1
                if info[i][j] == 2:
                    return False
        for i in range(1, N+1):
            if is_moved[i] or k[i] <= 0:
                continue
            if r[i] > nr[x] + h[x] - 1 or nr[x] > r[i] + h[i] - 1:
                continue
            if c[i] > nc[x] + w[x] - 1 or nc[x] > c[i] + w[i] - 1:
                continue
            is_moved[i] = True
            q.append(i)
    dmg[idx] = 0
    return True

def move_piece(idx,move_dir):
    if k[idx] <= 0:
        return
    if try_move(idx, move_dir):
        for i in range(1, N+1):
            r[i] = nr[i]
            c[i] = nc[i]
            k[i] -= dmg[i]

L, N, Q = map(int,input().split())
for i in range(1, L+1):
    info[i][1:] = map(int,input().split())
for i in range(1, N+1):
    r[i], c[i], h[i], w[i], k[i] = map(int,input().split())
    bef_k[i] = k[i]
for _ in range(Q):
    idx, d = map(int,input().split())
    move_piece(idx, d)

ans = sum([bef_k[i] - k[i] for i in range(1,N+1) if k[i] > 0])
print(ans)