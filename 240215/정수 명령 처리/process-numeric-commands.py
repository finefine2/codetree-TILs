class Stack: 
    def __init__(self): 
        self.items = [] 
    def push(self,item): 
        self.items.append(item) 
    def empty(self): 
        return not self.items 
    def size(self): 
        return len(self.items) 
    def pop(self): 
        if self.empty(): 
            raise Exception("Stack is empty") 
        return self.items.pop() 
    def top(self): 
        if self.empty(): 
            raise Exception("Stack is empty")
        return self.items[-1] 
N = int(input()) 
s = Stack() 

for _ in range(N):
    command = input()
    
    if command.startswith("push"):
        x = int(command.split()[1])
        s.push(x)
    elif command.startswith("pop"):
        print(s.pop())
    elif command == "size":
        print(s.size())
    elif command == "empty":
        print(1 if s.empty() else 0)
    else:
        print(s.top())