from collections import deque

n, m = map(int, input().split())

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
                check[nx][ny] = check[x][y] + 1
                q.append((nx, ny))

q = deque()
check = [[0] * n for _ in range(n)]
check[0][0] = 0
q.append((0,0))
BFS()



if check[n-1][n-1] == 0 or check[n-1][n-1] == 1:
    print(-1)
else:
    print(check[n-1][n-1])