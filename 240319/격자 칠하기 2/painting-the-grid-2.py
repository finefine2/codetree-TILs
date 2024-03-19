# from collections import deque

# n = int(input())

# arr = []
# for i in range(n):
#     tmp = list(map(int, input().split()))
#     arr.append(tmp)

# check = [[0] * n for _ in range(n)]

# def isin(a, b):
#     return 0<=a<n and 0<=b<n

# def BFS(i, j, dist):
#     check = [[0] * n for _ in range(n)]

#     q = deque()
#     q.append((i, j))
#     check[i][j] = 1

#     dx = [0,0,1,-1]
#     dy = [1,-1,0,0]

#     cnt = 1
#     while q:
#         x, y = q.popleft()
#         for dir in range(4):
#             nx = x + dx[dir]
#             ny = y + dy[dir]

#             if isin(nx, ny) and not check[nx][ny] and abs(arr[x][y] - arr[nx][ny]) <= dist:
#                 q.append((nx, ny))
#                 cnt += 1
#                 check[nx][ny] = 1
        
#     return cnt

# def find(dist):
#     ans = 0
#     for i in range(n):
#         for j in range(n):
#             if not check[i][j]:
#                 ans = max(ans, BFS(i, j, dist))
#                 # 각각 i, j에 따라서 해줄 때 개수를 구해준다.
#                 if ans >= (n * n + 1) // 2:
#                     return True
#                 # 전체 칸의 수 n**2에 반 이상이 되면은 True
#     return False

# left = 
# right = 1000000
# Min = 1000000

# while left <= right:
#     mid = (left + right) // 2

#     if find(mid):
#         Min = min(Min, mid)
#         right = mid - 1
#     else:
#         left = mid + 1

# print(Min)


import sys

sys.setrecursionlimit(10000)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]
visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def dfs(x, y, d):
    if visited[x][y]:
        return 0

    visited[x][y] = True
    count = 1
    for dx, dy in zip(dxs, dys):
        next_x = x + dx
        next_y = y + dy

        if in_range(next_x, next_y) and (abs(board[next_x][next_y] - board[x][y]) <= d):
            count += dfs(next_x, next_y, d)

    return count

def is_possible(d):
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if dfs(i, j, d) * 2 >= n * n:
                    return True

    return False

left = 0
right = 1000000
ans = 0

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        right = mid - 1
        ans = mid
    else:
        left = mid + 1

print(ans)