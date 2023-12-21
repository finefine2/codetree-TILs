# N = 4 
# answer = [[0] * N for _ in range(N)] 
# # 0 1 2 3 
# # R D L U
# drs, dcs = [0,1,0,-1], [1,0,-1,0]
# r,c = 0,0 
# dir_num = 0
# answer[r][c] = 1 

# # 소용돌이 회전 
# def in_range(r,c): 
#     return 0 <= r < N and 0 <= c < N 
# for i in range(2, N * N + 1): 
#     nr,nc = r + drs[dir_num], c + dcs[dir_num] 
#     # 더 이상 나아갈 수 없다면 90% 회전 
#     if not in_range(nr,nc) or answer[nr][nc] != 0: 
#         dir_num = (dir_num + 1) % 4 
#     # 그 다음 이동한 다음 배열 값 업데이트 
#     r,c = r + drs[dir_num], c + dcs[dir_num] 
#     answer[r][c] = i 
# # print 
# for i in range(N): 
#     for j in range(N): 
#         print(answer[i][j], end = " ")
#     print() 

N, M = map(int,input().split()) 

board = [[0] * M for _ in range(N)] 
r,c = 0,0 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < M 

drs, dcs = [0,1,0,-1], [1,0,-1,0]
dir_num = 0 

board[r][c] = 1
for i in range(2, N * M + 1): 
    nr, nc = r + drs[dir_num], c + dcs[dir_num]
    if not in_range(nr,nc) or board[nr][nc] != 0:
        dir_num = (dir_num + 1) % 4 
    r,c = r + drs[dir_num], c+ dcs[dir_num] 
    board[r][c] = i 

for i in range(N): 
    for j in range(M): 
        print(board[i][j], end = " ")
    print()