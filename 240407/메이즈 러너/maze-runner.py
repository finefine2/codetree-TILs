N,M,K = map(int,input().split()) 

board = [[0] * (N+1) for _ in range(N+1)] 

for i in range(1,N+1): 
    board[i] = [0] + list(map(int,input().split())) 

# 회전을 편하게 하기 위해서 2차원 리스트 하나 더 선언 
next_board = [[0] * (N+1) for _ in range(N+1)] 

# 참가자 위치 정보 
player = [(-1,-1)] + [tuple(map(int,input().split())) for _ in range(M)]
# 출구 정보
exits = tuple(map(int,input().split()))

# 정답 
ans = 0 
# 회전해야 하는 최소 스퀘어 
sr, sc, square_size = 0, 0, 0 

# 참가자들이 움직일 수 있는지 판단하고 이동한 뒤 회전할 정사각형 찾기 
# 선택된 정사각형 내부 벽의 내구도를 감소시키고, 정사각형 회전 
# 이 과정 중 참가자들과 출구의 위치 변화도 반영하여 회전 
# K초가 지나거나 모든 참가자들이 나갈 때까지 반복 
# 참가자 이동거리를 누적하여 기록, 모든 참가자가 탈출하거나 시간 끝나면 최종 결과 프린트

# 참가자 이동   
def move_all_player(): 
    global exits, ans 
    for i in range(1,M+1): 
        if player[i] == exits:
            continue
        
        tr, tc = player[i] 
        er, ec = exits
        # 행이 다르면 행을 이동
        if tr != er: 
            nr,nc = tr, tc

            if er > nr: 
                nr += 1 
            else: 
                nr -= 1 
            # 벽이 없다면 행을 이동하고 바로 다음 참가자로 
            if not board[nr][nc]: 
                player[i] = (nr, nc) 
                ans += 1 
                continue
        # 열이 다르면 열을 이동 
        if tc != ec: 
            nr, nc = tr, tc 
            if ec > nc: 
                ec ++ 1 
            else: 
                ec -= 1 
            # 벽이 없으면 행을 이동, 이 경우는 열을 이동 
            if not board[nr][nc]: 
                player[i] = (nr,nc) 
                ans += 1 
                continue
# 한 명 이상의 참가자와 출구 포함 최소 정사각형 찾기 
def find_minimum_square(): 
    global exits, sr, sc, square_size
    er, ec = exits
    # 최소 정사각형부터 모든 정사각형을 만들기 
    for sz in range(2,N+1): 
        # 좌상단 r이 작은 것부터 하나씩 만들기 
        for r1 in range(1, N - sz + 2):
            # 좌상단 c가 작은 것부터 하나씩 만들기 
            for c1 in range(1, N - sz + 2): 
                r2, c2 = r1 + sz - 1, c1 + sz - 1 
                # 출구가 정사각형 안에 없으면 스킵 
                if not (r1 <= er <= r2 and c1 <= ec <= c2): 
                    continue
                # 한 명 이상의 참가자가 정사각형 안에 있는지 체크 
                is_traveler_in = False 
                for l in range(1,M+1): 
                    tr, tc = player[i] 
                    if r1 <= tr <= r2 and c1 <= tc <= c2: 
                        # 출구의 참가자는 제외 
                        if not (tr == er and tc == ec): 
                            is_traveler_in = True 
                # 한 명 이상의 참가자가 정사각형 내부에 있다면 sr,sc,square_size 정보를 갱신하고 끝 
                if is_traveler_in: 
                    sr,sc = r1,c1 
                    square_size = sz 
                    return 
# 정사각형 내부 벽을 회전 
def rotate_square(): 
    # 정사각형 내부의 벽을 1 감소 
    for r in range(sr, sr + square_size): 
        for c in range(sc, sc + square_size): 
            if board[r][c]: 
                board[r][c] -= 1 
    # 정사각형을 시계방향 90도 회전 
    for r in range(sr, sr + square_size): 
        for c in range(sc, sc + square_size): 
            # step1. (sr, sc)를 (0,0) 으로 옮겨주는 변환 
            o_r, o_c = r - sr, c - sc 
            # step2 변환된 상태에서 회전 이후 좌표가 (r,c), (c, square_n - r - 1)
            rc, rr = o_c, square_size - o_r - 1 
            # step3 다시 (sr, sc)를 더함 
            next_board[rr + sr][rc + sc] = board[r][c] 
    # next board값을 현재 board로 
    for r in range(sr, sr + square_size): 
        for c in range(sc, sc + square_size): 
            board[r][c] = next_board[r][c] 
# 모든 참가자들 및 출구를 회전
def rotate_player_and_exit(): 
    global exits 
    for i in range(1, M+1): 
        tr,tc = player[i] 
        # 참가자가 정사각형 내부일 때만 회전 
        if sr <= tr < sr + square_size and sc <= tc < sc + square_size:
            # step1: sr,sc 를 0,0 으로 옮겨주는 변환 
            o_r, o_c = tr - sr, tc - sc 
            # step2: 변환된 상태에서는 회전 이후 좌표가 (r,c), (c, square_size - r-1)
            rr, rc = o_c, square_size - o_r - 1 
            # step3: 다시 sr, sc를 더함 
            player[i] = (rr + sr, rc + sc) 
    # 출구에도 회전 
    if sr <= er < sr + square_size and sc <= ec < sc + square_size:
        # step1: (sr,sc)를 (0,0)으로 옮겨주는 변환 
        o_r, o_c = er - sr, ec - sc 
        # step2: 변환된 상태 회전 후 좌표가 (r,c), (c,square_size-r-1) 
        rr, rc = o_r, square_size - o_r - 1 
        # step3: 다시 (sr,sc)를 더함 
        exits = (rr + sr, rc + sc) 

for _ in range(K): 
    # 모든 플레이어 이동 
    move_all_player() 
    # 모든 사람이 탈출했는지 판단 
    is_all_escaped = True 
    for i in range(1, M+1): 
        if player[i] != exits: 
            is_all_escaped = False 
    # 모두 탈출했으면 바로 종료 
    if is_all_escaped: 
        break 
    
    # 한 명 이상 참가자와 최소 정사각형 탐색 
    find_minimum_square() 
    # 정사각형 내부 벽 회전 
    rotate_square() 
    # 모든 참가자들 및 출구 회전 
    rotate_player_and_exit() 
print(ans) 
er,ec = exits
print(er, ec)