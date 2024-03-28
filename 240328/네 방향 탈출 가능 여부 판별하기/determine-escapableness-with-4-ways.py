N,M = map(int,input().split()) 

board = [list(map(int,input().split())) for _ in range(N)] 

visited = [[0 for _ in range(M)] for _ in range(N)] 


from collections import deque 

q = deque() 

def in_range(r,c): 
    return 0 <= r < N and 0 <= c < M 

def can_go(r,c): 
    if not in_range(r,c): 
        return False 
    if visited[r][c] or board[r][c] == 0: 
        return False
    return True 
def bfs(): 
    drs,dcs = [1,0,-1,0],[0,1,0,-1] 
    while q: 
        r,c = q.popleft() 
        for dr, dc in zip(drs,dcs): 
            new_r, new_c = r + dr, c + dc 
            if can_go(new_r,new_c): 
                q.append((new_r,new_c))
                visited[new_r][new_c] = 1 

q.append((0,0)) 
visited[0][0] = 1 
bfs() 

print(visited[N-1][M-1])