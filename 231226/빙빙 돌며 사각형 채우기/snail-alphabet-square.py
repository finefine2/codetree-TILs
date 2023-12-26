# my solution 
# # 0 1 2 3 
# # E S W N 
# # N * M번 진행 
# drs = [0,1,0,-1]
# dcs = [1,0,-1,0]
# N,M = map(int,input().split()) 

# board = [[0] * M for _ in range(N)] 
# dir_num = 0 
# def in_range(r,c): 
#     return 0 <= r < N and 0 <= c < M

# alpha_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
#             "Q","R","S","T","U","V","W","X","Y","Z"]
# def num_to_alpha(num): 
#     ans = ""
#     remain = num % 26 
#     ans = alpha_list[remain-1]
#     return ans 
# r,c = 0,0
# board[r][c] = "A"
# for i in range(2, N*M+1):
#     nr,nc = r + drs[dir_num], c + dcs[dir_num]
#     if not in_range(nr,nc) or board[nr][nc] != 0: 
#         dir_num = (dir_num+1) % 4 
#     r,c = r + drs[dir_num], c + dcs[dir_num]
#     board[r][c] = num_to_alpha(i)    
    
# for i in range(len(board)): 
#     for j in range(len(board[0])):
#         print(board[i][j],end=" ")
#     print()

N,M = map(int,input().split())

answer = [[0] * M for _ in range(N)] 
visited = [[0] * M for _ in range(N)] 

def move(nr,nc): 
    if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0: 
        return True 
    else: 
        return False 
drs,dcs = [0,1,0,-1],[1,0,-1,0]
r,c = 0,0
dir_num = 0 
visited[r][c] = True 
answer[r][c] = "A"
for i in range(1,N*M): 
    while True: 
        nr,nc = r + drs[dir_num],  c+dcs[dir_num] 
        if move(nr,nc): 
            r,c = nr,nc 
            visited[r][c] = True 
            answer[r][c] = chr((i%26) + ord("A")) 
            break 
        else: 
            dir_num = (dir_num + 1) % 4 
for i in range(N): 
    for j in range(M): 
        print(answer[i][j],end=" ") 
    print()