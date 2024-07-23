FACE_NUM = 6 
OUT_OF_GRID = (-1,-1) 

N,M,r,c,k = tuple(map(int,input().split())) 
board = [list(map(int,input().split())) for _ in range(N)] 

movements = list(map(int,input().split()))

up, front, right = 1,2,3 

dices = [0 for _ in range(FACE_NUM+1)]

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < M 
# 해당 방향으로 이동 시 다음 위치 이동 불가하면 out
def next_pos(r,c,move_dir): 
    drs, dcs = [0,0,0,-1,1], [0,1,-1,0,0] 
    nr,nc = r + drs[move_dir], c + dcs[move_dir] 
    return (nr,nc) if in_range(nr,nc) else OUT_OF_GRID

def simulate(move_dir): 
    global r,c,up,front,right

    nr,nc = next_pos(r,c,move_dir) 
    if (nr,nc) == OUT_OF_GRID: 
        return 
    
    r,c = nr,nc

    if move_dir == 1: 
        up, front, right = 7-right, front, up 
    elif move_dir == 2: 
        up, front, right = right, front, 7-up 
    elif move_dir == 3: 
        up, front, right = front, 7-up, right
    else: 
        up, front, right = 7 - front, up, right 

    bottom = 7 - up 

    if board[r][c] == 0: 
        board[r][c] = dices[bottom]
    else: 
        dices[bottom] = board[r][c] 
        board[r][c] = 0 
    print(dices[up]) 
for move_dir in movements: 
    simulate(move_dir)