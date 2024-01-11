n = int(input())

arr = [[0] * 400 for _ in range(400)]

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(8):
        for j in range(8):
            arr[a+i+100][b+j+100] = 1

ans = 0
for i in range(320):
    for j in range(320):
        if arr[i][j] == 1:
            ans += 1

print(ans)