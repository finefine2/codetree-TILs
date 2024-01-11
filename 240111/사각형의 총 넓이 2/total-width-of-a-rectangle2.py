n = int(input())

arr = [[0] * (n+200) for _ in range(n+200)]

for i in range(n):
    k = list(map(int, input().split()))
    for i in range(k[0]+100, k[2]+100):
        for j in range(k[1]+100, k[3]+100):
            arr[i][j] += 1

ans = 0
for i in range(n+200):
    for j in range(n+200):
        if arr[i][j] >= 1:
            ans += 1

print(ans)