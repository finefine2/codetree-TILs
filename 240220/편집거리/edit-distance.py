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
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

# for i in range(aa):
#     for j in range(bb):
#         print(dp[i][j], end = " ")
#     print()

print(dp[aa][bb])


# for i in range(1, aa):
#     if a[i] == b[0]:
#         dp[i][0] = dp[i-1][0]
#     else:
#         dp[i][0] = dp[i-1][0] + 1

# for i in range(1, bb):
#     if a[0] == b[i]:
#         dp[0][i] = dp[0][i-1]
#     else:
#         dp[0][i] = dp[0][i-1] + 1

# for i in range(1, aa):
#     for j in range(1, bb):
#         if a[i] == b[j]:
#             dp[i][j] = dp[i-1][j-1]
#         else:
#             if i == j:
#                 dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
#             else:
#                 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

# for i in range(aa):
#     for j in range(bb):
#         print(dp[i][j], end = " ")
#     print()
# print(dp[aa - 1][bb - 1])