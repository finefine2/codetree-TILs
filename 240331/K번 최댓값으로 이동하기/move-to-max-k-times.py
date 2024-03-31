from collections import deque
N, K = map(int,input().split()) 

board = [list(map(int,input().split())) for _ in range(N)] 

r,c = map(int,input().split()) 
curr_pos = (r-1,c-1) 
not_exist = (-1,-1) 

q = deque() 
visited = [[False for _ in range(N)] for _ in range(N)] 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

def can_go(r,c,num): 
    return in_range(r,c) and not visited[r][c] and board[r][c] < num 

def initialize(): 
    for i in range(N): 
        for j in range(N): 
            visited[i][j] = False 

def bfs(): 
    drs, dcs = [0,1,0,-1], [1,0,-1,0] 
    curr_r, curr_c = curr_pos
    visited[curr_r][curr_c] = True 
    q.append(curr_pos) 
    num = board[curr_r][curr_c]

    while q: 
        curr_r, curr_c = q.popleft() 
        for dr, dc in zip(drs,dcs): 
            new_r, new_c = curr_r + dr, curr_c + dc 
            if can_go(new_r, new_c, num): 
                q.append((new_r, new_c)) 
                visited[new_r][new_c] = True
def check_update(best_pos, new_pos): 
    if best_pos == not_exist: 
        return True 
    best_r, best_c = best_pos
    new_r, new_c = new_pos

    return (board[new_r][new_c], -new_r, -new_c) > (board[best_r][best_c],-best_r,-best_c)

def move(): 
    global curr_pos
    initialize() 
    bfs() 

    best_pos = not_exist
    for i in range(N): 
        for j in range(N): 
            if not visited[i][j] or (i,j) == curr_pos: 
                continue 
            new_pos = (i,j) 
            if check_update(best_pos, new_pos): 
                best_pos = new_pos
    if best_pos == not_exist: 
        return False 
    else: 
        curr_pos = best_pos 
        return True 
for _ in range(K): 
    is_moved = move() 
    if not is_moved: 
        break 
final_r, final_c = curr_pos
print(final_r + 1, final_c + 1)