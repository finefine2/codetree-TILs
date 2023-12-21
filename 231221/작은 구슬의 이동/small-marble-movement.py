'''
먼저 움직이는 걸 설정해준다 

'''
N, T = map(int,input().split())
board = [[0] * N for _ in range(N)]

r,c,d = input().split() 
r,c = int(r)-1, int(c)-1

dirs = {} 
dirs['L'] = [0,-1]
dirs['R'] = [0,1]
dirs['U'] = [-1,0] 
dirs['D'] = [1,0]

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N

def reverse_d(d): 
    if d == "L":
        d = "R"
    elif d == "R": 
        d = "L"
    elif d == "U": 
        d = "D" 
    elif d == "D":
        d = "U"
    return d 
t = 0 
while t < T: 
    board[r][c] = 1 
    nr,nc = r + dirs[d][0], c + dirs[d][1] 
    if in_range(nr,nc) and board[nr][nc] == 0:
        board[nr][nc] = 1 
        board[r][c] = 0 
        r,c = nr,nc 
        t += 1 
    elif not in_range(nr,nc):
        d = reverse_d(d) 
        t += 1
print(r+1, c+1)