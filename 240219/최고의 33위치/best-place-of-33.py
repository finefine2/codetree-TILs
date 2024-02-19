N = int(input()) 
board = [list(map(int,input().split())) for _ in range(N)] 

def count(row_s, col_s, row_e, col_e): 
    cnt = 0 
    for r in range(row_s,row_e+1): 
        for c in range(col_s,col_e+1): 
            cnt += board[r][c]
    return cnt 

max_num = 0 

for r in range(N): 
    for c in range(N): 
        if r + 2 >= N and c + 2 > = N: 
            continue 
        num = count(r,c,r+2,c+2): 
        max_num = max(max_num,num) 
print(max_num)