n, k = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

s = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + arr[i-1][j-1]

ans = 0
for i in range(1, n - k + 2):
    for j in range(1, n - k + 2):
        num = s[i+k-1][j+k-1] - s[i-1][j+k-1] - s[i+k-1][j-1] + s[i-1][j-1]
        ans = max(ans, num)

print(ans)