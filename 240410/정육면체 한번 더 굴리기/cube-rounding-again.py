from collections import deque 

FACE_NUM = 6 
OUT_OF_BOARD = (-1,-1) 
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)] 

r,c = 0,0 
move_dir = 0 
# R D L U 
drs, dcs = [0,1,0,-1],[1,0,-1,0] 
# 초기 주사위 
up, front, right = 1, 2, 3 
q = deque() 
visited = [[False for _ in range(N)] for _ in range(N)] 
ans = 0 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 
# 주사위 바닥과 같은 숫자여야지만 이동 가능 
def can_go(r,c,target_num): 
    return in_range(r,c) and not visited[r][c] and board[r][c] == target_num

def bfs(r,c,target_num): 
    for i in range(N): 
        for j in range(N): 
            visited[i][j] = False 
    visited[r][c] = True 
    q.append((r,c)) 

    score = 0 

    while q: 
        curr_r, curr_c = q.popleft() 
        score += target_num

        for dr, dc in zip(drs,dcs): 
            new_r, new_c = curr_r + dr, curr_c + dc 
            if can_go(new_r, new_c, target_num): 
                q.append((new_r,new_c)) 
                visited[new_r][new_c] = True 
    return score 
def get_score(): 
    return bfs(r,c,board[r][c]) 

def next_pos(): 
    nr, nc = r + drs[move_dir], c + dcs[move_dir]
    return (nr,nc) if in_range(nr,nc) else OUT_OF_BOARD

def simulate(): 
    global ans
    global r,c,move_dir
    global up,front, right
    nr,nc = next_pos() 
    if (nr,nc) == OUT_OF_BOARD: 
        move_dir = (move_dir + 2) if move_dir < 2 else (move_dir - 2)
        nr,nc = next_pos() 
    r,c = nr,nc 
    ans += get_score() 

    if move_dir == 0: 
        up,front,right = 7-right, front, up 
    elif move_dir == 1: 
        up,front,right = 7 - front, up, right
    elif move_dir == 2: 
        up,front,right = right, front, 7-up 
    else: 
        up,front,right = front, 7-up, right 

    bottom = 7 - up 

    if bottom > board[r][c]: 
        move_dir = (move_dir + 1) % 4
    elif bottom < board[r][c]: 
        move_dir = (move_dir - 1) % 4 
for _ in range(M): 
    simulate() 
print(ans)