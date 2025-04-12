R,C,K = map(int,input().split())

board = [[1]+[0]* C+[1] for _ in range(R+3)] + [[1] * (C+2)]

exit_set = set()

golems = []
for _ in range(K):
    c,d = map(int,input().split())
    golems.append((c,d))

drs,dcs = [-1,0,1,0],[0,1,0,-1]

from collections import deque
def bfs(sr,sc):
    q = deque()
    v = [[0] * (C+2) for _ in range(R+4)]

    mx_r = 0
    q.append((sr,sc))
    v[sr][sc] = 1
    while q:
        cr,cc = q.popleft()
        mx_r = max(cr,mx_r)

        for dr,dc in zip(drs,dcs):
            nr,nc = cr + dr, cc + dc
            if v[nr][nc] == 0 and (board[cr][cc]==board[nr][nc] or ((cr,cc) in exit_set and board[nr][nc]>1)):
                q.append((nr,nc))
                v[nr][nc] = 1
    return mx_r - 2
ans = 0
num = 2

for cc,d in golems:
    cr = 1
    while True:
        if board[cr+2][cc] + board[cr+1][cc+1] + board[cr+1][cc-1] == 0:
            cr += 1
        elif board[cr-1][cc-1] + board[cr][cc-2] + board[cr+1][cc-1] + board[cr+1][cc-2] + board[cr+2][cc-1] == 0:
            cr += 1
            cc -= 1
            d = (d-1) % 4
        elif board[cr-1][cc+1] + board[cr][cc+2] + board[cr+1][cc+1] + board[cr+1][cc+2] + board[cr+2][cc+1] == 0:
            cr += 1
            cc += 1
            d = (d+1) % 4
        else:
            break

    if cr < 4:
        board = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)]
        exit_set = set()
        num = 2
    else:
        board[cr-1][cc] = board[cr+1][cc] = num
        board[cr][cc-1:cc+2] = [num] * 3
        er,ec = cr + drs[d], cc + dcs[d]
        exit_set.add((er,ec))
        ans += bfs(cr,cc)
        num += 1

print(ans)