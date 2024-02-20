# # 각 마법석의 숫자는 이전의 숫자보다 작거나 같아야 하며, 모든 마법석의 숫자의 합은 m이 되어야 한다.

# import sys
# MAX = sys.maxsize

# n, m, k = map(int, input().split())

# dp = [[[0 for _ in range(202)] for _ in range(202)] for _ in range(12)]

# for i in range(1, m+1):
#     dp[1][i][i] = 1

# for i in range(1, n):
#     for j in range(1, m+1):
#         for k in range(1, m+1):
#             for l in range(1, k+1):
#                 if j + l > m:
#                     break
#                 dp[i+1][j+1][l] += dp[i][j][k]
#                 dp[i+1][j+1][l] = min(dp[i+1][j+1][l], 10**9 + 1)

# num = 1
# s = m
# # for i in range(n, 0, -1):
# #     while dp[i][s][num] < k:
# #         k -= dp[i][s][num]
# #         num += 1
# #         if num > m:
# #             break

# #     print(num, end = " ")
# #     s -= num

# for i in range(n, 0, -1):
#     while dp[i][s][num] < k: # num이 m을 넘지 않고, dp[i][s][num]이 k보다 작은 경우
#         k -= dp[i][s][num]
#         num += 1
#         if num > m:  # num이 m을 초과하는 경우, 더 이상 유효한 수열을 찾을 수 없음
#             break

#     # if num <= m:
#     print(num, end=" ")
#     s -= num
#     # num = 1  # 다음 반복을 위해 num 초기화

n, m, k = map(int, input().split())

dp = [[[0 for _ in range(205)] for _ in range(205)] for _ in range(15)]

for i in range(1, m + 1):
    dp[1][i][i] = 1

for i in range(1, n):
    for j in range(1, m + 1):
        for l in range(1, m + 1):
            for t in range(1, l + 1):
                if j + t > m:
                    break
                dp[i + 1][j + t][t] += dp[i][j][l]
                dp[i + 1][j + t][t] = min(dp[i + 1][j + t][t], 10 ** 9 + 1)

num = 1
s = m
for i in range(n, 0, -1):
    while dp[i][s][num] < k:
        k -= dp[i][s][num]
        num += 1

    print(num, end=" ")
    s -= num