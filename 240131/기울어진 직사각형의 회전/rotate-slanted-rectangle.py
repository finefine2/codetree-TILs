import copy
n = int(input())

arr = []
for i in range(n):
    st = list(map(int, input().split()))
    arr.append(st)

r, c, m1, m2, m3, m4, dir = map(int, input().split())
r -= 1
c -= 1
tmp = copy.deepcopy(arr)

if dir == 0:
    dx = [-1,-1,1,1]
    dy = [1,-1,-1,1]
    M = [m1, m2, m1, m2]
    # 사실상 m1과 m3가 같고, m2랑 m4랑 같으니 이런식으로 하면 된다.

else:
    dx = [1,1,-1,-1]
    dy = [1,-1,-1,1]
    M = [m2, m1, m2, m1]

for i in range(4):
    for j in range(M[i]):
        nx = r + dx[i]
        ny = c + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        tmp[nx][ny] = arr[r][c]
        r, c = nx, ny

ans = copy.deepcopy(tmp)

for i in range(n):
    print(*ans[i])