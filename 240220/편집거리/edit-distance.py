a = input()
b = input()

aa = len(a)
bb = len(b)

dp = [[0] * (bb + 1) for _ in range(aa + 1)]

if a[0] == b[0]:
    dp[0][0] = 0
else:
    dp[0][0] = 1


for i in range(1, aa):
    if a[i] == b[0]:
        dp[i][0] = dp[i-1][0]
    else:
        dp[i][0] = dp[i-1][0] + 1

for i in range(1, bb):
    if a[0] == b[i]:
        dp[0][i] = dp[0][i-1]
    else:
        dp[0][i] = dp[0][i-1] + 1

for i in range(1, aa):
    for j in range(1, bb):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1]
        else:
            if i == j:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

print(dp[aa - 1][bb - 1])