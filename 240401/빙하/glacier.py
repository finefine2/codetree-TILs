from collections import deque 
N,M = map(int,input().split()) 

board = [list(map(int,input().split())) for _ in range(N)]
def in_range(r,c): 
    return 0<=r<N and 0<=c<M 

drs,dcs = [0,1,0,-1],[1,0,-1,0] 

def bfs(): 
    num = 0 
    while q: 
        r,c = q.popleft() 
        for dr, dc in zip(drs, dcs): 
            new_r,new_c = r + dr, c + dc 
            if in_range(new_r,new_c) and not check[new_r][new_c]: 
                if board[new_r][new_c] == 1: 
                    check[new_r][new_c] = 1 
                    num += 1 
                    board[new_r][new_c] = 0 
                else:
                    check[new_r][new_c] = 1
                    q.append((new_r,new_c))
                    # 0일 경우 계속 탐색해준다.
    return num

last = 0
t = 0
while True:
    t += 1
    q = deque()
    check = [[0] * M for _ in range(N)]
    q.append((0,0))
    cnt = bfs()
    if cnt:
        last = cnt
    else:
        break

print(t - 1, last)