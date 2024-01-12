n, t = map(int, input().split())

r, c, d = map(str, input().split())

dx = [0,1,-1,0]
dy = [1,0,0,-1]


dir = {'R' : 0, 'D': 1, 'U' : 2, 'L': 3}

move_dir = dir[d]

def isin(x, y):
    return 0<=x<n and 0<=y<n

x, y = int(r) - 1, int(c) - 1

for i in range(t):
    nx = x +  dx[move_dir]
    ny = y +  dy[move_dir]
    if isin(nx, ny):
        x, y = nx, ny
    else:
        move_dir = 3 - move_dir

print(x + 1, y + 1)