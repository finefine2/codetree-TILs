import copy 
import sys 
N = int(input()) 

board = [list(map(int,input().split())) for _ in range(N)] 

r,c,m1,m2,m3,m4,d = map(int,input().split()) 

# 이동 중에 격자 안에 있어야 함 
def in_range(r,c): 
    return 0 <= r < N and 0 <= c< N 

def find_rect(r,c,m1,m2,m3,m4): 
    start_r, start_c = r-1,c-1
    rects = [(start_r,start_c)] 
    cnt = 0 
    # direction 1 
    while cnt < m1: 
        start_r -= 1
        start_c += 1 
        if in_range(start_r,start_c) and (start_r,start_c) not in rects: 
            cnt += 1 
            rects.append((start_r,start_c))
        else: 
            break 
    cnt = 0
    # direction 2 
    while cnt < m2: 
        start_r -= 1
        start_c -= 1 
        if in_range(start_r,start_c) and (start_r,start_c) not in rects: 
            cnt += 1 
            rects.append((start_r,start_c))
        else: 
            break
    cnt = 0 
    # direction 3 
    while cnt < m3: 
        start_r += 1 
        start_c -= 1
        if in_range(start_r,start_c) and (start_r,start_c) not in rects: 
            cnt += 1 
            rects.append((start_r,start_c))
        else: 
            break
    cnt = 0 
    # direction 4 
    while cnt < m4:
        start_r += 1 
        start_c += 1 
        if in_range(start_r,start_c) and (start_r,start_c) not in rects: 
            rects.append((start_r,start_c))
            cnt += 1 
        else: 
            break
    return rects 

rect = find_rect(r,c,m1,m2,m3,m4)
def rotate(rect,d):
    coord = rect 
    new_cord = [0] * len(coord)  
    # 반시계 방향으로 한칸씩 
    if d == 0: 
        tmp = coord[-1] 
        new_cord[1:] = coord[:-1]
        new_cord[0] = tmp
        
    # 시계 방향으로 한칸씩 
    elif d == 1: 
        tmp = coord[0] 
        new_cord[:-1] = coord[1:]
        new_cord[-1] = tmp 
    return new_cord 

new_cord = rotate(rect,d) 
new_board = copy.deepcopy(board) 
for i in range(len(rect)): 
    r,c = rect[i]
    nr,nc = new_cord[i] 
    board[r][c] = new_board[nr][nc] 
    
for b in board: 
    print(*b)