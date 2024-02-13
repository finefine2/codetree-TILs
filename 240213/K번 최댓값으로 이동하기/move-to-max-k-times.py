from collections import deque
n, k = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

r, c = map(int, input().split())
tmpr, tmpc = r, c
r -= 1
c -= 1

def isin(a, b):
    return 0<=a<n and 0<=b<n
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS(num):
    global Max, Maxi, Maxj
    global flag
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if isin(nx, ny) and not check[nx][ny] and arr[nx][ny] < num:
                check[nx][ny] = 1
                flag = True
                if arr[nx][ny] > Max or (arr[nx][ny] == Max and nx < Maxi) or (arr[nx][ny] == Max and nx == Maxi and ny < Maxj):
                    Max = arr[nx][ny]
                    Maxi = nx
                    Maxj = ny
                # if arr[nx][ny] >= Max:
                #     Max = arr[nx][ny]
                #     if Maxi > nx:
                #         Maxi = nx
                #         Maxj = ny
                #     elif Maxi == nx:
                #         if Maxj >= ny:
                #             Maxi = nx
                #             Maxj = ny
                q.append((nx, ny))

    

while k:
    q = deque()
    check = [[0] * (n) for _ in range(n)]
    flag = False
    Max = 0
    Maxi = 101
    Maxj = 101

    if isin(r, c):
        q.append((r, c))
        BFS(arr[r][c])

    if flag:
        r, c = Maxi, Maxj
    else:
        break
    k -= 1

if r == 101 and c == 101:
    print(tmpr, tmpc)
else:
    print(r+1, c+1)