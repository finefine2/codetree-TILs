from itertools import combinations
from collections import deque
import sys

n, k = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r1 -= 1
r2 -= 1
c1 -= 1
c2 -= 1

wall = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            wall.append((i, j))

remove_wall = list(combinations(wall, k))

def isin(a, b):
    return 0<=a<n and 0<=b<n

dx = [0,0,1,-1]
dy = [1,-1,0,0]

Min = sys.maxsize
def BFS():
    global Min
    q = deque()
    q.append((r1, c1))
    check = [[0] * n for _ in range(n)]
    check[r1][c1] = 0
    

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == r2 and ny == c2:
                Min = min(Min, check[x][y] + 1)
                return

            if isin(nx, ny) and not check[nx][ny] and arr[nx][ny] != 1:
                check[nx][ny] = check[x][y] + 1
                q.append((nx, ny))


for i in range(len(remove_wall)):
    for j in range(k):
        arr[remove_wall[i][j][0]][remove_wall[i][j][1]] = 0
    
    BFS()

    for j in range(k):
        arr[remove_wall[i][j][0]][remove_wall[i][j][1]] = 1
    
if Min == sys.maxsize:
    print(-1)
else:
    print(Min)






# 1번 : combination으로 벽들을 모두 조합해 만든다 -> 시간 초과 및 좋은 풀이가 아닐 듯
# 이게 올바른 풀이인듯하다..... 이게 최우선인가