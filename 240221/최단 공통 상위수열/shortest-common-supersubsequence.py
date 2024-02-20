s = input()
t = input()

ss = len(s)
tt = len(t)

dp = [[0] * (tt + 1) for _ in range(ss + 1)]

for i in range(1, ss + 1):
    for j in range(1, tt + 1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

num = dp[ss][tt]

print(ss + tt - num)