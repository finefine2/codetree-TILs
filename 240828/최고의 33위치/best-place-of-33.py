N = int(input()) 
board = [list(map(int,input().split())) for _ in range(N)] 

max_coin = 0 

def get_coin(s_r,s_c): 
    e_r,e_c = s_r+3, s_c+3 
    cnt = 0 
    for i in range(s_r,e_r): 
        for j in range(s_c,e_c): 
            if board[i][j] == 1: 
                cnt += 1 
    return cnt 

for r in range(N-2): 
    for c in range(N-2): 
        max_coin = max(max_coin,get_coin(r,c)) 
print(max_coin)