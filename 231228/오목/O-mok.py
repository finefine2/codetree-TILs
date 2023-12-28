board = [list(map(int,input().split())) for _ in range(19)] 

for i in range(len(board)-4): 
    for j in range(len(board[0])-4):
        if board[i][j] != 0:  
            if board[i][j] == board[i+1][j] and board[i+1][j] == board[i+2][j] and board[i+2][j] == board[i+3][j] and board[i+3][j] == board[i+4][j]: 
                print(board[i][j])
                print(i+3, j+1)
                break 
            elif board[i][j] == board[i][j+1] and board[i][j+1] == board[i][j+2] and board[i][j+2] == board[i][j+3] and board[i][j+3] == board[i][j+4]: 
                print(board[i][j])
                print(i+1, j+3)
                break 
            elif board[i][j] == board[i+1][j+1] and board[i+1][j+1] == board[i+2][j+2] and board[i+2][j+2] == board[i+3][j+3] and board[i+3][j+3] == board[i+4][j+4]:
                print(board[i][j]) 
                print(i+3, j+3) 
                break