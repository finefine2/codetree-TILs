R,C,K = map(int,input().split())
golems =[list(map(int,input().split())) for _ in range(K)]
board = [[1] + [0] * C + [1] for _ in range(R+3)] + [[1] * (C+2)]
exit_set = set()

drs,dcs = [-1,0,1,0],[0,1,0,-1]

from collections import deque

def bfs(sr,sc):
    q = deque()
    v = [[0] * (C+2) for _ in range(R+4)]

    q.append((sr,sc))
    v[sr][sc] = 1

    max_r = 0

    while q:
        cr,cc = q.popleft()
        max_r = max(max_r,cr)

        for dr,dc in ((-1,0),(0,1),(1,0),(0,-1)):
            nr,nc = cr + dr, cc + dc
            if v[nr][nc] == 0 and (board[nr][nc] == board[cr][cc] or ((cr,cc) in exit_set and board[nr][nc]>1)):
                q.append((nr,nc))
                v[nr][nc] =1

    return max_r - 2

ans = 0
num = 2

for cc, d in golems:
    cr = 1

    while True:
        if board[cr+1][cc-1] + board[cr+2][cc] + board[cr+1][cc+1] == 0:
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
        board = [[1] + [0] * C + [1] for _ in range(R+3)] + [[1] * (C+2)]
        exit_set = set()
        num = 2
    else:
        board[cr-1][cc] = board[cr+1][cc] = num
        board[cr][cc-1:cc+2] = [num] * 3
        num += 1

        exit_set.add((cr+drs[d],cc+dcs[d]))
        ans += bfs(cr, cc)

print(ans)