R,C,K = tuple(map(int,input().split())) 
units = [list(map(int,input().split())) for _ in range(K)] 
board = [[1] + [0] * C + [1] for _ in range(R+3)] + [[1] * (C+2)] 
exit_set = set() 

drs,dcs = [-1,0,1,0],[0,1,0,-1] 


ans = 0 
num = 2 
from collections import deque 
# 현재 위치에서 출구까지의 최소거리를 계산하기 
def bfs(sr,sc): 
    v = [[0] * (C+2) for _ in range(R+4)] 
    q = deque() 

    q.append((sr,sc)) 
    v[sr][sc] = 1 
    max_r = 0
    while q: 
        cr,cc = q.popleft() 
        max_r = max(max_r,cr) 
        # 4방향, 미방문, 조건: 같은 값이거나 또는 내가 출구이면서 상대방은 골렘 
        for dr,dc in zip(drs,dcs): 
            nr,nc = cr + dr, cc + dc 
            if v[nr][nc] == 0 and (board[nr][nc] == board[cr][cc] or ((cr,cc) in exit_set and board[nr][nc]>1)): 
                q.append((nr,nc)) 
                v[nr][nc] = 1 
    return max_r-2

# 골렘 입력 좌표 /방향에 따라 남쪽이동 및 정령 최대좌표 계산 및 누적 
for cc,dr in units: 
    cr = 1 
    # 남쪽으로 최대한 이동 ( 남 -> 서 -> 동) 
    while True:
        # 남쪽으로 한칸 이도 ㅇ
        if board[cr+1][cc-1] + board[cr+2][cc] + board[cr+1][cc+1] == 0: # 비어있음 
            cr += 1 
        # 서쪽으로 회전하면서 한칸 
        elif board[cr-1][cc-1] + board[cr][cc-2] + board[cr+1][cc-1] + board[cr+1][cc-2] + board[cr+2][cc-1] == 0: 
            cr += 1 
            cc -= 1 
            dr = (dr-1) % 4
        # 동쪽으로 회전하면서 한칸 
        elif board[cr-1][cc+1] + board[cr][cc+2] + board[cr+1][cc+1] + board[cr+1][cc+2] + board[cr+2][cc+1] == 0: 
            cr += 1 
            cc += 1 
            dr = (dr+1) % 4 
        else: 
            break 
    if cr < 4: # 몸이 범위 밖에 있으면 새롭게 보드 갱신 
        board = [[1] + [0]* C + [1] for _ in range(R+3)] + [[1] * (C+2)] 
        exit_set = set() 
        num = 2 
    else: 
        # 그게 아니면 골렘을 표시하고 출구 추가 
        board[cr+1][cc] = num 
        board[cr-1][cc] = num
        board[cr][cc-1] = num
        board[cr][cc] = num
        board[cr][cc+1] = num
        num += 1 

        exit_set.add((cr+drs[dr],cc+dcs[dr]))            
        ans += bfs(cr,cc) 
print(ans)