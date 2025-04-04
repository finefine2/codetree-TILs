R,C,K = map(int,input().split()) 
unit = [list(map(int,input().split())) for _ in range(K)] 
board = [[1] + [0] * C + [1] for _ in range(R+3)] + [[1] * (C+2)] 
exit_set = set() 

drs,dcs = [-1,0,1,0],[0,1,0,-1] 

from collections import deque 
def bfs(sr,sc): 
    q = deque() 
    v = [[0] * (C+2) for _ in range(R+4)] 
    mx_i = 0 # -2해서 리턴 

    q.append((sr,sc)) 
    v[sr][sc]=1 

    while q: 
        cr,cc = q.popleft() 
        mx_i = max(mx_i,cr) 

        # 4방향, 미방문, 조건: 같은 값이거나 내가 출구 - 상대가 골렘 
        for dr,dc in zip(drs,dcs): 
            nr,nc = cr + dr, cc + dc 
            if v[nr][nc] == 0 and (board[nr][nc] == board[cr][cc] or ((cr,cc) in exit_set and board[nr][nc]>1)):
                q.append((nr,nc)) 
                v[nr][nc] = 1 
    return mx_i-2 

ans = 0 
num = 2 # 골렘 표기형 
for cc,dr in unit: 
    cr = 1 
    # 남쪽으로 최대한 이동 
    while True: 
        if board[cr+1][cc-1] + board[cr+2][cc] + board[cr+1][cc+1] == 0: 
            cr += 1 
        # 서쪽으로 회전하면서 이동 
        elif board[cr-1][cc-1] + board[cr][cc-2] + board[cr+1][cc-1] + board[cr+1][cc-2] + board[cr+2][cc-1] == 0: 
            cr += 1
            cc -= 1 
            dr = (dr-1) % 4 
        elif board[cr-1][cc+1] + board[cr][cc+2] + board[cr+1][cc+1] + board[cr+1][cc+2] + board[cr+2][cc+1] == 0: 
            cr += 1 
            cc += 1 
            dr = (dr+1) % 4 
        else: 
            break 
    if cr < 4: 
        board = [[1]+[0]*C+[1] for _ in range(R+3)] +[[1] * (C+2)] 
        exit_set = set() 
        num = 2 
    else: 
        board[cr+1][cc]=board[cr-1][cc] = num
        board[cr][cc-1:cc+2] = [num] * 3 
        num += 1 

        exit_set.add((cr+drs[dr],cc+dcs[dr])) 
        ans += bfs(cr,cc) 
print(ans) 