n, m, r, c = map(int, input().split())

arr = [[0] * n for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
r -= 1
c -= 1
arr[r][c] = 1

# for t in range(1, m):
#     for i in range(n):
#         for j in range(n):
#                 if arr[i][j] == t:
#                     for d in range(4):
#                         # if 0<= i + dx[dir] * t <n and 0<= j + dy[dir] * t <n:
#                         nx = i + dx[d] * (2 ** (t-1))
#                         ny = j + dy[d] * (2 ** (t-1))
#                         print(nx, ny)

#                         if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
#                             arr[nx][ny] = t + 1
for t in range(1, m + 1):
    new_bombs = []  
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1: 
                for d in range(4): 
                    nx = i + dx[d] * (2 ** (t - 1))
                    ny = j + dy[d] * (2 ** (t - 1))
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                        new_bombs.append((nx, ny))
    for x, y in new_bombs:
        arr[x][y] = 1  

ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] > 0:
            ans += 1

print(ans)