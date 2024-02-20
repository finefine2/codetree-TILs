# n, m = map(int, input().split())

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# dp = [[0] * (m+1) for _ in range(n+1)]

# for i in range(1, n+1):
#     for j in range(1, m+1):
#         if a[i-1] == b[j-1]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# i, j = n, m
# st = []
# while i > 0 and j > 0:
#     if a[i-1] == b[j-1]:  # 문자가 같은 경우, 해당 문자를 결과에 추가하고 대각선으로 이동
#         st.append(str(a[i-1]))
#         i -= 1
#         j -= 1
#     elif dp[i-1][j] > dp[i][j-1]:  # 위쪽이 더 큰 경우, 위로 이동
#         i -= 1
#     else:  # 왼쪽이 더 큰 경우, 왼쪽으로 이동
#         j -= 1
# #
# print(' '.join(reversed(st)))


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[[] for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:  # 같은 원소를 찾았을 때
            dp[i][j] = dp[i - 1][j - 1] + [a[i - 1]]
        else:  # 같은 원소를 찾지 못했을 때
            # i-1, j와 i, j-1 중 더 긴 수열 또는 사전순으로 더 앞선 수열을 선택
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            elif len(dp[i - 1][j]) < len(dp[i][j - 1]):
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])

print(' '.join(map(str, dp[n][m])))