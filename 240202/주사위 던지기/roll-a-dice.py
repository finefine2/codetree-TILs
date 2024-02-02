n, m, r, c = map(int, input().split())
d = list(map(str, input().split()))
r -= 1
c -= 1

def isin(x, y):
    return 0 <= x < n and 0 <= y < n

arr = [[0] * n for _ in range(n)]

now = 1
up, front, rear = 1, 2, 3
dic = {'R': 0, 'L': 1, 'U': 2, 'D': 3}
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dice(dir):
    global r, c, up, front, rear, now
    nx, ny = r + dx[dic[dir]], c + dy[dic[dir]]

    if isin(nx, ny):
        if dir == 'R':
            up, front, rear = 7 - rear, front, up
        elif dir == 'L':
            up, front, rear = rear, front, 7 - up
        elif dir == 'U':
            up, front, rear = front, 7 - up, rear
        elif dir == 'D':
            up, front, rear = 7 - front, up, rear

        arr[nx][ny] = 7 - up
        r, c = nx, ny

arr[r][c] = 6
for i in range(m):
    dice(d[i])

ans = 0
for i in range(n):
    for j in range(n):
        ans += arr[i][j]
print(ans)





#     #       2
#     # 6  4  1  3
#     #       5

#     #       6
#     # 5  4  2  3
#     #       1

#     #       1
#     # 4  2  3  5
#     #       6

#     #       5
#     # 3  1  4  6
#     #       2

#     #       1
#     # 2  4  5  3
#     #       6

#     #       5
#     # 1  4  6  3
#     #       2


# arr[r][c] = 6

# # 6   
# for i in range(m):
#     if arr[r][c] == 6:
#         if d[i] == 'L':
#             if isin(r, c-1):
#                 r, c = r, c-1
#                 arr[r][c] = 4
#         elif d[i] == 'R':
#             if isin(r, c+1):
#                 r, c = r, c+1
#                 arr[r][c] = 3
#         elif d[i] == 'U':
#             if isin(r-1, c):
#                 r, c = r-1, c
#                 arr[r][c] = 5
#         elif d[i] == 'D':
#             if isin(r+1, c):
#                 r, c = r+1, c
#                 arr[r][c] = 2
#     # 5    4 3 1 6
#     elif arr[r][c] == 5:
#         if d[i] == 'L':
#             if isin(r, c-1):
#                 r, c = r, c-1
#                 arr[r][c] = 4
#         elif d[i] == 'R':
#             if isin(r, c+1):
#                 r, c = r, c+1
#                 arr[r][c] = 3
#         elif d[i] == 'U':
#             if isin(r-1, c):
#                 r, c = r-1, c
#                 arr[r][c] = 1
#         elif d[i] == 'D':
#             if isin(r+1, c):
#                 r, c = r+1, c
#                 arr[r][c] = 6
    
#     # 4 1652
#     elif arr[r][c] == 4:
#         if d[i] == 'L':
#             if isin(r, c-1):
#                 r, c = r, c-1
#                 arr[r][c] = 1
#         elif d[i] == 'R':
#             if isin(r, c+1):
#                 r, c = r, c+1
#                 arr[r][c] = 6
#         elif d[i] == 'U':
#             if isin(r-1, c):
#                 r, c = r-1, c
#                 arr[r][c] = 5
#         elif d[i] == 'D':
#             if isin(r+1, c):
#                 r, c = r+1, c
#                 arr[r][c] = 2
    
#     # 3 2516
#     elif arr[r][c] == 3:
#         if d[i] == 'L':
#             if isin(r, c-1):
#                 r, c = r, c-1
#                 arr[r][c] = 2
#         elif d[i] == 'R':
#             if isin(r, c+1):
#                 r, c = r, c+1
#                 arr[r][c] = 5
#         elif d[i] == 'U':
#             if isin(r-1, c):
#                 r, c = r-1, c
#                 arr[r][c] = 1
#         elif d[i] == 'D':
#             if isin(r+1, c):
#                 r, c = r+1, c
#                 arr[r][c] = 6

#     # 2 4361
#     elif arr[r][c] == 2:
#         if d[i] == 'L':
#             if isin(r, c-1):
#                 r, c = r, c-1
#                 arr[r][c] = 4
#         elif d[i] == 'R':
#             if isin(r, c+1):
#                 r, c = r, c+1
#                 arr[r][c] = 3
#         elif d[i] == 'U':
#             if isin(r-1, c):
#                 r, c = r-1, c
#                 arr[r][c] = 6
#         elif d[i] == 'D':
#             if isin(r+1, c):
#                 r, c = r+1, c
#                 arr[r][c] = 1

#     # 1 4325
#     elif arr[r][c] == 1:
#         if d[i] == 'L':
#             if isin(r, c-1):
#                 r, c = r, c-1
#                 arr[r][c] = 4
#         elif d[i] == 'R':
#             if isin(r, c+1):
#                 r, c = r, c+1
#                 arr[r][c] = 3
#         elif d[i] == 'U':
#             if isin(r-1, c):
#                 r, c = r-1, c
#                 arr[r][c] = 2
#         elif d[i] == 'D':
#             if isin(r+1, c):
#                 r, c = r+1, c
#                 arr[r][c] = 5


# ans = 0
# for i in range(n):
#     for j in range(n):
#         ans += arr[i][j]
#         print(arr[i][j], end = " ")
#     print()

# print(ans)