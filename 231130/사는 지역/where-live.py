# my solution 

# class Place: 
#     def __init__(self,name,num,region): 
#         self.name = name 
#         self.num = num 
#         self.region = region
         
# n = int(input()) 
# people = []
# for _ in range(n):
#     a,b,c = input().split()
#     people.append(Place(a,b,c))

# idx = 0 
# for i in range(1,n): 
#     if people[idx].name < people[i].name: 
#         idx = i 
# print(f"name {people[idx].name}")
# print(f"addr {people[idx].num}")
# print(f"city {people[idx].region}")


# given 
class Address: 
    def __init__(self,name,address,region): 
        self.name = name 
        self.address = address
        self.region = region 
n = int(input()) 
arr = [input().split() for _ in range(n)] 
people = [Address(name,address,region) for name,address,region in arr]

target_idx = 0 
for i, person in enumerate(people): 
    if person.name > people[target_idx].name: 
        target_idx = i 

print(f"name {people[target_idx].name}")
print(f"addr {people[target_idx].address}")
print(f"city {people[target_idx].region}")