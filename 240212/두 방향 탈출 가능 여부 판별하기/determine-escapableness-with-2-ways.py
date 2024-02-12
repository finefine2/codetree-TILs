n, m = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

check = [[0] * m for _ in range(n)]
dx = [0,1]
dy = [1,0]

def isin(a, b):
    return 0<=a<n and 0<b<m

def ismove(a, b):
    if not isin(a, b):
        return False
    if check[a][b] or arr[a][b] == 1:
        return False
    
    return True
    
ans = 0
check[0][0] = 1

def move(x, y):
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if ismove(nx, ny):
            if nx == n-1 and ny == m-1:
                ans = 1
                return
            check[nx][ny] = 1
            move(nx, ny)
            

move(0, 0)
print(ans)