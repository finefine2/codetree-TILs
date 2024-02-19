N = int(input()) 

board = [list(map(int,input().split())) for _ in range(N)] 

ans = -1 

for i in range(N-2): 
    for j in range(N-2): 
        cnt = 0 
        for k in range(3): 
            for l in range(3): 
                if board[i+k][j+l] == 1: 
                    cnt += 1 
        if cnt > ans: 
            ans = cnt 
print(ans)