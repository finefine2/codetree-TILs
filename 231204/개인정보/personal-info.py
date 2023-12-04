class Person: 
    def __init__(self, name, height, weight): 
        self.name = name 
        self.height = height
        self.weight = weight

people1 = [] 
people2 = []
for i in range(5): 
    n,h,w = input().split() 

    people1.append(Person(n,int(h),float(w)))
    people2.append(Person(n,int(h),float(w)))

people1.sort(key = lambda x: x.name)
people2.sort(key = lambda x: -x.height)

print("name") 
for p in people1: 
    print(p.name, p.height, round(p.weight,1))
print() 
print("height")
for p in people2: 
    print(p.name, p.height, round(p.weight,1))