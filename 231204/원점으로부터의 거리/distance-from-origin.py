# my solution using Class
# N = int(input())

# class Dot: 
#     def __init__(self,x,y,num): 
#         self.x = abs(x) + abs(y) 
#         self.num = num

# dist = [] 
# for i in range(1,N+1): 
#     x,y = map(int,input().split()) 
#     dist.append(Dot(x,y,i)) 

# dist.sort(key=lambda x: x.x)
# for d in dist: 
#     print(d.num)

N = int(input()) 
dist = [] 

def get_dist_from_origin(x,y): 
    return abs(x) + abs(y) 

for i in range(n): 
    x,y = map(int,input().split()) 
    dist.append((get_dist_from_origin(x,y), i+1))
dist.sort() 

for _, idx in dist: 
    print(idx)