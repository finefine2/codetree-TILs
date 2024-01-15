n = int(input())

arr = [[0] * n for _ in range(n)]

cnt = 1

dx = [0,-1,0,1]
dy = [1,0,-1,0]

def isin(x, y):
    return 0<=x<n and 0<=y<n

dir = 0
x, y = n//2,n//2
arr[n//2][n//2] = cnt
cnt += 1
num = 1
for i in range(1, n * n):
    for k in range(num):
        if isin(x + dx[dir], y + dy[dir]) and arr[x + dx[dir]][y + dy[dir]] == 0:
            x += dx[dir]
            y += dy[dir]
            arr[x][y] = cnt
            cnt += 1
    dir = (dir + 1) % 4  
    if i % 2 == 0:
        num += 1


for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()