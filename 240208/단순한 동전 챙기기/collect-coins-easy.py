import sys
n = int(input())

arr = []
for i in range(n):
    tmp = list(input())
    arr.append(tmp)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

coin = []
select = []
ans = sys.maxsize

x, y = 0, 0
endx, endy = 0,0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'S':
            x, y = i, j
        elif arr[i][j] == 'E':
            endx, endy = i, j

def dist(a, b, c, d):
    return abs(a - c) + abs(b - d)

def move_cal():
    move_num = dist(x, y, select[0][0], select[0][1])
    # 처음에는 시작과 고른 번호 중에 다음으로 가는 길이를 넣어준다.

    for i in range(2):
        move_num += dist(select[i][0], select[i][1], select[i+1][0], select[i+1][1])
    # 그 다음에는 0 - 1, 1 - 2 의 거리를 더해준다.

    move_num += dist(select[2][0], select[2][1], endx, endy)
    # 그 다음 3번째와 마지막 end의 길이를 구해서 더해준다.

    return move_num

def move_min(now, num):
    global ans

    if num == 3:
        ans = min(ans, move_cal())
        return
    
    if now == len(coin):
        return
    # now가 coin의 길이가 같으면 리턴한다.
    
    move_min(now + 1, num)

    select.append(coin[now])
    move_min(now + 1, num + 1)
    select.pop()

for k in range(1, 10):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == str(k):
                coin.append((i, j))
# 각 숫자마다 코인을 넣어줌 번호 순서대로 들어가게

move_min(0, 0)

if ans == sys.maxsize:
    ans = -1

print(ans)    



# def move(x, y, num, t):
#     if x == endx and y == endy:
#         return t

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<=nx<n and 0<=ny<n and (num < int(arr[nx][ny] if arr[nx][ny] != '.' else 0) or arr[nx][ny] == '.'):
#             x, y = nx, ny
#             if arr[nx][ny] != '.':
#                 move(nx, ny, int(arr[nx][ny]), t + 1)
#             else:
#                 move(nx, ny, num, t + 1)

# print(move(x, y, 0, 0))