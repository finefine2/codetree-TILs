n = int(input())

arr = list(map(int, input().split()))

up = [1] * 1001
down = [1] * 1001

up[0] = 1
down[-1] = 1
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            up[i] = max(up[i], up[j] + 1)

# for i in range(n):
#     print(up[i], end = " ")

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            down[i] = max(down[i], down[j] + 1)

ans = 0
for i in range(n):
    ans = max(ans, up[i] + down[i] - 1)

print(ans)

# print(max(down))
# for i in range(n):
#     print(up[i], end = " ")
# print()
# for i in range(n):
#     print(down[i], end = " ")