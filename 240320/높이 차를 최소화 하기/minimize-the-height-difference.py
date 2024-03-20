import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

# 최대를 최소로, 최소를 최대로

check = [[0] * m for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def isin(a, b):
    return 0<=a<n and 0<=b<m

def DFS(x, y, low, high):
    if check[x][y]:
        return
    
    check[x][y] = True
    for dxs, dys in zip(dx, dy):
        nx = x + dxs
        ny = y + dys

        if isin(nx, ny) and arr[nx][ny] >= low and arr[nx][ny] <= high:
            DFS(nx, ny, low, high)

def clear():
    for i in range(n):
            for j in range(m):
                check[i][j] = 0

def find(mid):
    for low in range(1, 501):
        clear()
        
        high = low + mid

        if high >= 501:
            high = 501

        if arr[0][0] >= low and arr[0][0] <= high:
            DFS(0,0,low, high)
        
        if check[n-1][m-1]:
            return True
        # 이렇게 햇는데 check가 방문한 적이 있으면 true 즉 끝 점까지 이동 된 경우!

    return False

left = 0
right = 500
ans = 500

while left <= right:
    mid = (left + right) // 2

    if find(mid):
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1

print(ans)