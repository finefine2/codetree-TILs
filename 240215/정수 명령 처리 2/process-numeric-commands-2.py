from collections import deque 

class Queue: 
    def __init__(self): 
        self.dq = deque() 
    def push(self,item): 
        self.dq.append(item) 
    def empty(self): 
        return not self.dq 
    def size(self): 
        return len(self.dq) 
    def pop(self): 
        if self.empty(): 
            raise Exception("Queue is empty") 
        return self.dq.popleft() 
    def front(self): 
        if self.empty(): 
            raise Exception("Queue is empty") 
        return self.dq[0] 

N = int(input()) 
q = Queue() 

for _ in range(N): 
    command = list(map(str,input().split()))
    if command[0] == 'push': 
        q.push(int(command[1]))
    elif command[0] == 'empty': 
        if q.empty(): 
            print(1)
        else: 
            print(0) 
    elif command[0] == 'size': 
        print(q.size()) 
    elif command[0] == 'pop': 
        print(q.pop())
    elif command[0] == 'front':     
        print(q.front())