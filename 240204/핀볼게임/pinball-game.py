# 처음에 접근했던 방법 : 처음 시작하는 네 방향들에 대해서 각각 시작 -> 방향이 바뀌면 다르므로 다르게 해야 한다.

n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

def isin(x, y):
    return 0<=x<n and 0<=y<n

# UP -> 1 -> R 
# UP -> 2 -> L 
# DOWN -> 1 -> L 
# DOWN -> 2 -> R  
# LEFT -> 1 -> DOWN 
# LEFT -> 2 -> UP
# RIGHT -> 1 -> UP
# RIGHT -> 2 -> DOWN

dir = {'D': 0, 'L': 1, 'U': 2, 'R': 3}
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
# down right up left

Max = 0
def pinball(startx, starty, d):
    t = 0
    x, y = startx, starty
    dirnum = dir[d]

    while True:
        t += 1
        nx = x + dx[dirnum]
        ny = y + dy[dirnum]

        if isin(nx, ny):
            x, y = nx, ny
            if arr[x][y] == 1:  # 1을 만났을 때 
                if dirnum == 2 or dirnum == 0:   # 위아래일 경우에는
                    dirnum = (dirnum + 1) % 4    # down은 right, up은 left로 바꾼다.
                else:
                    dirnum = (dirnum + 3) % 4    # 좌우일 경우 right는 down, left는 up
            # 이런 식으로 두개의 경우에 이런 규칙을 쓸 수 있다.
            elif arr[x][y] == 2:
                if dirnum == 2 or dirnum == 0:
                    dirnum = (dirnum + 3) % 4
                else:
                    dirnum = (dirnum + 1) % 4
        else:
            break

    return t

for j in range(n):
    t = pinball(-1, j, 'D')
    Max = max(Max, t)
    t = pinball(n, j, 'U')
    Max = max(Max, t)
# 위아래

for i in range(n):
    t = pinball(i, -1, 'R')
    Max = max(Max, t)
    t = pinball(i, n, 'L')
    Max = max(Max, t)
# 좌우

print(Max)


# for j in range(n):
#     t = 0
#     i = 0

#     x = 0
#     y = j
#     while True:
#         if arr[x][y] == 0:
#             nx = x + dx[0]
#             ny = y + dy[0]
#         elif arr[x][y] == 1:
#             nx = x + dx[3]
#             ny = y + dy[3]
#         elif arr[x][y] == 2:
#             nx = x + dx[2]
#             ny = y + dy[2]
        
#         t += 1
#         if isin(nx, ny):
#             x = nx
#             y = ny
#             continue
#         else:
#             break

# # RIGHT
# for j in range(n):
#     t = 0
#     i = 0

#     x = 0
#     y = j
#     while True:
#         if arr[x][y] == 0:
#             nx = x + dx[2]
#             ny = y + dy[2]
#         elif arr[x][y] == 1:
#             nx = x + dx[1]
#             ny = y + dy[1]
#         elif arr[x][y] == 2:
#             nx = x + dx[0]
#             ny = y + dy[0]
        
#         t += 1
#         if isin(nx, ny):
#             x = nx
#             y = ny
#             continue
#         else:
#             break

# # LEFT
# for j in range(n):
#     t = 0
#     i = 0

#     x = 0
#     y = j
#     while True:
#         if arr[x][y] == 0:
#             nx = x + dx[0]
#             ny = y + dy[0]
#         elif arr[x][y] == 1:
#             nx = x + dx[3]
#             ny = y + dy[3]
#         elif arr[x][y] == 2:
#             nx = x + dx[2]
#             ny = y + dy[2]
        
#         t += 1
#         if isin(nx, ny):
#             x = nx
#             y = ny
#             continue
#         else:
#             break

# # UP
# for j in range(n):
#     t = 0
#     i = 0

#     x = 0
#     y = j
#     while True:
#         if arr[x][y] == 0:
#             nx = x + dx[0]
#             ny = y + dy[0]
#         elif arr[x][y] == 1:
#             nx = x + dx[3]
#             ny = y + dy[3]
#         elif arr[x][y] == 2:
#             nx = x + dx[2]
#             ny = y + dy[2]
        
#         t += 1
#         if isin(nx, ny):
#             x = nx
#             y = ny
#             continue
#         else:
#             break
    
#     Max = max(Max, t)