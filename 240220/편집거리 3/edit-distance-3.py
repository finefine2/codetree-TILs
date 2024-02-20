ai = input()
bi = input()

aa = len(ai)
bb = len(bi)

a = " " + ai
b = " " + bi

dp = [[0] * (bb + 1) for _ in range(aa + 1)]

for i in range(1, aa + 1):
    dp[i][0] = i
for j in range(1, bb + 1):
    dp[0][j] = j

for i in range(1, aa + 1):
    for j in range(1, bb + 1):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

print(dp[aa][bb])