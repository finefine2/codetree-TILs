from collections import deque 

N,M = tuple(map(int,input().split())) 
board = [[-1] * (N+2)] + [[-1] + list(map(int,input().split())) + [-1] for _ in range(N)] + [[-1] * (N+2)] 
EMPTY = M+1

ans = 0 

def gravity(): 
    for sr in range(1,N): 
        for sc in range(1,N+1): 
            cr,cc = sr,sc 
            while 0<=board[cr][cc]<=M and board[cr+1][cc] == EMPTY: 
                board[cr][cc],board[cr+1][cc] = board[cr+1][cc],board[cr][cc] 
                cr -= 1 
def get_base(group): 
    base_r,base_c = -1, N+1
    for (r,c) in group: 
        if r > base_r or (r==base_r and c < base_c): 
            base_r,base_c = r,c 
    return base_r, base_c
def bfs(): 
    v = [[0] * (N+2) for _ in range(N+2)] 
    tlst = [] 
    max_group = set() 
    drs,dcs = [-1,0,1,0],[0,1,0,-1] 
    for sr in range(1,N+1): 
        for sc in range(1,N+1): 
            if v[sr][sc] == 0 and 0<board[sr][sc]<=M: # 미방문 일반블럭 
                q = deque() 
                group = set() 
                r_cnt = 0 

                q.append((sr,sc)) 
                group.add((sr,sc)) 
                color = board[sr][sc]
                v[sr][sc] = 1 
                while q: 
                    cr,cc = q.popleft() 
                    for dr,dc in zip(drs,dcs): 
                        nr,nc = cr + dr, cc + dc 
                        if v[nr][nc] == 0 and (nr,nc) not in group and (board[nr][nc] == color or board[nr][nc] == 0): 
                            q.append((nr,nc)) 
                            group.add((nr,nc)) 
                            if board[nr][nc] == 0: 
                                r_cnt += 1 
                            else: 
                                v[nr][nc] = 1 
                base_r, base_c = get_base(group) 
                tlst.append((len(group),r_cnt,base_r,base_c,group))
                if len(tlst) > 0: 
                    tlst.sort(key=lambda x:(-x[0],x[1],-x[2],x[3]))
                    max_group = tlst[0][-1] 
    return max_group
while True: 
    bomb_group = bfs() 
    if len(bomb_group) < 2: 
        break 

    ans += len(bomb_group) ** 2 

    for br,bc in bomb_group: 
        board[br][bc] = EMPTY 
    gravity() 
    board = list(map(list,zip(*board)))[::-1] 
    gravity() 
print(ans)