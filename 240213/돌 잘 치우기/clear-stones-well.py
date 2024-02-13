from collections import deque
from itertools import combinations
from copy import deepcopy


n, k, m = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

rock = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            rock.append((i, j))

rock_remove = combinations(rock, m)


def isin(a, b):
    return 0<=a<n and 0<=b<n

def BFS(bfs_arr):
    global num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if isin(nx, ny) and not check[nx][ny] and bfs_arr[nx][ny] == 0:
                check[nx][ny] = 1
                num += 1
                q.append((nx, ny))

start = []
for i in range(k):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    start.append((r, c))

ans = 0
for stone in rock_remove:
    remove_arr = deepcopy(arr)
    check = [[0] * n for _ in range(n)]
    for stone_x, stone_y in stone:
        remove_arr[stone_x][stone_y] = 0
    
    for i in range(n):
        for j in range(n):
            num = 0
            q = deque()
            if not check[i][j] and remove_arr[i][j] == 0:
                check[i][j] = 0
                q.append((i, j))
                BFS(remove_arr)
                ans = max(ans, num)

print(ans)