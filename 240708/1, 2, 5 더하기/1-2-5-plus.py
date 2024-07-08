import sys
n = int(input())

dp = [0] * 1001

arr = [1, 2, 5]

dp[0] = 1
for i in range(1, n+1):
    for k in arr:
        if i >= k:
            dp[i] += dp[i - k] % 10007

print(dp[n] % 10007)

# 여기에서는 




# n = int(input())

# dp = [0] * 1001

# num = [1, 2, 5]

# dp[0] = 1
# for i in range(1, n+1):
#     for k in num:
#         if i >= k:
#             dp[i] += dp[i - k] % 10007

# print(dp[n] % 10007)

# # for k in range(n+2):
# #     print(dp[k], end = " ")