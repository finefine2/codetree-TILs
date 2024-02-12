import sys

sys.setrecursionlimit(2500)

n, m = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

def isin(a, b):
    return 0<=a<n and 0<=b<m

def ismove(a, b, k):
    if not isin(a, b):
        return False
    if check[a][b] or arr[a][b] <= k:
        return False
    return True

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def DFS(x, y, k):
    global num
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if ismove(nx, ny, k):
            check[nx][ny] = 1
            num += 1
            DFS(nx, ny, k)
    
Max = -1
for i in range(n):
    for j in range(m):
        if arr[i][j] > Max:
            Max = arr[i][j]

MaxArea = 0
MaxK = 1
for k in range(1, Max + 1):
    area = []
    check = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] > k and not check[i][j]:
                num = 1
                DFS(i, j, k)
                area.append(num)
    if MaxArea < len(area):
        MaxArea = len(area)
        MaxK = k

print(MaxK, MaxArea)