from collections import deque
n = int(input())

r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def isin(a, b):
    return 0<=a<n and 0<=b<n

check = [[0] * n for _ in range(n)]

def BFS():
    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if isin(nx, ny) and not check[nx][ny]:
                check[nx][ny] = check[x][y] + 1
                q.append((nx, ny))

q = deque()
if isin(r1, c1):
    check[r1][c1] = 0
    q.append((r1, c1))

BFS()

if r1 == r2 and c1 == c2:
    print(0)
if isin(r2, c2):
    if check[r2][c2] == 0:
        print(-1)
    else:
        print(check[r2][c2])