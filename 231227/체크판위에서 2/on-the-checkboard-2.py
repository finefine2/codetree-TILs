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

# 문제 이해에 꽤 걸렸으나 어찌저찌 풀었음 
# R, C = map(int,input().split()) 
# board = [list(input().split()) for _ in range(R)] 

# cnt = 0 

# start_r, start_c = 0,0 
# end_r, end_c = R-1, C-1
# for i in range(1,R-1): 
#     for j in range(1,C-1): 
#         for k in range(i+1, R-1): 
#             for l in range(j+1, C-1): 
#                 if board[start_r][start_c] != board[i][j] and board[i][j] != board[k][l] and board[k][l] != board[end_r][end_c]:
#                     cnt += 1
# print(cnt) 

# given solution
R,C = map(int,input().split()) 
board = [input().split() for _ in range(R)]

cnt = 0 
# 점프 후 처음으로 밟는 위치와 그 다음으로 밟는 위치를 전부 정하는 완탐 + 행, 열은 전부 증가하는 방향
# 점프 이후 첫 번째, 두 번째로 방문하는 위치를 일일이 짚어보며 모든 알파벳이 다른지 확인 
for i in range(1,R): 
    for j in range(1,C): 
        for k in range(i+1,R-1): 
            for l in range(j+1,C-1): 
                if board[0][0] != board[i][j] and board[i][j] != board[k][l] and board[k][l] != board[R-1][C-1]: 
                    cnt += 1 
print(cnt)