from collections import deque
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
for i in range(n):
    for j in range(n):
        q = deque()
        dp = [[0] * n for _ in range(n)]

        q.append((i, j))
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if isin(nx, ny) and isin(x, y) and arr[x][y] < arr[nx][ny]:
                    dp[nx][ny] = max(dp[x][y] + 1, dp[nx][ny])
                    q.append((nx, ny))
        
        for k in range(n):
            for l in range(n):
                ans = max(ans, dp[k][l])

print(ans + 1)