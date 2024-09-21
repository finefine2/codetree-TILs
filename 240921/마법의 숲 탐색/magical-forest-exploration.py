from collections import deque
R,C,K = tuple(map(int,input().split()))
golems = []
for _ in range(K):
    gc,gd = tuple(map(int,input().split()))
    golems.append((gc,gd))

board = [[1] + [0] * C + [1] for _ in range(R+3)] + [[1] * (C+2)]
exit_set = set()
num = 2
ans = 0

# N E S W
drs,dcs = [-1,0,1,0],[0,1,0,-1]
def bfs(sr,sc):
    q = deque()
    visited = [[0] * (C+2) for _ in range(R+4)]
    max_r = 0
    q.append((sr,sc))
    visited[sr][sc] = 1

    while q:
        cr,cc = q.popleft()
        max_r = max(cr,max_r)
        for dr,dc in zip(drs,dcs):
            nr,nc = cr + dr, cc + dc
            # 4 방향 미방문, 같은 좌표거나 출구거나
            if not visited[nr][nc] and (board[cr][cc] == board[nr][nc] or ((cr,cc) in exit_set and board[nr][nc] >1)):
                q.append((nr,nc))
                visited[nr][nc] = 1
    return max_r -2
for gc,gd in golems:
    # 일단은 제약이 없는 한 계속해서 내려간다
    gr = 1
    while True:
        # 남쪽으로 쭉
        if board[gr+2][gc] + board[gr+1][gc-1] + board[gr+1][gc+1] == 0:
            gr += 1
        # 서쪽으로 회전을 계속 시킴
        elif board[gr-1][gc-1] + board[gr][gc-2] + board[gr+1][gc-1] + board[gr+2][gc-1] + board[gr+1][gc-2] == 0:
            gr += 1
            gc -= 1
            gd = (gd-1) % 4
        # 동쪽으로 계속 회전 시킴
        elif board[gr-1][gc+1] + board[gr][gc+2] + board[gr+1][gc+1] + board[gr+2][gc+1] + board[gr+1][gc+2] == 0:
            gr += 1
            gc += 1
            gd = (gd+1) % 4
        else:
            break

        # if out of board?
    if gr < 4:
        board = [[1] + [0] * C + [1] for _ in range(R+3)] + [[1] * (C+2)]
        exit_set = set()
        num = 2
    else:
        board[gr][gc] = num
        board[gr+1][gc] = num
        board[gr-1][gc] = num
        board[gr][gc+1] = num
        board[gr][gc-1] = num
        exit_set.add((gr+drs[gd],gc+dcs[gd]))
        num += 1
        ans += bfs(gr,gc)
print(ans)