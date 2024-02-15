from collections import deque 
Q = deque() 
N = int(input()) 
for i in range(1,N+1): 
    Q.append(i) 

while len(Q) > 1: 
    Q.popleft()
    Q.append(Q[0]) 
    Q.popleft() 
print(Q[0])