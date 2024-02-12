# n = int(input())

# arr = []
# for i in range(n):
#     tmp = list(map(int, input().split()))
#     arr.append(tmp)


# def isin(a, b):
#     return 0<=a<n and 0<=b<n
# def ismove(a, b, k):
#     if not isin(a, b):
#         return False
#     if check[a][b] or arr[a][b] != k:
#         return False
#     return True

# dx = [0,0,1,-1]
# dy = [1,-1,0,0]

# def DFS(x, y, k):
#     global num
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if ismove(nx, ny, k):
#             check[nx][ny] = 1
#             num += 1
#             DFS(nx, ny, k)

# block = []
# ans = 0
# flag = False
# for k in range(1, 101):
#     check = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if not check[i][j]:
#                 num = 0
#                 DFS(i, j, k)
#                 if num >= 2:
#                     block.append(num)
#                     flag = True
#                 if num >= 4:
#                     ans += 1
    

# if not flag:
#     print(ans, 1)
# else:
#     print(ans, max(block))

n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

visited = [[False] * n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, value):
    global num
    num += 1
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == value:
            dfs(nx, ny, value)

blocks = []
ans = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            num = 0
            dfs(i, j, arr[i][j])
            if num >= 2:
                blocks.append(num)
            if num >= 4:
                ans += 1

if blocks:
    print(ans, max(blocks))
else:
    print(ans, 1)