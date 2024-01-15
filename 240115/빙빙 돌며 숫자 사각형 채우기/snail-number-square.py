n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def isin(a, b):
    if 0<=a<n and 0<=b<m:
        return True
    else:
        return False

dir = 0
cnt = 2
x, y = 0,0
arr[x][y] = 1
for i in range(2, n*m+1):
    nx = x + dx[dir]
    ny = y + dy[dir]

    if not isin(nx, ny) or arr[nx][ny] != 0:
        dir = (dir + 1) % 4

    x = x + dx[dir]
    y = y + dy[dir]
    arr[x][y] = cnt
    cnt += 1
    
    

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()