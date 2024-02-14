from collections import deque

n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def isin(a, b):
    return 0 <= a < n and 0 <= b < n

ans = 0
for i in range(n):
    for j in range(n):
        q = deque()
        dp = [[1] * n for _ in range(n)]

        q.append((i, j))
        while q:
            if len(q) > 250000:  # 큐의 크기가 최대 요소 수를 초과하면 중단
                break
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if isin(nx, ny) and arr[x][y] < arr[nx][ny]:
                    dp[nx][ny] = max(dp[x][y] + 1, dp[nx][ny])
                    q.append((nx, ny))

        for k in range(n):
            for l in range(n):
                ans = max(ans, dp[k][l])

print(ans)

        
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