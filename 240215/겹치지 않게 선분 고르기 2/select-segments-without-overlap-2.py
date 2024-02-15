n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()

dp = [0] * 1001

for i in range(n):
    dp[i] = 1

    for j in range(i):
        ix, iy = arr[i]
        jx, jy = arr[j]

        if jy < ix:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))