'''
목표는 레이저가 맵 밖을 나가기 전까지 거울에 튕기는 횟수를 카운팅하는 것 
'''

N = int(input()) 
board = []
 
for _ in range(N): 
    board.append(list(input().strip())) 

K = int(input()) 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N

def start_pos(num):
    r,c = 0,0 
    curr_dir = 0 
    if 1 <= num <= N: 
        r,c = -1,num-1
        curr_dir = 0 
    elif N+1 <= num <= 2*N: 
        r,c = num-N-1,N
        curr_dir = 1
    elif 2*N + 1 <= num <= 3*N: 
        r,c = N, 3*N - num
        curr_dir = 2
    elif 3*N + 1 <= num <= 4*N: 
        r,c = 4*N - num,-1
        curr_dir = 3 
    return r,c,curr_dir
# 0 1 2 3 
# D L U R
'''
0 + / = 1 
0 + \ = 3 

1 + / = 0
1 + \ = 2

2 + / = 3 
2 + \ = 1

3 + / = 2
3 + \ = 0
'''
def change_dir(dirs, c): 
    if dirs % 2 == 0: 
        if c == "/": 
            dirs = (dirs + 1) % 4
        elif c == "\\":
            dirs = (dirs - 1) % 4
    elif dirs % 2 != 0: 
        if c == "/": 
            dirs = (dirs - 1) % 4
        elif c == "\\": 
            dirs = (dirs + 1) % 4
    return dirs 
drs = [1,0,-1,0] 
dcs = [0,-1,0,1]
dirs = 0 

start_r, start_c, start_dir = start_pos(K)

cnt = 0 
while True: 
    nr, nc = start_r + drs[start_dir], start_c + dcs[start_dir] 
    if in_range(nr,nc): 
        cnt += 1
        start_dir = change_dir(start_dir,board[nr][nc]) 
        start_r, start_c = nr, nc 
    else: 
        break 
print(cnt)