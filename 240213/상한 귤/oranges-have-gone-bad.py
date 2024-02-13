from collections import deque

n, k = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)


def isin(a, b):
    return 0<=a<n and 0<=b<n

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if isin(nx, ny) and not check[nx][ny] and arr[nx][ny] == 1:
                check[nx][ny] = 1
                ans[nx][ny] = ans[x][y] + 1
                q.append((nx, ny))

ans = [[0] * n for _ in range(n)]
check = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            ans[i][j] = 0
            check[i][j] = 1

for t in range(100):
    q = deque()

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                q.append((i, j))
                check[i][j] = 1

    BFS()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and ans[i][j] == 0:
            ans[i][j] = -2
        elif arr[i][j] == 0:
            ans[i][j] = -1
        

for i in range(n):
    for j in range(n):
        print(ans[i][j], end = " ")
    print()