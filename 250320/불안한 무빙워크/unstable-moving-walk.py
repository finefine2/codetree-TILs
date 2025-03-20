N,K = map(int,input().split()) 

board = list(map(int,input().split()))
man = [0] * N 

ans = 0 

while True: 
    ans += 1 
    #[1] 벨트, 로봇회전, [N-1] 로봇 내림 
    board = [board[-1]] + board[:-1] 
    man = [0] + man[:-1] 
    man[N-1] = 0 
    
    # [2] 먼저 올라간 로봇 처리 
    for i in range(N-2,0,-1): 
        if man[i] == 1 and man[i+1] == 0 and board[i+1] > 0: 
            man[i], man[i+1] = 0, 1 
            board[i+1] -=1 
            
    # [3] 0자리 내구도 >0 이면 올림 
    if board[0] > 0: 
        man[0] = 1
        board[0] -= 1 

    # [4] 0인 개수 >= K이면 탈출
    if board.count(0) >= K: 
        break 
print(ans)