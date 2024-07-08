n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

dp = [-1] * (m+1)
dp[0] = 0

# 원소 하나에 대해서 돌고, 그 다음을 돌고 해야 하므로 1, n+1이 밖에 있어야 한다.
for i in range(1, n + 1):
    for j in range(m, -1, -1):
        if j - arr[i] >= 0:
            if dp[j - arr[i]] == -1:
                continue
            dp[j] = max(dp[j - arr[i]] + 1, dp[j])

if dp[m] == -1:
    print("No")
else:
    print("Yes")




# n, m = map(int, input().split())

# arr = [0] + list(map(int, input().split()))

# dp = [-1] * (m+1)

# dp[0] = 0

# # arr의 원소하나에 대해서 각각 dp를 돌아야 하니까 1 ~ n이 바깥에 와야 한다.
# for i in range(1, n+1):
#     for j in range(m, -1, -1):
#         if j >= arr[i]:
#             if dp[j - arr[i]] == -1:
#                 continue
#             dp[j] = max(dp[j], dp[j - arr[i]] + 1)

# # for i in range(m+1):
# #     print(dp[i], end = " ")

# if dp[m] == -1:
#     print("No")
# else:
#     print("Yes")