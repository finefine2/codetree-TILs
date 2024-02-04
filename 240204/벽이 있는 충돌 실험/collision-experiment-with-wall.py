t = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]
# R L D U

for _ in range(t):
    n, m = map(int, input().split())

    def isin(a, b):
        return 0<=a<n and 0<=b<n

    arr = [[0] * n for _ in range(n)]
    for i in range(m):
        x, y, d = map(str, input().split())
        x = int(x)
        y = int(y)
        arr[x-1][y-1] = d

    dir = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for _ in range(1000):
        arr_tmp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if arr[i][j] != 0:
                    dirnum = dir[arr[i][j]]
                    nx = i + dx[dirnum]
                    ny = j + dy[dirnum]

                    #  안에 있을 때 옮겨진 nx,ny가 0이 아닐 경우 1로 바꾸어 준다. 충돌한다는 의미
                    if isin(nx, ny):
                        if arr_tmp[nx][ny] != 0:
                            arr_tmp[nx][ny] = 1
                            # 0일 경우에는 그냥 원래의 값을 넣어준다. (arr[i][j])
                        else:
                            arr_tmp[nx][ny] = arr[i][j]
                    # 범위 밖인 경우에
                    else:    # 0이 아닐 때에는 1로 바꾼다.
                        if arr_tmp[i][j] != 0:
                            arr_tmp[i][j] = 1
                        # 0일 경우에는 방향을 바꾼다. 반대로
                        else:
                            if arr[i][j] == 'U':
                                arr_tmp[i][j] = 'D'
                            elif arr[i][j] == 'D':
                                arr_tmp[i][j] = 'U'
                            elif arr[i][j] == 'L':
                                arr_tmp[i][j] = 'R'
                            else:
                                arr_tmp[i][j] = 'L'

        for i in range(n):
            for j in range(n):
                if arr_tmp[i][j] == 1:   # 만약에 충돌하는 경우 arr을 0으로 만든다.
                    arr[i][j] = 0
                else:                    # 아닐 경우 arr에 arr_tmp의 값을 넣어준다.
                    arr[i][j] = arr_tmp[i][j]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                cnt += 1

print(cnt)