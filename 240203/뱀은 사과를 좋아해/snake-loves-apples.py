n, m, k = map(int, input().split())

arr = [[0] * n for _ in range(n)]
pos = []
for i in range(m):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 8
    pos.append((x-1, y-1))
    # 사과가 있을때 8을 넣는다.

# 4는 뱀의 머리
arr[0][0] = 4
snake = [[0, 0]]
# 8 : apple, 4 : head, 1 : tail

change = []
for i in range(k):
    d, p = map(str, input().split())
    change.append((d, p))

def isin(a, b):
    return 0<=a<n and 0<=b<n

dir = {'U': 0, 'D': 1, 'R': 2, 'L': 3}
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
t = 0
x, y = 0,0
# 순서대로 위 아래 오른쪽 왼쪽

for k in change:
    
    end = False
    for _ in range(int(k[1])):
        t += 1
        nx, ny = snake[0][0] + dx[dir[k[0]]], snake[0][1] + dy[dir[k[0]]]
        # 움직인 좌표가 안에 있을 경우에
        if isin(nx, ny):
            # 그리고 거기에 사과가 있을 경우
            if arr[nx][ny] == 8:
                # 그 좌표를 머리로 바꾸고 원래의 머리 자리를 head로 한다.
                arr[nx][ny] = 4
                arr[snake[0][0]][snake[0][1]] = 1
                snake = [[nx, ny]] + snake
                # 새로운 좌표에다가 snake를 더함 (nx, ny)가 제일 앞
            elif arr[nx][ny] == 1 and not (nx == snake[-1][0] and ny == snake[-1][1]):
                end = True
                break
            # 사과가 아니고 움직인 좌표가 몸통인데 그게 제일 마지막 꼬리라서 안부딪치는게 아닐 경우 끝
            else:  # 그냥 사과가 없고 부딪치지 않는 경우
                arr[nx][ny] = 4
                arr[snake[0][0]][snake[0][1]] = 0
                # 머리를 새로운 위치로 놓고 원래의 머리 위치에 0을 넣어준다.

                # 그런데 만약 원래의 크기가 2개면 몸통이 있으므로 
                if len(snake) > 1:
                    arr[snake[0][0]][snake[0][1]] = 1
                    arr[snake[-1][0]][snake[-1][1]] = 0
                    snake = [[nx, ny]] + snake[:len(snake) - 1]
                    # 나머지 몸통들을 nx,ny 를 넣고 맨 뒤를 제외한 부분을 넣는다.
                else:
                    snake = [[nx, ny]]
                    # 아닐 경우 그냥 nx,ny만 넣고 끝낸다. 왜나면 머리만 있으므로
        else:
            end = True
            break
        # 범위를 벗어날 경우도 나감
    if end:
        break
    # 나가야 하는 경우 끝내준다.

print(t)
            

# ////////////////////////////////