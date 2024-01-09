class User:
    def __init__(self, x, y, z, num):
        self.x = x
        self.y = y
        self.z = z
        self.num = num

n = int(input())

user = []
for i in range(n):
    x, y = tuple(map(int, input().split()))
    user.append(User(x, y, abs(x) + abs(y), i+1))

user.sort(key=lambda x: x.z)

for i in range(n):
    print(f"{user[i].num}")