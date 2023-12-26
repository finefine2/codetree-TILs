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

alpha_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
            "Q","R","S","T","U","V","W","X","Y","Z"]
def num_to_alpha(num): 
    ans = ""
    remain = num % 26 
    ans = alpha_list[remain-1]
    return ans 
    # if num <= 26: 
    #     ans = chr(65+num-1) 
    # else: 
    #     ans = chr(65+num-26-1) 
    # return ans 

# def num_to_alpha(new_num): 
#     ans = ""
#     num = 0 
#     if new_num < =26:
#         num = 65 + new_num - 1
#     else: 
#         num = 65 + new_num -2
#     if num % 26 == 0: 
#     elif num % 26 == 1:
#     elif num % 26 == 2:
#     elif num % 26 == 3:
#     elif num % 26 == 4:                
#     elif num % 26 == 5:
#     elif num % 26 == 6:
#     elif num % 26 == 7:
#     elif num % 26 == 8:
#     elif num % 26 == 9:
#     elif num % 26 == 10:
#     elif num % 26 == 11:
#     elif num % 26 == 12:
#     elif num % 26 == 13:
#     elif num % 26 == 14:
#     elif num % 26 == 15:
#     elif num % 26 == 16:
#     elif num % 26 == 17:
#     elif num % 26 == 18:
#     elif num % 26 == 19:
#     elif num % 26 == 20:
#     elif num % 26 == 21:
#     elif num % 26 == 22:
#     elif num % 26 == 23:
#     elif num % 26 == 24:
#     elif num % 26 == 25:        

# print(ord("A"))
# print(ord("Z"))
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