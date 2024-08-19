N,M = tuple(map(int,input().split()))
r,c,d = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# N E S W
# 0 1 2 3
drs,dcs = [-1,0,1,0], [0,1,0,-1]

# step1.현재를 기준으로 왼쪽 좌회전
def rotate():
    global d
    d -= 1
    if d == -1:
        d = 3
cnt = 1
turn_time = 0
# 후진이 불가능할 때까지 움직임을 강제로 진행시키는 느낌
while True:
    rotate()
    nr, nc = r + drs[d], c + dcs[d]
    # 아직 안 가봤거나 빈 칸이면 이동 가능
    if not visited[nr][nc] and board[nr][nc] == 0:
        visited[nr][nc] = True
        r,c = nr, nc
        cnt += 1

    # 가봤거나 바다라면 1단계로 백
    else:
        turn_time += 1

    if turn_time == 4:
        nr,nc = r - drs[d], c- dcs[d]

        if board[nr][nc] == 1:
            break
        else:
            turn_time = 0
            continue
print(cnt)
