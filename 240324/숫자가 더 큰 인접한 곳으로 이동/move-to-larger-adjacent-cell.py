N, start_r, start_c = map(int,input().split()) 

start_r -= 1
start_c -= 1 
board = [list(map(int,input().split())) for _ in range(N)] 

# 상하좌우 
drs = [-1,1,0,0]
dcs = [0,0,-1,1]

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

ans = []
ans.append(board[start_r][start_c])
def simulate():
    global start_r, start_c
    for dr,dc in zip(drs,dcs): 
        next_r, next_c = start_r + dr, start_c + dc 
        if in_range(next_r,next_c) and board[next_r][next_c] > board[start_r][start_c]: 
            start_r, start_c = next_r, next_c
            return True
    return False

while True: 
    can_go = simulate() 
    if not can_go: 
        break 
    ans.append(board[start_r][start_c])

for a in ans: 
    print(a,end=" ")