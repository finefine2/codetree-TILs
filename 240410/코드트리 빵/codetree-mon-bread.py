# U L R D 

from collections import deque 
# U L R D 
dir = [(-1,0),(0,-1),(0,1),(1,0)] 
N,M = map(int,input().split()) 
board = [list(map(int,input().split())) for _ in range(N)] 
customer = {} 
customerlist = [] 

time = 1
while True: 
    # move
    for i in customerlist: 
        if i in customer: 
            visited = [[False] * N for _ in range(N)] 
            visited[customer[i][0]][customer[i][1]] = True 
            q = deque([(customer[i][0], customer[i][1],-1,-1)])

            while q: 
                r,c,dr,dc = q.popleft() 
                if (r,c) == (customer[i][2], customer[i][3]): 
                    customer[i][0], customer[i][1] = dr,dc 

                    # arrive at store 
                    if (dr,dc) == (customer[i][2], customer[i][3]): 
                        board[dr][dc] -= 1 
                        del customer[i]
                    break 
                for j in range(4): 
                    nr,nc = r + dir[j][0], c + dir[j][1] 
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and board[nr][nc] != -1: 
                        visited[nr][nc] = True 
                        if (dr,dc) == (-1,-1): 
                            q.append((nr,nc,nr,nc)) 
                        else: 
                            q.append((nr,nc,dr,dc))
    # number t customer 
    if 0 < time < M+1: 
        visited = [[False] * N for _ in range(N)] 
        a,b = map(int,input().split()) 
        q = deque([(a-1,b-1)])
        visited[a-1][b-1] = True

        while q: 
            r,c = q.popleft() 
            if board[r][c] == 1: 
                board[r][c] = -1 
                customer[time] = [r,c,a-1,b-1] 
                customerlist.append(time) 
                break 
            for i in range(4): 
                nr,nc = r + dir[i][0], c + dir[i][1] 
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and board[nr][nc] != -1: 
                    visited[nr][nc] = True 
                    q.append((nr,nc)) 
    if not customer: 
        print(time) 
        break
    time += 1