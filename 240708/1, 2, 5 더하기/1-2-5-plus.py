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

# dp[i] += dp[i - k]
# 와 같이 i - 1, i - 2, i - 5에서 각각 1, 2, 5를 더해주면 되므로 그 전까지의 경우의 수들을 누적한 값들을 추가해서 더해주는 형식으로 하면 된다.



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