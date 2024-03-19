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


from sys import stdin
n = int(stdin.readline())
base_2d = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def in_range(i, j):
    return 0<=i<n and 0<=j<n

from collections import deque
def bfs(i, j, D):
    #처음 상태 초기화!
    visited = [[False]*n for _ in range(n)]

    q = deque()
    q.append((i,j))
    visited[i][j] = True

    dx, dy =[0,0,-1,1], [-1,1,0,0]
    
    total = 1

    while q:
        x, y = q.popleft()
        for dxs, dys in zip(dx, dy):
            next_x, next_y = x+dxs, y+dys
            if in_range(next_x, next_y) and not visited[next_x][next_y] and abs(base_2d[x][y]-base_2d[next_x][next_y])<=D: #범위안이고 방문을 아직 안한 경우이며 현재 값보다 D이하로 차이나야함!
                q.append((next_x, next_y))
                total += 1
                visited[next_x][next_y] = True
    return total

def check(D):
    ans = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                ans = max(ans, bfs(i,j,D))
                if ans >= (n*n+1)//2:
                    return True #반올림 처리!
    return False

left = 1
right = 1000000
min_value = 1000000
while left <= right:
    mid = (left+right)//2
    if check(mid):
        min_value = min(min_value, mid)
        right = mid-1
    else:
        left = mid+1
print(min_value)