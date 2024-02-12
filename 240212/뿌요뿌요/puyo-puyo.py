n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)


def isin(a, b):
    return 0<=a<n and 0<=b<n
def ismove(a, b, k):
    if not isin(a, b):
        return False
    if check[a][b] or arr[a][b] != k:
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

block = []
ans = 0
for k in range(1, 101):
    check = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                num = 0
                DFS(i, j, k)
                if num >= 2:
                    block.append(num)
                if num >= 4:
                    ans += 1
    

if len(block) == 0:
    print(ans, 0)
else:
    print(ans, max(block))