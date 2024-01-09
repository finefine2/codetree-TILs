class User:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

user = []
user2 = []
for i in range(5):
    name, height, weight = tuple(map(str, input().split()))
    user.append(User(name, height, weight))
    user2.append(User(name, height, weight))

user.sort(lambda x: -int(x.height))
user2.sort(lambda x: x.name)

print("name")
for i in range(5):
    print(f"{user2[i].name} {user2[i].height} {user2[i].weight}")

print()
print("height")
for i in range(5):
    print(f"{user[i].name} {user[i].height} {user[i].weight}")