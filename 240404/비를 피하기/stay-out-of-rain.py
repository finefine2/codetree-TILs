from collections import deque 
N,H,M = map(int,input().split()) 

board = [list(map(int,input().split())) for _ in range(N)] 
'''
0 이동 가능 
1 벽, 이동 불가 
2 사람 있음 
3 비 피하는 공간
'''
def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 
start_pos = [(i,j) for i in range(N) for j in range(N) if board[i][j] == 3]

visited = [[False for _ in range(N)] for _ in range(N)] 
step = [[0 for _ in range(N)] for _ in range(N)] 
def can_go(r,c): 
    if in_range(r,c) and board[r][c] != 1 and not visited[r][c]: 
        return True 
def push(new_r,new_c,new_s): 
    q.append((new_r,new_c)) 
    visited[new_r][new_c] = True 
    step[new_r][new_c] = new_s

q = deque() 

def bfs(): 
    drs, dcs = [1,0,-1,0],[0,1,0,-1] 
    while q: 
        r,c = q.popleft() 

        for dr, dc in zip(drs,dcs): 
            new_r, new_c = r + dr, c + dc 
            if can_go(new_r,new_c): 
                push(new_r,new_c,step[r][c] + 1) 
for r,c in start_pos: 
    push(r,c,0) 
bfs() 
for i in range(N): 
    for j in range(N): 
        if board[i][j] != 2: 
            print(0, end= " ") 
        else: 
            if not visited[i][j]: 
                print(-1, end= " ")
            else: 
                print(step[i][j],end=" ") 
    print()