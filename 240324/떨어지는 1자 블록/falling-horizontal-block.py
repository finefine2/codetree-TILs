N,M,K = map(int,input().split()) 
board = [list(map(int,input().split())) for _ in range(N)] 

start_r = 0 
start_c = K - 1
blocks = [1] * M

dr = 1
dc = 0 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

def check(r,c): 
    nr,nc = r + dr, c + dc 
    return in_range(nr,nc) and board[nr][nc] == 0 

def move(): 
    global start_r, start_c
    can_move = True 
    for i in range(M): 
        if not check(start_r, start_c+i): 
            can_move = False     
    if can_move: 
        start_r += 1 
        return True 
    else: 
        return False 

while True: 
    availability = move() 
    if not availability: 
        break 
    
for i in range(M): 
    board[start_r][start_c+i] = 1 

for b in board: 
    print(*b)