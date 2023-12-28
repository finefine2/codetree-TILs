N = int(input()) 
board = [list(map(int,input().split())) for _ in range(N)] 

ans = 0
for i in range(N): 
    for j in range(N-2): 
        for k in range(N): 
            for l in range(j+3,N-2): 
                ans = max(ans, board[i][j] + board[i][j+1] + board[i][j+2] 
                + board[k][l] + board[k][l+1] + board[k][l+2])

print(ans)