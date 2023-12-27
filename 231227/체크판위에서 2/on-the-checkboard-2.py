# N = int(input())
# board = [list(map(int,input().split())) for _ in range(N)] 
# max_cnt = 0 

# for i in range(N): 
#     for j in range(N-1): 
#         for k in range(i+1, N): 
#             for l in range(N-1): 
#                 max_cnt = max(max_cnt, board[i][j] + board[i][j+1]
#                                        board[k][l] + board[k][l+1])
# print(max_cnt)

R, C = map(int,input().split()) 
board = [list(input().split()) for _ in range(R)] 

cnt = 0 

start_r, start_c = 0,0 
end_r, end_c = R-1, C-1
for i in range(1,R-1): 
    for j in range(1,C-1): 
        for k in range(i+1, R-1): 
            for l in range(j+1, C-1): 
                if board[start_r][start_c] != board[i][j] and board[i][j] != board[k][l] and board[k][l] != board[end_r][end_c]:
                    cnt += 1
print(cnt)