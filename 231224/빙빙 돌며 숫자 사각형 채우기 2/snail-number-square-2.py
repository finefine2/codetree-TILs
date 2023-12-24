N, M = map(int,input().split()) 

board = [[0] * M for _ in range(N)] 
r,c = 0,0 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < M 

drs, dcs = [1,0,-1,0], [0,1,0,-1]

dir_num = 0 

board[r][c] = 1
# N * M번 진행 
for i in range(2, N * M + 1): 
    # 현재 방향을 기준으로 다음 위치 값을 계산 
    nr, nc = r + drs[dir_num], c + dcs[dir_num]
    # 더 이상 진행할 수 없다면 시계방향으로 회전 
    if not in_range(nr,nc) or board[nr][nc] != 0:
        dir_num = (dir_num + 1) % 4 
    # 다음 위치로 이동한 다음 배열에 값을 입력 
    r,c = r + drs[dir_num], c+ dcs[dir_num] 
    board[r][c] = i 
# 출력 
for i in range(N): 
    for j in range(M): 
        print(board[i][j], end = " ")
    print()