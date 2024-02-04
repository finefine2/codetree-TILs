n, m = map(int, input().split())

def isin(a, b):
    return 0 <= a < n and 0 <= b < n

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

def now_pos(next_num):
    for i in range(n):
        for j in range(n):
            for num in arr[i][j]:
                if num == next_num:
                    return (i, j)

def next_now(now):
    x, y = now
    Max = -1
    Maxpos = (-1, -1)

    for xx, yy in zip(dx, dy):
        nx = x + xx
        ny = y + yy
        if isin(nx, ny):
            for num in arr[nx][ny]:
                if num > Max:
                    Max = num
                    Maxpos = (nx, ny)
    return Maxpos

def move_position(now, next_position, next_num):
    (x, y) = now
    (nx, ny) = next_position

    check = False
    for num in arr[x][y]:
        if num == next_num:
            check = True
        # arr[x][y]가 다음 num일 경우 True로 한다.

        if check:
            arr[nx][ny].append(num)
        # 다음일 경우 arr[nx][ny]에 num을 append 해준다.
    
    # arr[x][y] 안의 제일 끝부분이 next_num이 아닐 경우 pop해준다.
    while arr[x][y][-1] != next_num:
        arr[x][y].pop()
    arr[x][y].pop()
    # 마지막에 한번 더 해준다.

arr = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    tmp = list(map(int, input().split()))
    for j, num in enumerate(tmp):
        arr[i][j].append(num)
        # i, j는 인덱스고 arr[i][j]에 num 값들을 다 넣어준다.

moves = list(map(int, input().split()))

for move_num in moves:
    now = now_pos(move_num)
    Maxpos = next_now(now)
    # 현재의 위치를 nowfㅗ 받고 여기서 다음으로 넘어가서 제일 큰 Maxpos를 찾는다.
    if Maxpos != (-1, -1):
        move_position(now, Maxpos, move_num)
        # 이렇게 받은 현재와 제일 큰 값, 그리고 움직여야 하는 숫자를 가지고 움직인다.

for i in range(n):
    for j in range(n):
        if not arr[i][j]:
            print("None", end=" ")
        else:
            for num in arr[i][j][::-1]:
                print(num, end=" ")
        print()
# 가장 위에 있는 숫자부터 순서대로 출력해야 하므로 이런 식으로 해준다.