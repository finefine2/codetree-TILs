import copy 
N,M,Q = map(int,input().split()) 

board = [list(map(int,input().split())) for _ in range(N)] 

rects = [] 

for _ in range(Q): 
    r1,c1,r2,c2 = map(int,input().split())
    rects.append((r1-1,c1-1,r2-1,c2-1)) 

drs,dcs = [-1,0,1,0],[0,-1,0,1]

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < M 

def check_mean(r,c): 
    ans = board[r][c]
    cnt = 1 
    for dr, dc in zip(drs,dcs):  
        nr,nc = r + dr, c + dc 
        if in_range(nr,nc): 
            ans += board[nr][nc] 
            cnt += 1
    return ans, cnt 
# r1 c1 r2 c2 
# 1 1 3 5 
def wind(r1,c1,r2,c2): 
    new_board = copy.deepcopy(board)
    tmp = new_board[r1][c1]
    # 왼쪽 열 이동
    for i in range(r1, r2):
        new_board[i][c1] = new_board[i + 1][c1]

    # 아래쪽 행 이동
    for i in range(c1, c2):
        new_board[r2][i] = new_board[r2][i + 1]

    # 오른쪽 열 이동
    for i in range(r2, r1, -1):
        new_board[i][c2] = new_board[i - 1][c2]

    # 위쪽 행 이동
    for i in range(c2, c1, -1):
        new_board[r1][i] = new_board[r1][i - 1]

    # 첫 번째 요소를 마지막에 삽입
    new_board[r1][c1 + 1] = tmp
    # 내부 
    # for i in range(r1,r2+1): 
    #     for j in range(c1,c2+1): 
    #         ans, cnt = check_mean(i,j)
    #         new_board[i][j] = int(ans/cnt) 

    ans = copy.deepcopy(new_board)
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            cnt = 1
            s = 0
            s += ans[i][j]
            if i - 1 >= 0:
                s += ans[i-1][j]
                cnt += 1
            if i + 1 < N:
                s += ans[i+1][j]
                cnt += 1
            if j - 1 >= 0:
                s += ans[i][j-1]
                cnt += 1
            if j + 1 < M:
                s += ans[i][j+1]
                cnt += 1

            new_board[i][j] = (s // cnt)
    return new_board

for i in range(Q): 
    r1,c1,r2,c2 = rects[i] 
    board = wind(r1,c1,r2,c2) 

for b in board: 
    print(*b)