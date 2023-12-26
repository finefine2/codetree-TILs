# 역방향으로 들어가는 코드를 구현하자 
# N = int(input()) 
# # L, U, R, D 
# drs, dcs = [0,-1,0,1], [-1,0,1,0] 
# board = [[0] * N for _ in range(N)] 
# visited = [[False] * N for _ in range(N)] 
# dir_num = 0 
# r,c = N-1, N-1
# board[r][c] = N * N
# visited[r][c] = True
# def check_move(r,c): 
#     if 0 <= r < N and 0 <= c < N and visited[r][c] == False: 
#         return True
#     else: 
#         return False

# for i in range(N*N-1, 0, -1):
#     while True: 
#         nr,nc = r + drs[dir_num], c + dcs[dir_num] 
#         if check_move(nr,nc): 
#             r,c = nr,nc 
#             board[r][c] = i 
#             visited[r][c] = True 
#             break 
#         else: 
#             dir_num = (dir_num+1) % 4 
# for i in range(N): 
#     for j in range(N): 
#         print(board[i][j],end = " ")
#     print() 

# given solution 
# direction: R U L D 
# movement 1 2 3 4 

N = int(input()) 
board = [[0] * N for _ in range(N)] 
r,c = N // 2, N // 2 
move_dir, move_num = 0, 1 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

def move(): 
    global r,c 
    # R U L D 
    drs, dcs = [0,-1,0,1],[1,0,-1,0]
    r,c = r + drs[move_dir], c + dcs[move_dir] 
def end(): 
    return not in_range(r,c)

# 시작 위치, 방향 그리고 이동횟수 
cnt = 1 
while not end(): 
    # move_num 만큼 이동 
    for _ in range(move_num): 
        board[r][c] = cnt 
        cnt += 1 
        move() 
        # 격자를 벗어나게 되면 움직이는 걸 종료 
        if end(): 
            break 
    # change direction 
    move_dir = (move_dir + 1) % 4 
    # 현재 방향이 왼쪽 혹은 오른쪽인 경우에는 특정방향으로 이동횟수 +1 
    if move_dir == 0 or move_dir == 2: 
        move_num += 1 
for i in range(N): 
    for j in range(N): 
        print(board[i][j],end=" ") 
    print()