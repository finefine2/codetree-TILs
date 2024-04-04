from collections import deque 
N = int(input())
start_r, start_c, end_r, end_c = map(int,input().split()) 
start_r -= 1 
start_c -= 1 
end_r -= 1
end_c -= 1

check = [[0 for _ in range(N)] for _ in range(N)] 
knight = [[-1] * N for _ in range(N)] 
def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

def can_go(r,c): 
    if in_range(r,c) and not check[r][c]: 
        return True 
    
def bfs(): 
    drs, dcs = [1,2,1,2,-1,-2,-1,-2], [2,1,-2,-1,2,1,-2,-1] 

    while q: 
        r,c = q.popleft() 
        for dr,dc in zip(drs,dcs): 
            new_r, new_c = r + dr, c + dc 
            if can_go(new_r,new_c):
                knight[new_r][new_c] = knight[r][c] + 1 
                check[new_r][new_c] = 1 
                q.append((new_r,new_c)) 

q = deque() 
knight[start_r][start_c] = 0 
q.append((start_r,start_c)) 
bfs() 

if check[end_r][end_c] == -1: 
    print(-1) 
else: 
    print(knight[end_r][end_c])