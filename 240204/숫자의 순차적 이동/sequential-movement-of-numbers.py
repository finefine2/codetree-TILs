n, m = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)


# dx = [-1, -1, -1, 0, 0, 1, 1, 1]
# dy = [-1, 0, 1, -1, 1, -1, 0, 1]
dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]


def isin(a, b):
    return 0<=a<n and 0<=b<n

def find_num(num):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == num:
                return i, j


for _ in range(m):
    for num in range(1, n*n+1):
        x, y = find_num(num)
        Maxnum = 0
        Maxx = 0
        Maxy = 0
        for dir in range(8):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if isin(nx, ny) and Maxnum < arr[nx][ny]:
                Maxnum = arr[nx][ny]
                Maxx, Maxy = nx, ny
        
        # print(arr[Maxx][Maxy])
        arr[x][y], arr[Maxx][Maxy] = arr[Maxx][Maxy], arr[x][y]




for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()