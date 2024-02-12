n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

check = [[0] * n for _ in range(n)]

def isin(a, b):
    return 0<=a<n and 0<=b<n

def ismove(a, b):
    if not isin(a, b):
        return False
    if check[a][b] or arr[a][b] == 0:
        return False
    return True

dx = [0,0,1,-1]
dy = [1,-1,0,0]

ans = 0
def DFS(x, y):
    global ans
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if ismove(nx, ny):
            check[nx][ny] = 1
            ans += 1
            DFS(nx, ny)

group = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not check[i][j]:
            check[i][j] = 1
            ans = 1
            DFS(i, j)
            group.append(ans)

print(len(group))
group.sort()
for k in group:
    print(k)