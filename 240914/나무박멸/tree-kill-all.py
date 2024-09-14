from pprint import pprint
N,M,K,C = tuple(map(int,input().split()))

board = [list(map(int,input().split())) for _ in range(N)]
new_board = [[0] * N for _ in range(N)]
spray = [[0] * N for _ in range(N)]
ans = 0
def in_range(r,c):
    return 0<=r<N and 0<=c<N
# 성장
# 주변에 나무가 몇개있는지 세고 그에 따라 성장
def grow():
    drs,dcs = [1,-1,0,0],[0,0,1,-1]
    for r in range(N):
        for c in range(N):
            cnt = 0
            if board[r][c] > 0:
                for dr,dc in zip(drs,dcs):
                    nr,nc = r + dr, c + dc
                    if in_range(nr,nc) and board[nr][nc] > 0:
                        cnt += 1
                board[r][c] += cnt
# 번식
def spread():
    drs, dcs = [1,-1,0,0],[0,0,1,-1]
    for r in range(N):
        for c in range(N):
            new_board[r][c] = 0
    for r in range(N):
        for c in range(N):
            # 기존에 있던 나무들이 인접4칸 번식시킴
            if board[r][c] > 0:
                cnt = 0
                spread_pos = []
                for dr,dc in zip(drs,dcs):
                    nr,nc = r + dr, c + dc
                    if in_range(nr,nc) and board[nr][nc] == 0 and spray[nr][nc] == 0:
                        cnt += 1
                        spread_pos.append([nr,nc])
                for nnr,nnc in spread_pos:
                    new_board[nnr][nnc] += board[r][c] // cnt
    for r in range(N):
        for c in range(N):
            board[r][c] += new_board[r][c]
# 제초제 뿌리기
def remove():
    global ans
    # 1. 제초제 뿌릴 위치를 정하기
    max_del, max_r, max_c = 0, 0, 0
    frs, fcs = [1,-1,1,-1],[1,1,-1,-1]
    for r in range(N):
        for c in range(N):
            # 나무가 있는 칸에 제초제를 뿌려야함
            if board[r][c] > 0:
                cnt = board[r][c]
                for fr,fc in zip(frs,fcs):
                    nr,nc = r,c
                    for i in range(K):
                        nr,nc = nr + fr, nc + fc
                        if in_range(nr,nc):
                            if board[nr][nc] > 0:
                                cnt += board[nr][nc]
                            else:
                                break
                if max_del < cnt:
                    max_del = cnt
                    max_r,max_c = r,c
    ans += max_del
    # 이제 제초제가 뿌려지는 시작점을 찾았음
    # 제초제가 뿌려지는 조건
    # 다음 칸이 나무가 없는 칸이면 그 다음 칸으로는 전파가 안됨
    if board[max_r][max_c] > 0:
        board[max_r][max_c] = 0
        spray[max_r][max_c] = C
        for fr,fc in zip(frs,fcs):
            nr,nc = max_r,max_c
            for i in range(K):
                nr,nc = nr + fr, nc + fc
                if in_range(nr,nc):
                    if board[nr][nc] > 0:
                        board[nr][nc] = 0
                        spray[nr][nc] = C
                    elif board[nr][nc] == 0:
                        spray[nr][nc] = C
                        break
                    elif board[nr][nc] == -1:
                        break
def decrease_spray():
    for r in range(N):
        for c in range(N):
            if spray[r][c] > 0:
                spray[r][c] -= 1
# pprint(board)
# grow()
# print("#######")
# pprint(board)
# spread()
# print("#######")
# pprint(board)
for i in range(M):
    grow()
    spread()
    decrease_spray()
    remove()
print(ans)