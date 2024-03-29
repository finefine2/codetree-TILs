from collections import deque
n, k = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def isin(a, b):
    return 0<=a<n and 0<=b<n

def BFS():
    global num
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if isin(nx, ny) and not check[nx][ny] and arr[nx][ny] == 0:
                check[nx][ny] = 1
                num += 1
                q.append((nx, ny))

check = [[0] * n for _ in range(n)]

num = 0
for i in range(k):
    r, c = map(int, input().split())
    q = deque()
    if arr[r-1][c-1] == 0 and not check[r-1][c-1]:
        num += 1
        check[r-1][c-1] = 1
        q.append((r-1, c-1))

    BFS()

if n == 1:
    if arr[0][0] == 1:
        print(0)
    else:
        print(1)
else:
    print(num)