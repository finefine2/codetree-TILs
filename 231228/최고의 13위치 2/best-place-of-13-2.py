N = int(input()) 
board = [list(map(int,input().split())) for _ in range(N)] 

# 두 사각형이 겹치지 않는 경우를 고려해야 함 
# 두 사각형이 겹치는 경우는 i,k 가 동일하고 j와 l차이가 2 이내일 때
ans = 0
for i in range(N): 
    for j in range(N-2): 
        for k in range(N): 
            for l in range(N-2): 
                if i == k and abs(j-l) <= 2: 
                    continue
                ans = max(ans, board[i][j] + board[i][j+1] + board[i][j+2] 
                + board[k][l] + board[k][l+1] + board[k][l+2])

print(ans)