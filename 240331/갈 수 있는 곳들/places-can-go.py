from collections import deque 

N, K = map(int,input().split()) 

board = [list(map(int,input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)] 


q = deque() 
def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

def can_go(r,c): 
    if in_range(r,c) and not visited[r][c] and board[r][c] == 0:
        return True
cnt = 0 
def bfs():
    global cnt 
    drs,dcs = [0,1,0,-1],[1,0,-1,0] 

    while q: 
        r,c = q.popleft() 

        for dr, dc in zip(drs,dcs): 
            new_r, new_c = r + dr, c + dc 
            if can_go(new_r,new_c): 
                visited[new_r][new_c] = True 
                cnt += 1 
                r,c = new_r, new_c

for _ in range(K): 
    r,c = map(int,input().split())
    r -= 1 
    c -= 1
    bfs()
print(cnt)