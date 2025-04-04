def rotate(board,sr,sc): 
    nboard = [x[:] for x in board] 
    for r in range(3): 
        for c in range(3): 
            nboard[sr+r][sc+c] = board[sr+3-c-1][sc+r] 
    return nboard

from collections import deque 

def bfs(board,v,sr,sc,clr): 
    q = deque() 
    sset = set() 
    cnt = 0 

    q.append((sr,sc)) 
    v[sr][sc] = 1 

    sset.add((sr,sc)) 
    cnt += 1 

    while q: 
        cr,cc = q.popleft() 
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)): 
            nr,nc = cr + dr, cc + dc 
            if 0<=nr<5 and 0<=nc<5 and v[nr][nc] == 0 and board[cr][cc] == board[nr][nc]: 
                q.append((nr,nc)) 
                v[nr][nc] = 1 
                sset.add((nr,nc)) 
                cnt += 1 
    if cnt >= 3: 
        if clr == 1: 
            for r,c in sset: 
                board[r][c] = 0 
        return cnt 
    else: 
        return 0 

def count_clear(board,clr): 
    v = [[0] * 5 for _ in range(5)] 
    cnt = 0 
    for r in range(5): 
        for c in range(5): 
            if v[r][c] == 0: 
                t = bfs(board,v,r,c,clr) 
                cnt += t 
    return cnt 

K,M = map(int,input().split()) 
board = [list(map(int,input().split())) for _ in range(5)] 
treasures = list(map(int,input().split())) 
ans = [] 

for _ in range(K): 
    #[1] start exploration 
    mx_cnt = 0 
    for rot in range(1,4): # rotation -> c -> r 
        for sc in range(3): 
            for sr in range(3): 
                nboard = [x[:] for x in board]
                for _ in range(rot): 
                    nboard = rotate(nboard,sr,sc) 
                
                # count treasures 
                t = count_clear(nboard,0) 
                if mx_cnt < t: 
                    mx_cnt = t 
                    mboard = nboard
    # break condition 
    if mx_cnt == 0: 
        break 

    #[2] continual gain 
    cnt = 0
    board = mboard
    while True: 
        t = count_clear(board,1) 
        if t == 0: 
            break 
        cnt += t 

        for c in range(5): 
            for r in range(4,-1,-1): 
                if board[r][c] == 0: 
                    board[r][c] = treasures.pop(0) 
    ans.append(cnt) 
print(*ans) 