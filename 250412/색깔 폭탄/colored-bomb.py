N,M = map(int,input().split()) 
EMPTY = M+1 

board = [[-1] * (N+2)] + [[-1] + list(map(int,input().split())) + [-1] for _ in range(N)] + [[-1] * (N+2)] 

from collections import deque 
def get_base(group): 
    base_r,base_c = -1,N+1 
    for gr,gc in group: 
        if board[gr][gc] != 0: 
            if gr > base_r or (gr == base_r and gc < base_c): 
                base_r,base_c = gr,gc 
    return base_r,base_c

def bfs(): 
    v = [[0] * (N+2) for _ in range(N+2)] 
    
    mx_group = set() 
    tlst =[] 
    for sr in range(1,N+1): 
        for sc in range(1,N+1): 
            if v[sr][sc] == 0 and 0<board[sr][sc]<=M: 
                q = deque()
                group = set() 

                q.append((sr,sc)) 
                group.add((sr,sc)) 
                v[sr][sc] = 1 
                color = board[sr][sc] 
                r_cnt = 0 

                while q: 
                    cr,cc = q.popleft() 
                    for dr,dc in ((-1,0),(0,1),(1,0),(0,-1)): 
                        nr,nc = cr + dr, cc + dc 
                        if v[nr][nc] == 0 and (nr,nc) not in group and (board[nr][nc] == color or board[nr][nc] == 0): 
                            q.append((nr,nc)) 
                            group.add((nr,nc)) 

                            if board[nr][nc] == 0: 
                                r_cnt += 1 
                            else: 
                                v[nr][nc] = 1 
                base_r,base_c = get_base(group)
                tlst.append((len(group),r_cnt,base_r,base_c,group))
                if len(tlst)>0: 
                    tlst.sort(key=lambda x: (-x[0],x[1],-x[2],x[3]))
                    mx_group = tlst[0][-1]
    return mx_group
def gravity(): 
    nboard = [x[:] for x in board] 

    for r in range(1,N): 
        for c in range(1,N+1): 
            while M>=board[r][c]>=0 and board[r+1][c] == EMPTY: 
                board[r][c],board[r+1][c] = board[r+1][c],board[r][c] 
                r -= 1 
    board = nboard
    


ans = 0
while True: 
    del_group = bfs() 
    if len(del_group) < 2: 
        break 
    
    ans += len(del_group) ** 2 
    for tr,tc in del_group: 
        board[tr][tc] = EMPTY
    gravity()

    board = list(map(list,zip(*board)))[::-1] 
    gravity()
print(ans)