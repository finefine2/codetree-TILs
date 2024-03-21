import copy 

N = int(input())

board = [list(map(int,input().split())) for _ in range(N)] 

start_r, start_c = map(int,input().split()) 
start_r -= 1 
start_c -= 1 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

drs, dcs = [-1,0,1,0], [0,-1,0,1] 

'''
한번의 사이클 동안 
bomb 
move - 빈 칸은 모두 0 으로 
'''
def bomb(r,c): 
    global board, drs, dcs 
    tmp = copy.deepcopy(board) 
    
    length = tmp[r][c] 
    for i in range(length): 
        for dr,dc in zip(drs,dcs): 
            nr,nc = r + dr * i, c + dc * i 
            if in_range(nr,nc): 
                tmp[nr][nc] = 0 
                board[nr][nc] = tmp[nr][nc] 
    return tmp 

mid = bomb(start_r,start_c)


tmp = [[0] * N for _ in range(N)] 
for c in range(N): 
    next_r = N-1 
    for r in range(N-1,-1,-1): 
        if mid[r][c]: 
            tmp[next_r][c] = mid[r][c]
            next_r -= 1
for r in range(N): 
    for c in range(N): 
        mid[r][c] = tmp[r][c] 
for m in mid: 
    print(*m)
# for m in mid: 
#     print(*m)
# tmp 배열을 만들어서 0이 아닌 건 다 이동시킨다 
# def move(arr): 
#     tmp = copy.deepcopy(arr) 
#     # BLANK = 0 
#     # end_of_arr = len(tmp) 
#     for j in range(len(tmp)): 
#         for i in range(len(tmp)-1): 
#             # if tmp[i+1][j] == 0 and tmp[i][j] != 0:
#             #     tmp[i+1][j], tmp[i][j] = tmp[i][j], tmp[i+1][j]
#             if tmp[i+1][j] == 0: 
#                 mid = tmp[i+1][j]
#     return tmp