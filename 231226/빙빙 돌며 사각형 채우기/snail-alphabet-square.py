# 0 1 2 3 
# E S W N 
# N * M번 진행 
drs = [0,1,0,-1]
dcs = [1,0,-1,0]
N,M = map(int,input().split()) 

board = [[0] * M for _ in range(N)] 
dir_num = 0 
def in_range(r,c): 
    return 0 <= r < N and 0 <= c < M

def num_to_alpha(num): 
    ans = ""
    if num < 26: 
        ans = chr(65+num-1) 
    else: 
        ans = chr(65+num-26-1) 
    return ans 

r,c = 0,0
board[r][c] = "A"
for i in range(2, N*M+1):
    nr,nc = r + drs[dir_num], c + dcs[dir_num]
    if not in_range(nr,nc) or board[nr][nc] != 0: 
        dir_num = (dir_num+1) % 4 
    r,c = r + drs[dir_num], c + dcs[dir_num]
    board[r][c] = num_to_alpha(i)    
    
for i in range(len(board)): 
    for j in range(len(board[0])):
        print(board[i][j],end=" ")
    print()