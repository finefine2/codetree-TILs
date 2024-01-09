class User:
    def __init__(self, height, weight, num):
        self.height = height
        self.weight = weight
        self.num = num

n = int(input())

user = []
for i in range(n):
    height, weight = tuple(map(int, input().split()))
    user.append(User(height, weight, i+1))

user.sort(key=lambda x: (x.height, -x.weight, x.num))

for i in range(n):
    print(f"{user[i].height} {user[i].weight} {user[i].num}")