from collections import deque

m, n = map(int, input().split())

arr = []
for i in range(m):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

color = []
for i in range(m):
    tmp = list(map(int, input().split()))
    color.append(tmp)

color_num = 0
for i in range(m):
    for j in range(n):
        if color[i][j] == 1:
            color_num += 1

def isin(a, b):
    return 0<=a<m and 0<=b<n

def BFS(dist):
    visited = [[False for _ in range(n)] for _ in range(m)]
    q = deque()

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    for i in range(m):
        for j in range(n):
            color_cnt = 0

            if color[i][j] == 1 and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True

                while q:
                    x, y = q.popleft()
                    if color[x][y] == 1:
                        color_cnt += 1
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]

                        if isin(nx, ny) and not visited[nx][ny] and abs(arr[x][y] - arr[nx][ny]) <= dist:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            # if color[nx][ny] == 1:
                            #     color_cnt += 1

                if color_cnt == color_num:
                    return True
    return False




left = 0
right = 1000000000
Min = 1000000000

while left <= right:
    mid = (left + right) // 2

    if BFS(mid):
        Min = min(Min, mid)
        right = mid - 1
    else:
        left = mid + 1


print(Min)