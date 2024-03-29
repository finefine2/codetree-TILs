class User:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
user = []
for i in range(n):
    name, height, weight = tuple(map(str, input().split()))
    user.append(User(name, height, weight))

user.sort(lambda x: (int(x.height), -int(x.weight)))

for i in range(n):
    print(f"{user[i].name} {user[i].height} {user[i].weight}")