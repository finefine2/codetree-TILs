class Person: 
    def __init__(self,name,height,weight): 
        self.name = name 
        self.height = height
        self.weight = weight
n = int(input())

people = [] 
for _ in range(n): 
    n,h,w = input().split() 
    h, w = int(h), int(w) 
    people.append(Person(n,h,w))

people.sort(key = lambda x: x.height) 

for p in people: 
    print(p.name, p.height, p.weight)