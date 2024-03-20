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

# from collections import deque

# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]

# # 주어진 높이 범위 내에서 이동이 가능한지 확인하는 BFS 함수
# def bfs(min_height, max_height):
#     if arr[0][0] < min_height or arr[0][0] > max_height:
#         return False
#     visited = [[False]*m for _ in range(n)]
#     queue = deque([(0, 0)])
#     visited[0][0] = True
#     while queue:
#         x, y = queue.popleft()
#         if x == n-1 and y == m-1:
#             return True
#         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
#                 if min_height <= arr[nx][ny] <= max_height:
#                     visited[nx][ny] = True
#                     queue.append((nx, ny))
#     return False

# # 이진 탐색으로 최소 높이 차를 찾는 과정
# def binary_search():
#     ans = float('inf')
#     for min_height in range(1, 501):
#         left, right = 0, 500 - min_height
#         while left <= right:
#             mid = (left + right) // 2
#             if bfs(min_height, min_height + mid):
#                 ans = min(ans, mid)
#                 right = mid - 1
#             else:
#                 left = mid + 1
#     return ans

# print(binary_search())


import sys

# 재귀함수의 깊이 제한을 풀어줍니다.
sys.setrecursionlimit(10000)

MAX_H = 500

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

dys = [-1, 0, 1, 0]
dxs = [0, -1, 0, 1]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

# dfs를 이용해 이동합니다. visited 배열로 끝까지 도달할 수 있는지 확인합니다.
def dfs(x, y, lo, hi):
    if visited[x][y]:
        return
    
    visited[x][y] = True
    for (dx, dy) in zip(dxs, dys):
        next_x = x + dx
        next_y = y + dy
        if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m \
        and board[next_x][next_y] >= lo and board[next_x][next_y] <= hi:
            dfs(next_x, next_y, lo, hi)

# visited 배열을 초기화합니다.
def clear_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

# d 이하로 최대 높이와 최소 높이의 차이가 나는 칸만 갈 수 있을 때,
# 마지막 칸으로 이동할 수 있는지 확인합니다.
def reachable(d):
    # 모든 높이 제한에 대해서, 도달 가능한지 확인합니다.
    for lo in range(1, MAX_H + 1):
        clear_visited()

        hi = lo + d
        # 만약 시작하는 위치의 높이가 lo이상 hi이하라면 dfs로 탐색합니다.
        if board[0][0] >= lo and board[0][0] <= hi:
            dfs(0, 0, lo, hi)
        # 마지막에 도달할 수 있으면 도달 가능합니다.
        if visited[n - 1][m - 1]:
            return True

    return False


lo = 0                     # 답이 될 수 있는 가장 작은 숫자 값을 설정합니다.
hi = MAX_H                 # 답이 될 수 있는 가장 큰 숫자 값을 설정합니다.
ans = MAX_H                # 답을 저장합니다.

while lo <= hi:            # [lo, hi]가 유효한 구간이면 계속 수행합니다.
    mid = (lo + hi) // 2   # 가운데 위치를 선택합니다.
    if reachable(mid):     # 결정문제에 대한 답이 Yes라면
        hi = mid - 1       # 왼쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 right를 바꿔줍니다.
        ans = min(ans, mid)# 답의 후보들 중 최솟값을 계속 갱신해줍니다.
    else:
        lo = mid + 1       # 결정문제에 대한 답이 No라면 right를 바꿔줍니다.

# 정답을 출력합니다.
print(ans)