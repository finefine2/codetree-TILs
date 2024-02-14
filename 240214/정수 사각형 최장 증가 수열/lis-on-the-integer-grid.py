# from collections import deque
n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def isin(a, b):
    return 0<=a<n and 0<=b<n

ans = 0
dp = [[0] * n for _ in range(n)]

def DFS(x, y, dist):

    if dp[x][y]:
        return dp[x][y]

    Max = 0
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if isin(nx, ny) and arr[nx][ny] > arr[x][y]:
            Max = max(Max, dist + DFS(nx, ny, dist))


    dp[x][y] = Max
    
    return Max

for i in range(n):
    for j in range(n):
        if not dp[i][j]:
            DFS(i, j, 1)

print(max(map(max, dp))+1)

# for i in range(n):
#     for j in range(n):
#         ans = max(ans, dp[i][j])

# print(ans + 1)

        
# from collections import deque

# n = int(input())

# arr = []
# for i in range(n):
#     tmp = list(map(int, input().split()))
#     arr.append(tmp)

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# def isin(a, b):
#     return 0 <= a < n and 0 <= b < n

# ans = 0
# for i in range(n):
#     for j in range(n):
#         visited = [[False] * n for _ in range(n)]
#         q = deque([(i, j, 1)])  

#         while q:
#             x, y, dist = q.popleft()
#             visited[x][y] = True
#             ans = max(ans, dist) 

#             for k in range(4):
#                 nx = x + dx[k]
#                 ny = y + dy[k]
#                 if isin(nx, ny) and arr[x][y] < arr[nx][ny] and not visited[nx][ny]:
#                     q.append((nx, ny, dist + 1))

# print(ans)