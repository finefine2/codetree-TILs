n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

cnt = 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def isin(x, y):
    return 0<=x<n and 0<=y<m

dir = 0
x, y = 0,0
arr[0][0] = cnt
cnt += 1
for i in range(1, n*m):
    if isin(x + dx[dir], y + dy[dir]) and arr[x+dx[dir]][y+dy[dir]] == 0:
        x += dx[dir]
        y += dy[dir]
        arr[x][y] = cnt
        cnt += 1
        
    else:
        dir = (dir + 1) % 4
        x += dx[dir]
        y += dy[dir]
        arr[x][y] = cnt
        cnt += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()