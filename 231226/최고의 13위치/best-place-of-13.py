# N = int(input()) 
# board = [[0] * N for _ in range(N)] 

# max_cnt = 0 
# for i in range(N): 
#     for j in range(N-1): 
#         max_cnt = max(max_cnt, board[i][j] + board[i][j+1]) 

N = int(input()) 
board = [list(map(int,input().split())) for _ in range(N)] 
max_cnt = 0 

for i in range(N): 
    for j in range(N-2): 
        max_cnt = max(max_cnt, board[i][j] + board[i][j+1] + board[i][j+2])
print(max_cnt)