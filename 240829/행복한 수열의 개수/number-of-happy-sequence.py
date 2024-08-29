N,M = tuple(map(int,input().split())) 

board = [list(map(int,input().split())) for _ in range(N)] 

row_list = [] 

for i in range(N): 
    row_list.append(board[i]) 

for j in range(N): 
    mid = [] * N 
    for i in range(N): 
        mid.append(board[i][j]) 
    row_list.append(mid) 

def check_happy(arr): 
    cnt, max_cnt = 1,1 

    for i in range(0,N-1): 
        if arr[i] == arr[i+1]: 
            cnt += 1 
        else: 
            cnt = 1
        max_cnt = max(max_cnt,cnt) 

    return max_cnt >= M 
ans = 0
for r in row_list:
    if check_happy(r): 
        ans += 1 
print(ans)