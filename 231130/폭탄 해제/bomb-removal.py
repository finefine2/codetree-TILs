class Bomb: 
    def __init__(self,code,color,time): 
        self.code = code
        self.color = color 
        self.time = time 

a,b,c = input().split() 
B1 = Bomb(a,b,c) 

print(f"code : {B1.code}")
print(f"color : {B1.color}")
print(f"second : {B1.time}")