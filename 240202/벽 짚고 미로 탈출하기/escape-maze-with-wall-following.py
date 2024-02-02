n = int(input())

x, y = map(int, input().split())

arr = []
for i in range(n):
    tmp = input()
    arr.append(tmp)

dx = [0,-1,0,1]
dy = [1,0,-1,0]

x -= 1
y -= 1

fx, fy = x, y

ans = -1
def isin(x, y):
    return 0<=x<n and 0<=y<n

dir = 0
t = 0
while isin(x, y):
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    if isin(nx, ny):
        # 만약 이동하는 거리에 #가 있을 경우 방향 바꾸기
        if arr[nx][ny] == '#':
            dir = (dir + 1) % 4

        # 이동이 가능할 때
        elif isin(nx + dx[(dir + 3) % 4], ny + dy[(dir + 3) % 4]):
            # 이동을 하고 시간을 늘리고 dir도 돌려준다.
            x = nx
            y = ny
            t += 1
            ndir = (dir + 3) % 4

            # 해당 방향 오른쪽에 벽이 존재하지 않는 경우
            if arr[nx + dx[ndir]][ny + dy[ndir]] == '.':
                dir = ndir
                x = x + dx[dir]
                y = y + dy[dir]
                t += 1
        else:
            t -= 1
            nx = n

    # 앞이 칸 밖이라면 탈출한다.
    else:
        x, y = nx, ny
        t += 1
    
    # 만약 처음의 방향과 위치도 같을 경우 불가능하므로 time을 -1로 하고 break
    if dir == 0 and x == fx and y == fy:
        t = -1
        break
    
print(t)