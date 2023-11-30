class Place: 
    def __init__(self,name,num,region): 
        self.name = name 
        self.num = num 
        self.region = region
         
n = int(input()) 
people = []
for _ in range(n):
    a,b,c = input().split()
    people.append(Place(a,b,c))

idx = 0 
for i in range(1,n): 
    if people[idx].name < people[i].name: 
        idx = i 
print(f"name {people[idx].name}")
print(f"addr {people[idx].num}")
print(f"city {people[idx].region}")