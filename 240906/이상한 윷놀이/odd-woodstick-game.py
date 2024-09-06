N,K = tuple(map(int,input().split()))
board = [[2]*(N+2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(N)] + [[2]*(N+2)]
players = []
player_info = [[[] for _ in range(N+2)] for _ in range(N+2)]
for k in range(K):
    r,c,d = tuple(map(int,input().split()))
    players.append([r,c,d])
    # 3차원 좌표 - 해당 포지션에 몇명이 있는지 체크하기 위함
    player_info[r][c].append(k)

# 일단 이동을 한다는데
# 내 위에 있는 말들도 다 이동시켜
# 근데 다음 판때기 색깔에 따라서 이동조건이 바뀌는거

# d starts from R L U D
drs,dcs = [0,0,0,-1,1],[0,1,-1,0,0]
ops_d = {1:2,2:1,3:4,4:3}
def simulate():
    for ans in range(1,1001):
        # k 번째 플레이어에 대해서 진행을 해보도록 하자
        for k in range(K):
            r,c,d = players[k]
            nr,nc = r + drs[d], c + dcs[d]
            # 만약 파란색이거나 외부라면
            if board[nr][nc] == 2:
                d = ops_d[d]
                nr,nc = r + drs[d], c + dcs[d]
                players[k][2] = d
                if board[nr][nc] == 2:
                    continue
            # 흰색이거나 빨간색이라면!
            # 현재 속해 있는 좌표에 몇명의 플레이어들이 쌓여있는지
            for idx in range(len(player_info[r][c])):
                # 몇 명을 움직여야하는지도
                # 내 위에 있는 말들까지도 전부 움직여야함
                if player_info[r][c][idx] == k:
                    move_players = player_info[r][c][idx:]
                    if board[nr][nc] == 1:
                        move_players = move_players[::-1]
                    player_info[nr][nc] += move_players
                    if len(player_info[nr][nc]) >= 4:
                        return ans
                    # 제거해줘야지
                    player_info[r][c] = player_info[r][c][:idx]
                    # 그러고 현재 players 보드도 갱신해줘야한다
                    for m in move_players:
                        players[m][0],players[m][1] = nr,nc
                    break 
    else:
        return -1

ans = simulate()
print(ans)