class User:
    def __init__(self, x, y):
        self.x = x
        self.y = y

n = int(input())

user = []

arr = list(map(int, input().split()))
for i in range(len(arr)):
    user.append(User(arr[i], (i+1)))

user.sort(key=lambda x: x.x)

result = [0] * n

for i in range(n):
    result[user[i].y - 1] = i + 1

print(*result)

# ans = [0 for _ in range(n)]
# for idx, num in enumerate(user):
#     ans[num.index] = idx + 1
# for k in ans:
#     print(k, end = ' ')

# for i in range(n):
#     print(f"{user[i].y}", end = " ")