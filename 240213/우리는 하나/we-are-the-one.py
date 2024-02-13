from collections import deque
from itertools import combinations

n, k, u, d = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

country = ((i, j) for i in range(n) for j in range(n))
country_pick = combinations(country, k)

def isin(a, b):
    return 0<=a<n and 0<=b<n

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS():
    global num
    global check, q

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if isin(nx, ny) and not check[nx][ny] and u<=abs(arr[nx][ny] - arr[x][y])<=d:
                check[nx][ny] = 1
                num += 1
                q.append((nx, ny))

ans = 0
for start in country_pick:
    check = [[0] * n for _ in range(n)]
    q = deque()
    num = 0

    for i, j in start:
        if not check[i][j]:
            check[i][j] = True
            q.append((i, j))
            num += 1
            BFS()

    ans = max(ans, num)

print(ans)