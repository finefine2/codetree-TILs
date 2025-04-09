from collections import deque 

def bfs(sr,sc): 
    q = deque() 
    v =[[0] * N for _ in range(N)] 
    tlst = [] 

    q.append((sr,sc)) 
    v[sr][sc] = 1 
    eat =0 

    while q: 
        cr,cc = q.popleft() 
        if eat == v[cr][cc]: 
            return tlst, eat-1 

        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)): 
            nr,nc = cr + dr, cc + dc 
            if 0<=nr<N and 0<=nc<N and v[nr][nc] == 0 and robot >= board[nr][nc]: 
                q.append((nr,nc)) 
                v[nr][nc] = v[cr][cc]+ 1
                if robot > board[nr][nc] > 0: 
                    tlst.append((nr,nc)) 
                    eat = v[nr][nc] 
    return tlst,eat-1 
N = int(input()) 
board = [list(map(int,input().split())) for _ in range(N)] 

for r in range(N): 
    for c in range(N): 
        if board[r][c] == 9: 
            cr,cc = r,c 
            board[r][c] = 0 

robot = 2 
cnt = ans = 0 

while True: 
    tlst, dist = bfs(cr,cc) 
    if len(tlst) == 0: 
        break 
    tlst.sort(key=lambda x: (x[0],x[1]))
    cr,cc = tlst[0] 

    board[cr][cc] = 0 
    cnt += 1 
    ans += dist 
    if robot == cnt: 
        robot += 1 
        cnt = 0 
print(ans) 