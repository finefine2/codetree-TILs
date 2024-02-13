from collections import deque
n = int(input())

r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def isin(a, b):
    return 0<=a<n and 0<=b<n

check = [[0] * n for _ in range(n)]
knight = [[-1] * n for _ in range(n)]

def BFS():
    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if isin(nx, ny) and not check[nx][ny]:
                knight[nx][ny] = knight[x][y] + 1
                check[nx][ny] = 1
                q.append((nx, ny))

q = deque()
r1 -= 1
r2 -= 1
c1 -= 1
c2 -= 1

knight[r1][c1] = 0
q.append((r1, c1))

BFS()

if knight[r2][c2] == -1:
    print(-1)
else:
    print(knight[r2][c2])

# if r1 == r2 and c1 == c2:
#     print(0)

# print(r2, c2)
# if knight[r2][c2] == -1:
#     print(-1)
# else:
#     print(knight[r2][c2])