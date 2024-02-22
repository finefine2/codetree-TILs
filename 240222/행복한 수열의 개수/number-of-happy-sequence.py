N,M = map(int,input().split()) 
board = [list(map(int,input().split())) for _ in range(N)] 
seq = [0 for _ in range(N)] 

def is_happy(): 
    consec_conut, max_cnt = 1,1 
    for i in range(1,N): 
        if seq[i-1] == seq[i]: 
            consec_conut += 1
        else: 
            consec_conut = 1 
        max_cnt = max(max_cnt,consec_conut) 
    return max_cnt >= M 

num = 0 
for i in range(N): 
    seq = board[i][:]
    if is_happy(): 
        num += 1 
for j in range(N): 
    for i in range(N): 
        seq[i] = board[i][j] 
    if is_happy(): 
        num += 1 
print(num)