n, m = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

dp = [[-1] * m for _ in range(n)]

dp[0][0] = 1
for i in range(n):
    for j in range(m):
        for k in range(i):
            for l in range(j):
                if dp[k][l] == -1:
                    continue
                if arr[i][j] > arr[k][l]:
                    dp[i][j] = max(dp[i][j], dp[k][l] + 1)

ans = 0
for i in range(n):
    for j in range(m):
        # print(dp[i][j], end = " ")
        ans = max(ans, dp[i][j])
    # print()

print(ans)