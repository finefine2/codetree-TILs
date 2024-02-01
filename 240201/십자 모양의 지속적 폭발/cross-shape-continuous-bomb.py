# n, m = map(int, input().split())

# arr = []
# for i in range(n):
#     tmp = list(map(int, input().split()))
#     arr.append(tmp)

# bomb = []
# for i in range(m):
#     c = int(input())
#     bomb.append(c-1)

# dx = [0,0,1,-1]
# dy = [1,-1,0,0]

# for k in bomb:
#     num = 0
#     for i in range(n):
#         if arr[i][k] != 0:
#             if num == 0:
#                 arr[i][k] = 0
#             else:
#                 arr[i][k] = 0
#                 for dir in range(4):
#                     for j in range(1, num+1):
#                         nx = i + dx[dir] * j
#                         ny = k + dy[dir] * j
                        
#                         if 0<=nx<n and 0<=ny<n:
#                             arr[nx][ny] = 0
#                         else:
#                             break
#                 num += 1
            
#             for ii in range(n-1, -1, -1):
#                 for jj in range(n):
#                     if arr[ii][jj] == 0:
#                         for kk in range(i, 0, -1):
#                             arr[kk][jj] = arr[kk-1][jj]
#                             arr[kk-1][jj] = 0

            

# for i in range(n):
#     for j in range(n):
#         print(arr[i][j], end = " ")
#     print()

n, m = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

bomb = []
for i in range(m):
    c = int(input())
    bomb.append(c-1)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def explode(x, y, size):
    arr[x][y] = 0
    for dir in range(4):
        for i in range(1, size):
            nx = x + dx[dir] * i
            ny = y + dy[dir] * i
            
            if 0 <= nx < n and 0 <= ny < n:
                arr[nx][ny] = 0

def gravity():
    for j in range(n):
        col = []
        for i in range(n):
            if arr[i][j] != 0:
                col.append(arr[i][j])
                arr[i][j] = 0
        for i in range(n - len(col), n):
            arr[i][j] = col[i - (n - len(col))]

for k in bomb:
    x = 0
    while x < n and arr[x][k] == 0:
        x += 1
    if x < n:
        size = arr[x][k]
        explode(x, k, size)
        gravity()

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()