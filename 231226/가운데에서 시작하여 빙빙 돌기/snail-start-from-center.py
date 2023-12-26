N = int(input()) 
# 0 1 2 3 
# R U L D 
drs, dcs = [0,-1,0,1], [1,0,-1,0] 

board = [[0] * N for _ in range(N)] 
visited = [[False] * N for _ in range(N)] 

def check_move(r,c): 
    if 0 <= r < N and 0 <= c < N and visited[r][c] == False: 
        return True 
    else: 
        return False 

dir_num = 0 
r,c = N // 2, N // 2 
board[r][c] = 1 
visited[r][c] = True 

for i in range(2, N*N+1): 
    while True: 
        nr, nc = r + drs[dir_num], c + dcs[dir_num]
        if check_move(nr,nc): 
            r,c = nr,nc 
            board[r][c] = i 
            visited[r][c] = True 
            break 
        else: 
            dir_num = (dir_num+1) % 4

for i in range(N): 
    for j in range(N): 
        print(board[i][j], end =" ")
    print()