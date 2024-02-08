n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

dir = []
for i in range(n):
    tmp = list(map(int, input().split()))
    dir.append(tmp)

r, c = map(int, input().split())

r -= 1
c -= 1
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
ans = 0

def move(x, y, num):
    global ans

    for i in range(1, n):
        nx = x + i * dx[dir[x][y] - 1]
        ny = y + i * dy[dir[x][y] - 1]

        # arr가 더 크면 ans를 갱신하고 move해본다. num을 증가시키고
        if 0<=nx<n and 0<=ny<n and arr[x][y] < arr[nx][ny]:
            ans = max(ans, num + 1)
            move(nx, ny, num + 1)
        else:
            continue

move(r, c, 0)
print(ans)