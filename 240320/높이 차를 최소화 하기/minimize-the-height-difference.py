# import sys
# sys.setrecursionlimit(10000)

# n, m = map(int, input().split())

# arr = []
# for i in range(n):
#     tmp = list(map(int, input().split()))
#     arr.append(tmp)

# # 최대를 최소로, 최소를 최대로

# check = [[0] * m for _ in range(n)]
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]

# def isin(a, b):
#     return 0<=a<n and 0<=b<m

# def DFS(x, y, low, high):
#     if check[x][y]:
#         return
    
#     check[x][y] = True
#     for dxs, dys in zip(dx, dy):
#         nx = x + dxs
#         ny = y + dys

#         if isin(nx, ny) and arr[nx][ny] >= low and arr[nx][ny] <= high:
#             DFS(nx, ny, low, high)

# def clear():
#     for i in range(n):
#             for j in range(m):
#                 check[i][j] = 0

# def find(mid):
#     for low in range(1, 501):
#         clear()
        
#         high = low + mid

#         if high >= 501:
#             high = 501

#         if arr[0][0] >= low and arr[0][0] <= high:
#             DFS(0,0,low, high)
        
#         if check[n-1][m-1]:
#             return True
#         # 이렇게 햇는데 check가 방문한 적이 있으면 true 즉 끝 점까지 이동 된 경우!

#     return False

# left = 0
# right = 500
# ans = 500

# while left <= right:
#     mid = (left + right) // 2

#     if find(mid):
#         ans = min(ans, mid)
#         right = mid - 1
#     else:
#         left = mid + 1

# print(ans)

from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def is_valid(x, y, min_height, max_height):
    return 0 <= x < n and 0 <= y < m and min_height <= grid[x][y] <= max_height

def bfs(min_diff):
    for offset in range(500 - min_diff + 1):
        min_height = max(1, grid[0][0] - offset)
        max_height = min_height + min_diff
        if not is_valid(0, 0, min_height, max_height):
            continue
        visited = [[False] * m for _ in range(n)]
        queue = deque([(0, 0)])
        visited[0][0] = True
        while queue:
            x, y = queue.popleft()
            if x == n-1 and y == m-1:
                return True
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, min_height, max_height) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return False

left, right = 0, 499
answer = 500

while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)