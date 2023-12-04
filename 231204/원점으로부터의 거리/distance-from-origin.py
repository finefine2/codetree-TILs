N = int(input())

class Dot: 
    def __init__(self,x,y,num): 
        self.x = abs(x) + abs(y) 
        self.num = num

dist = [] 
for i in range(1,N+1): 
    x,y = map(int,input().split()) 
    dist.append(Dot(x,y,i)) 

dist.sort(key=lambda x: x.x)
for d in dist: 
    print(d.num)