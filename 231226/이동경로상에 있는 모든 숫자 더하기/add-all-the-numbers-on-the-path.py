N,T = map(int,input().split()) 
r, c = N // 2, N // 2 

s_in = input() 
board = [list(map(int,input().split())) for _ in range(N)] 
visited = [[False] * N for _ in range(N)] 

dir_num = 0 
def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

drs, dcs = [-1,0,1,0],[0,1,0,-1] 
ans = board[r][c] 
visited[r][c] = True 
for s in s_in: 
    if s == "F": 
        nr,nc = r + drs[dir_num], c + dcs[dir_num]
        if not in_range(nr,nc):
            continue
        else: 
            r,c = nr,nc 
            ans += board[r][c]
    elif s == "L": 
        dir_num = (dir_num-1) % 4 
    elif s == "R": 
        dir_num = (dir_num+1) % 4
         
     
print(ans)