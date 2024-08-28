# from collections import deque 
# N = int(input()) 

# calcs = [1,-1,2,3]
# visited = [0] * (2*N+1) 
# steps = [0] * (2*N+1) 

# q = deque() 

# def in_range(num): 
#     return 1 <= num < 2*N + 1 

# def bfs(): 
#     q.append(1) 
#     visited[1] = 1 
    
#     while q: 
#         num = q.popleft()
#         for i in range(4): 
#             if i == 0 or i == 1: 
#                 next_num = num + calcs[i] 
#             else: 
#                 next_num = num * calcs[i] 
            
#             if in_range(next_num) and not visited[next_num]: 
#                 visited[next_num] = 1 
#                 steps[next_num] = steps[num] + 1 
#                 q.append(next_num)
#             if next_num == N: 
#                 print(steps[next_num]) 
#                 return 
# bfs()

import sys, enum 
sys.setrecursionlimit(100000) 
operator_num = 4 
INT_MAX = sys.maxsize

class operator(enum.Enum): 
    subtract = 0 
    add = 1 
    div2 = 2 
    div3 = 3 
N = int(input()) 
ans = INT_MAX

def possible(num,op): 
    if op == 0 or op == 1: 
        return True 
    elif op == 2: 
        return num % 2 == 0 
    else: 
        return num % 3 == 0 

def calculate(num,op): 
    if op == 0: 
        return num - 1 
    elif op == 1: 
        return num + 1 
    elif op == 2: 
        return num // 2 
    else: 
        return num // 3
def find_min(num,cnt): 
    global ans 
    if num == 1: 
        ans = min(ans,cnt) 
        return
    if cnt >= N-1: 
        return 
    for i in range(operator_num): 
        if possible(num,i): 
            find_min(calculate(num,i),cnt+1) 
find_min(N,0) 
print(ans)