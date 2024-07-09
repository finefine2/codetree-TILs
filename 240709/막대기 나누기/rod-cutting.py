n = int(input())

arr = list(map(int, input().split()))

dp = [-1] * (n + 1)

dp[0] = 0
for i, num in enumerate(arr):
    for j in range(1, n + 1):
        if j - (i + 1) >= 0:
            dp[j] = max(dp[j], dp[j - i - 1] + num)

print(max(dp))




# n = int(input())

# arr = [0] + list(map(int, input().split()))

# # MAX = 10001
# dp = [-1] * 10001

# dp[0] = 0
# for i in range(1, len(dp)):
#     for j in range(1, len(arr)):
#         if i >= j:
#             if dp[i - j] == -1:
#                 continue
#             dp[i] = max(dp[i], dp[i - j] + arr[j])

# # for i in range(20):
# #     print(dp[i], end = " ")

# print(dp[n])