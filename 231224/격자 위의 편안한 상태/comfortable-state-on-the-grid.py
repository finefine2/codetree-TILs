# my solution 
# N, M = map(int,input().split()) 

# board = [[0] * N for _ in range(N)] 

# drs, dcs = [1,0,-1,0],[0,1,0,-1]
# def in_range(r,c): 
#     return 0 <= r < N and 0 <= c < N 

# def count_block(r,c):
#     cnt = 0  
#     for i in range(4): 
#         nr, nc = r + drs[i], c + dcs[i] 
#         if in_range(nr,nc) and board[nr][nc] == 1: 
#             cnt += 1 
#     if cnt == 3: 
#         return True 
#     else: 
#         return False 

# for _ in range(M): 
#     r,c = map(int,input().split()) 
#     r,c = r-1, c-1 
#     board[r][c] = 1 
#     if count_block(r,c): 
#         print(1) 
#     else: 
#         print(0)

N,M = map(int,input().split()) 
board = [[0] * N for _ in range(N)] 

drs = [1,0,-1,0]
dcs = [0,1,0,-1]

def in_range(r,c):
    return 0 <= r < N and 0 <= c < N 

def close_cnt(r,c): 
    cnt = 0 
    for dr, dc in zip(drs, dcs): 
        nr,nc = r + dr, c + dc 
        if in_range(nr,nc) and board[nr][nc] == 1: 
            cnt += 1
    return cnt 

for _ in range(M): 
    r,c = map(int,input().split()) 
    r -= 1 
    c -= 1 
    board[r][c] = 1 
    if close_cnt(r,c) == 3: 
        print(1) 
    else: 
        print(0 )