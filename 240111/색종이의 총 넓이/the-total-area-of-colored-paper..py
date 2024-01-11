n = int(input())

arr = [[0] * 200 for _ in range(200)]

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(4):
        for j in range(4):
            arr[i+100][j+100] = 1

ans = 0
for i in range(200):
    for j in range(200):
        if arr[i][j] == 1:
            ans += 8

print(ans)