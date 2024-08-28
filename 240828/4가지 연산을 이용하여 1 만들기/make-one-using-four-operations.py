from collections import deque 
N = int(input()) 

calcs = [1,-1,2,3]
visited = [0] * (2*N+1) 
steps = [0] * (2*N+1) 

q = deque() 

def in_range(num): 
    return 1 <= num < 2*N + 1 

def bfs(): 
    q.append(1) 
    visited[1] = 1 
    
    while q: 
        num = q.popleft()
        for i in range(4): 
            if i == 0 or i == 1: 
                next_num = num + calcs[i] 
            else: 
                next_num = num * calcs[i] 
            
            if in_range(next_num) and not visited[next_num]: 
                visited[next_num] = 1 
                steps[next_num] = steps[num] + 1 
                q.append(next_num)
            if next_num == N: 
                print(steps[next_num]) 
                return 
bfs()