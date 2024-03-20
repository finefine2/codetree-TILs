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



import sys
sys.setrecursionlimit(10000)

MAX_H = 500

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
visited = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def dfs(x, y, lo, hi):
    if visited[x][y]:
        return
    
    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if in_range(nx, ny) and board[nx][ny] >= lo and board[nx][ny] <= hi:
            dfs(nx, ny, lo, hi)

def clear_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

def reachable(d):
    for lo in range(1, MAX_H + 1):
        clear_visited()

        hi = lo + d
        
        if board[0][0] >= lo and board[0][0] <= hi:
            dfs(0, 0, lo, hi)

        if visited[n-1][m-1]:
            return True
    
    return False

lo = 0
hi = MAX_H
ans = MAX_H

while lo <= hi:
    mid = (lo + hi) // 2
    if reachable(mid):
        hi = mid - 1
        ans = min(ans, mid)
    else:
        lo = mid + 1

print(ans)