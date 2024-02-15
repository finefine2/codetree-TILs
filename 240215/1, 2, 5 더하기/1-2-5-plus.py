n = int(input())

dp = [0] * 1001

num = [1, 2, 5]

dp[0] = 0
dp[1] = 1
for i in range(2, n+2):
    for j in range(3):
        if i >= num[j]:
            dp[i] += dp[i - num[j]] % 10007

print(dp[n+1])

# for k in range(n+2):
#     print(dp[k], end = " ")