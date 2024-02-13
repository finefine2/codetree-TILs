# 0 : 이동 가능
# 1 : 벽이라 이동 불가
# 2 : 사람이 있음
# 3 : 비를 피할 수 있는 공간

from collections import deque

n, h, m = map(int, input().split())

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

            if isin(nx, ny) and not check[nx][ny] and arr[nx][ny] != 1:
                check[nx][ny] = 1
                ans[nx][ny] = ans[x][y] + 1
                q.append((nx, ny))

ans = [[0] * n for _ in range(n)]
check = [[0] * n for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 3:
            check[i][j] = 1
            q.append((i, j))

BFS()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            if ans[i][j]:
                print(ans[i][j], end = " ")
            else:
                print(-1, end = " ")
        else:
            print(0, end = " ")
    print()

# 사람이 있는 곳에서 시작하는 것이 아니라 답인 3에서 시작해서 사람이 있는 곳을 찾아간다.
# 그리고 사람이 있는 경우에만 움직일 수 있으므로 ans를 출력하면 된다.