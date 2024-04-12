N,M,K = map(int,input().split())
board = [[0] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    board[i] = [0] + list(map(int,input().split()))

next_board = [[0] * (N+1) for _ in range(N+1)]

traveler = [(-1,-1)] + [tuple(map(int,input().split())) for _ in range(M)]

exits = tuple(map(int,input().split()))
ans = 0
sr, sc, square_size = 0,0,0

def move_all_traveler():
    global exits, ans
    for i in range(1,M+1):
        if traveler[i] == exits:
            continue
        tr,tc = traveler[i]
        er,ec = exits

        if tr != er:
            nr,nc = tr,tc
            if er > nr:
                nr += 1
            else:
                nr -= 1
            if not board[nr][nc]:
                traveler[i] = (nr,nc)
                ans += 1
                continue
        if tc != ec:
            nr,nc = tr,tc
            if ec > nc:
                nc += 1
            else:
                nc -= 1
            if not board[nr][nc]:
                traveler[i] = (nr,nc)
                ans += 1
                continue
def find_mini_square():
    global exits, sr,sc, square_size
    er,ec = exits
    for sz in range(2, N+1):
        for r1 in range(1,N-sz+2):
            for c1 in range(1,N-sz+2):
                r2,c2 = r1 + sz -1, c1 + sz -1
                if not (r1 <= er <= r2 and c1 <= ec <= c2):
                    continue
                is_traveler_in = False
                for l in range(1,M+1):
                    tr, tc = traveler[l]
                    if r1 <= tr <= r2 and c1 <= tc <= c2:
                        if not (tr == er and tc == ec):
                            is_traveler_in = True
                if is_traveler_in:
                    sr,sc,square_size = r1, c1, sz
                    return

def rotate_square():
    for r in range(sr,sr+square_size):
        for c in range(sc,sc+square_size):
            if board[r][c]:
                board[r][c] -= 1
    for r in range(sr, sr+ square_size):
        for c in range(sc,sc+square_size):
            o_r,o_c = r - sr, c - sc
            r_r,r_c = o_c, square_size-o_r-1
            next_board[r_r+sr][r_c+sc] = board[r][c]
    for r in range(sr,sr+square_size):
        for c in range(sc,sc+square_size):
            board[r][c] = next_board[r][c]
def rotate_traveler_and_exit():
    global exits
    for i in range(1,M+1):
        tr, tc = traveler[i]
        if sr <= tr < sr + square_size and sc <= tc < sc + square_size:
            o_r, o_c = tr - sr, tc - sc
            r_r, r_c = o_c, square_size - o_r - 1
            traveler[i] = (r_r + sr, r_c + sc)
    er,ec = exits
    if sr <= er < sr + square_size and sc <= ec < sc + square_size:
        o_r, o_c = er - sr, ec - sc
        r_r, r_c = o_c, square_size - o_r - 1
        exits = (r_r + sr, r_c + sc)
for _ in range(K):
    move_all_traveler()
    is_all_escaped = True
    for i in range(1,M+1):
        if traveler[i] != exits:
            is_all_escaped = False
    if is_all_escaped:
        break
    find_mini_square()
    rotate_square()
    rotate_traveler_and_exit()
print(ans)
er,ec = exits
print(er, ec)