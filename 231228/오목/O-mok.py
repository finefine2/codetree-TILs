board = [list(map(int,input().split())) for _ in range(19)] 

def in_range(r,c): 
    return 0 <= r < 19 and 0 <= c < 19 

drs,dcs = [1,1,1,-1,-1,-1,0,0], [-1,0,1,-1,0,1,-1,1]

# 모든 좌표 순회 
for i in range(19): 
    for j in range(19): 
        if board[i][j] == 0: 
            continue 
        for dr,dc in zip(drs,dcs): 
            curt = 1 
            cur_r = i 
            cur_c = j 
            while True: 
                nr,nc = cur_r + dr, cur_c + dc
                if not in_range(nr,nc):
                    break 
                if board[nr][nc] != board[i][j]: 
                    break 
                curt += 1 
                cur_r, cur_c = nr,nc
            if curt == 5: 
                print(board[i][j]) 
                print(i + 2 * dr + 1, j + 2 * dc + 1) 
                exit() 
print(0)