N,M,K,C = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]

spray = [[0] * N for _ in range(N)]

ans = 0
def in_range(r,c):
    return 0<=r<N and 0<=c<N

for m in range(M):
    # 0 spray decrease
    for r in range(N):
        for c in range(N):
            if spray[r][c] > 0:
                spray[r][c] -= 1
    # 1. grow
    nboard = [x[:] for x in board]
    for r in range(N):
        for c in range(N):
            cnt = 0
            if board[r][c] > 0:
                for nr,nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                    if in_range(nr,nc) and board[nr][nc] > 0:
                        cnt += 1
            nboard[r][c] += cnt
    board = nboard
    # 2. spread
    nboard = [x[:] for x in board]
    for r in range(N):
        for c in range(N):
            if board[r][c] > 0:
                tlst = []
                for nr,nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                    if in_range(nr,nc) and board[nr][nc] == 0 and spray[nr][nc] == 0:
                        tlst.append((nr,nc))
                if len(tlst) > 0:
                    d = board[r][c] // len(tlst)
                    for tr,tc in tlst:
                        nboard[tr][tc] += d
    board = nboard

    # 3. get max
    mx, max_r, max_c = 0, 0, 0
    for r in range(N):
        for c in range(N):
            if board[r][c] > 0:
                cnt = board[r][c]
                for fr, fc in ((-1, 1), (-1, -1), (1, -1), (1, 1)):
                    for k in range(1,K+1):
                        nr, nc = r + fr * k, c + fc * k
                        if in_range(nr, nc):
                            if board[nr][nc] > 0:
                                cnt += board[nr][nc]
                            else:
                                break
                if mx < cnt:
                    mx, max_r, max_c = cnt, r, c
    ans += mx
    if mx == 0:
        break
    for fr, fc in ((-1, 1), (-1, -1), (1, -1), (1, 1)):
        start_r, start_c = max_r, max_c
        board[start_r][start_c] = 0
        spray[start_r][start_c] = C
        for k in range(1,K+1):
            nr, nc = start_r + fr * k, start_c + fc * k
            if in_range(nr, nc):
                # 벽이 있는 칸
                if board[nr][nc] == -1:
                    break
                    # 나무가 아예 없는 칸
                elif board[nr][nc] == 0:
                    spray[nr][nc] = C
                    break
                elif board[nr][nc] > 0:
                    board[nr][nc] = 0
                    spray[nr][nc] = C

print(ans)