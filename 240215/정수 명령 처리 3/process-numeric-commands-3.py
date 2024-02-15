from collections import deque
N = int(input()) 
q = deque() 

for _ in range(N): 
    command = list(map(str,input().split())) 
    if command[0] == "push_front": 
        q.appendleft(int(command[1]))
    elif command[0] == "push_back": 
        q.append(int(command[1])) 
    elif command[0] == "pop_front": 
        print(q.popleft())
    elif command[0] == "pop_back": 
        print(q.pop()) 
    elif command[0] == "size": 
        print(len(q))
    elif command[0] == "empty": 
        if not q: 
            print(1) 
        else: 
            print(0) 
    elif command[0] == "front":
        print(q[0]) 
    else: 
        print(q[-1])