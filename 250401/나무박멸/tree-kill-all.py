N,M,K,C = tuple(map(int,input().split()))
# blank 0, wall -1, tree > 0
board = [list(map(int,input().split())) for _ in range(N)]

spray = [[0] * N for _ in range(N)]
new_board = [[0] * N for _ in range(N)]
ans = 0
def in_range(r,c):
    return 0<=r<N and 0<=c<N

def grow():
    drs,dcs = [1,-1,0,0],[0,0,1,-1]
    # 모든 나무들에 대해서 진행한다
    for r in range(N):
        for c in range(N):
            # 나무는 양수로 주어짐
            cnt = 0
            if board[r][c] > 0:
                for dr,dc in zip(drs,dcs):
                    nr,nc = r + dr, c + dc
                    if in_range(nr,nc) and board[nr][nc] > 0:
                        cnt += 1
            board[r][c] += cnt

def spread():
    drs,dcs = [1,-1,0,0],[0,0,1,-1]
    # new_board 초기화 작업
    for r in range(N):
        for c in range(N):
            new_board[r][c] = 0
    # 모든 나무들에 대해서 진행한다
    # 번식 가능한 칸에 대해 조사하기
    for r in range(N):
        for c in range(N):
            if board[r][c] > 0:
                tree_cnt = 0
                tree_pos = []
                for dr,dc in zip(drs,dcs):
                    nr,nc = r + dr, c + dc
                    # 번식 가능한 칸 갯수 카운팅 + 좌표 기록
                    if in_range(nr,nc) and board[nr][nc] == 0 and spray[nr][nc] == 0:
                        tree_cnt += 1
                        tree_pos.append([nr,nc])
                for nnr,nnc in tree_pos:
                    new_board[nnr][nnc] += board[r][c] // tree_cnt

    for r in range(N):
        for c in range(N):
            board[r][c] += new_board[r][c]

# pprint(board)
# grow()
# print("######")
# pprint(board)
# print("######")
# spread()
# pprint(board)
def remove():
    global ans
    # 제초제를 뿌리고 사라지는 과정
    frs,fcs = [1,-1,1,-1],[1,1,-1,-1]
    # 제초제를 뿌릴 위치 고르기
    max_del, max_r, max_c = 0,0,0
    for r in range(N):
        for c in range(N):
            # 나무가 있는 칸에 뿌려야 제초제가 전파가 된다
            if board[r][c] > 0:
                cnt = board[r][c]
                for fr, fc in zip(frs,fcs):
                    for i in range(1,K+1):
                        nr,nc = r + fr*i, c + fc*i
                        if in_range(nr,nc):
                            if board[nr][nc] > 0:
                                cnt += board[nr][nc]
                            else:
                                break
                if max_del < cnt:
                    max_del = cnt
                    max_r, max_c = r,c
    # print(f"start position is {max_r} and {max_c}")

    ans += max_del
    # 제초제를 뿌릴 위치를 찾았다
    # 대각선 방향으로 전파
    # 4개 방향으로 k칸만큼
    for fr,fc in zip(frs,fcs):
        start_r, start_c = max_r,max_c
        board[start_r][start_c] = 0
        spray[start_r][start_c] = C
        for i in range(1,K+1):
            nr,nc = start_r + fr * i, start_c + fc * i
            # 제초제에 대한 처리
            # 제초제 여부는 크게 상관하지 않고 새로 뿌려지면 다시 C년동안 유지가 됨
            if in_range(nr,nc):
                # 벽이 있으면
                if board[nr][nc] == -1:
                    break
                # 나무가 아예 없으면 제초제가 뿌려지고 다음칸은 ㄴㄴ
                elif board[nr][nc] == 0:
                    spray[nr][nc] = C
                    break
                # 나무가 있으면?
                # 나무가 있는 자리를 제거해야함
                elif board[nr][nc] > 0:
                    spray[nr][nc] = C
                    board[nr][nc] = 0
def decrease():
    for r in range(N):
        for c in range(N):
            if spray[r][c] > 0:
                spray[r][c] -= 1
for i in range(M):
    # print(f"current turn is {i+1}")
    grow()
    spread()
    decrease()
    remove()

print(ans)