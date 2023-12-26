# 중복하여 더해도 상관없기 때문에 
# N,T = map(int,input().split()) 
# r, c = N // 2, N // 2 

# s_in = input() 
# board = [list(map(int,input().split())) for _ in range(N)] 

# dir_num = 0 
# def in_range(r,c): 
#     return 0 <= r < N and 0 <= c < N 

# drs, dcs = [-1,0,1,0],[0,1,0,-1] 
# ans = board[r][c] 
# for s in s_in: 
#     if s == "F": 
#         nr,nc = r + drs[dir_num], c + dcs[dir_num]
#         if not in_range(nr,nc):
#             continue
#         else: 
#             r,c = nr,nc 
#             ans += board[r][c]
#     elif s == "L": 
#         dir_num = (dir_num-1) % 4 
#     elif s == "R": 
#         dir_num = (dir_num+1) % 4
# print(ans) 

N, T = map(int,input().split()) 
commands = input() 
board = [list(map(int,input().split())) for _ in range(N)] 

ans = 0 
r,c,move_dir = N // 2, N // 2, 0 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

def simulate(): 
    global ans 
    global r, c, move_dir
    drs = [-1,0,1,0]
    dcs = [0,1,0,-1] 
    for com in commands: 
        if com == "R": 
            move_dir = (move_dir + 1) % 4 
        elif com == "L": 
            move_dir = (move_dir - 1) % 4 
        else: 
            nr, nc = r + drs[move_dir], c + dcs[move_dir] 
            # 이동할 수 있으면 이동 
            if in_range(nr,nc): 
                ans += board[nr][nc] 
                r,c = nr,nc 
ans += board[r][c] 
simulate() 
print(ans)