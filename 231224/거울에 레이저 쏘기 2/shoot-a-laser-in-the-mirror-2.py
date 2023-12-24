'''
my solution 
레이저 포인트의 시작위치와 방향 관련 설정들을 각각 함수로 구현해줌 
목표는 레이저가 맵 밖을 나가기 전까지 거울에 튕기는 횟수를 카운팅하는 것 
'''
# N = int(input()) 
# board = []
 
# for _ in range(N): 
#     board.append(list(input().strip())) 

# K = int(input()) 

# def in_range(r,c): 
#     return 0 <= r < N and 0 <= c < N

# def start_pos(num):
#     r,c = 0,0 
#     curr_dir = 0 
#     if 1 <= num <= N: 
#         r,c = -1,num-1
#         curr_dir = 0 
#     elif N+1 <= num <= 2*N: 
#         r,c = num-N-1,N
#         curr_dir = 1
#     elif 2*N + 1 <= num <= 3*N: 
#         r,c = N, 3*N - num
#         curr_dir = 2
#     elif 3*N + 1 <= num <= 4*N: 
#         r,c = 4*N - num,-1
#         curr_dir = 3 
#     return r,c,curr_dir
# # 0 1 2 3 
# # D L U R
# '''
# 0 + / = 1 
# 0 + \ = 3 

# 1 + / = 0
# 1 + \ = 2

# 2 + / = 3 
# 2 + \ = 1

# 3 + / = 2
# 3 + \ = 0
# '''
# def change_dir(dirs, c): 
#     if dirs % 2 == 0: 
#         if c == "/": 
#             dirs = (dirs + 1) % 4
#         elif c == "\\":
#             dirs = (dirs - 1) % 4
#     elif dirs % 2 != 0: 
#         if c == "/": 
#             dirs = (dirs - 1) % 4
#         elif c == "\\": 
#             dirs = (dirs + 1) % 4
#     return dirs 
# drs = [1,0,-1,0] 
# dcs = [0,-1,0,1]
# dirs = 0 

# start_r, start_c, start_dir = start_pos(K)

# cnt = 0 
# while True: 
#     nr, nc = start_r + drs[start_dir], start_c + dcs[start_dir] 
#     if in_range(nr,nc): 
#         cnt += 1
#         start_dir = change_dir(start_dir,board[nr][nc]) 
#         start_r, start_c = nr, nc 
#     else: 
#         break 
# print(cnt) 

# given solution 
'''
/ 모양을 만나면 0 <-> 1, 2<-> 3 으로 방향이 바뀌고. 이는 현재 방향에 1을 xor 연산한 것 
xor 연산은 비트 단위로 연산하되, 각 bit당 같은 숫자면 0 다른 수면 1을 만들어줌 
\ 모양의 경우에는 0 <-> 3, 1<-> 2 이렇게 바뀜. 숫자3에서 현재 방향을 빼줌 
'''
N = int(input())
board = [input() for _ in range(N)] 
start_num = int(input()) 

# 주어진 숫자에 따라 시작 위치와 방향을 구한다 
def initialize(num): 
    if num <= N: 
        return 0, num-1, 0 
    elif num <= 2 * N: 
        return num - N -1, N-1, 1 
    elif num <= 3 * N: 
        return N - 1, N - (num - 2*N), 2 
    else: 
        return N - (num - 3 * N), 0, 3 
def in_range(r,c): 
    return 0 <= r< N and 0 <= c < N     

# r,c 에서 시작해 next_dir 방향으로 이동한 후 위치를 리턴 
def move(r,c,next_dir): 
    drs, dcs = [1,0,-1,0], [0,-1,0,1] 
    nr, nc = r + drs[next_dir], c + dcs[next_dir]
    return nr,nc,next_dir

def simulate(r,c,move_dir):
    move_num = 0 
    while in_range(r,c): 
        if board[r][c] == "/":
            r,c,move_dir = move(r,c,move_dir^1) 
        else: 
            r,c,move_dir = move(r,c,3-move_dir) 
        move_num += 1 
    return move_num 
# 시작 위치, 방향을 구한다 
r,c,move_dir = initialize(start_num) 
move_num = simulate(r,c,move_dir) 
print(move_num)