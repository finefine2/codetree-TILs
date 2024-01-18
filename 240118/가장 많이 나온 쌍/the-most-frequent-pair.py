n, m = map(int, input().split())

arr = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] += 1
    arr[b][a] += 1

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, arr[i][j])

print(ans)