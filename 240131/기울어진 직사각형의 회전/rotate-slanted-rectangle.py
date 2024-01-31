import copy
n = int(input())

arr = []
for i in range(n):
    st = list(map(int, input().split()))
    arr.append(st)

r, c, m1, m2, m3, m4, dir = map(int, input().split())

def cal(r, c, m11, m22, d):
    # tmp = copy.deepcopy(arr)

    # if d == 0:
    #     dx = [-1,-1,1,1]
    #     dy = [1,-1,-1,1]
    #     M = [m11, m22, m11, m22]
    #     # 사실상 m1과 m3가 같고, m2랑 m4랑 같으니 이런식으로 하면 된다.

    # else:
    #     dx = [-1,-1,1,1]
    #     dy = [1,-1,-1,1]
    #     # dx = [1,1,-1,-1]
    #     # dy = [1,-1,-1,1]
    #     M = [m22, m11, m22, m11]


    # for i in range(4):
    #     for j in range(M[i]):
    #         nx = r + dx[i]
    #         ny = c + dy[i]

    #         tmp[nx][ny] = arr[r][c]
    #         r, c = nx, ny
        
    # return tmp
    tmp = copy.deepcopy(arr)

    if d == 0:
        dx, dy=[-1, -1, 1, 1], [1, -1, -1, 1]
        M = [m11, m22, m11, m22]
    else:
        dx, dy=[-1, -1, 1, 1], [-1, 1, 1, -1]
        M = [m22, m11, m22, m11]

    for i in range(4):
        for j in range(M[i]):
            nr, nc = r+dx[i], c+dy[i]
            tmp[nr][nc] = arr[r][c]
            r, c = nr, nc
    return tmp

ans = copy.deepcopy(cal(r-1, c-1, m1, m2, dir))

for i in range(n):
    print(*ans[i])