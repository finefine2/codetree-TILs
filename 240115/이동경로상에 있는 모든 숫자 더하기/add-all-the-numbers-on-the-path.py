n, t = map(int, input().split())

st = input()

dx = [-1,0,1,0]
dy = [0,-1,0,1]

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

def isin(x, y):
    return 0<=x<n and 0<=y<n

ans = arr[n//2][n//2]
dir = 0
x, y = n//2, n//2

for k in st:
    if k == 'F':
        if isin(x+dx[dir], y+dy[dir]):
            x += dx[dir]
            y += dy[dir]
            ans += arr[x][y]
            # print(arr[x][y])
    elif k == 'L':
        dir = (dir + 1) % 4
    elif k == 'R':
        dir = (dir - 1) % 4

print(ans)