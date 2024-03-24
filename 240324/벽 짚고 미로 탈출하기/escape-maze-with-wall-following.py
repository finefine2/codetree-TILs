N = int(input())
start_r, start_c =  map(int, input().split())

board = [list(input())for _ in range(N)]

dr = [0,-1,0,1]
dc = [1,0,-1,0]

start_r -= 1
start_c -= 1 
fr,fc = start_r, start_c 

ans = -1
def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

dir = 0
t = 0
while in_range(start_r, start_c):
    nr,nc = start_r + dr[dir], start_c + dc[dir] 
    if in_range(nr,nc):
        # 만약 이동하는 거리에 #가 있을 경우 방향 바꾸기
        if board[nr][nc] == '#':
            dir = (dir + 1) % 4

        # 이동이 가능할 때
        # 벽의 좌표를 체크 
        elif in_range(nr + dr[(dir + 3) % 4], nc + dc[(dir + 3) % 4]):
            # 이동을 하고 시간을 늘리고 dir도 돌려준다.
            start_r, start_c = nr,nc 
            t += 1
            ndir = (dir + 3) % 4

            # 해당 방향 오른쪽에 벽이 존재하지 않는 경우
            if board[nr + dr[ndir]][nc + dc[ndir]] == '.':
                dir = ndir
                start_r, start_c = start_r + dr[dir], start_c + dc[dir]
                t += 1
        else:
            t -= 1
            nr = N

    # 앞이 칸 밖이라면 탈출한다.
    else:
        start_r,start_c = nr, nc
        t += 1
    
    # 만약 처음의 방향과 위치도 같을 경우 불가능하므로 time을 -1로 하고 break
    if dir == 0 and start_r == fr and start_c == fc:
        t = -1
        break
    
print(t)