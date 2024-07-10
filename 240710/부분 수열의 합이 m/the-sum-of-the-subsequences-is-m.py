import sys
n, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))

dp = [sys.maxsize] * 10001
dp[0] = 0

for i in range(1, n+1):
    for j in range(m, -1, -1):
        if j - arr[i] >= 0:
            # 그 전의 값이 아직 값이 안 정해져 있으면 그거 사용안하고 넘어간다.
            # if j - arr[i] == sys.maxsize:
            #     continue
            # 값이 있는 경우 그것을 사용해서 값을 min으로 갱신한다.
            dp[j] = min(dp[j - arr[i]] + 1, dp[j])

if dp[m] == sys.maxsize:
    print(-1)
else:
    print(dp[m])





# n, m = map(int, input().split())

# arr = [0] + list(map(int, input().split()))

# import sys
# MAX = sys.maxsize
# dp = [MAX] * (m+1)

# dp[0] = 0
# for i in range(1, n+1):
#     for j in range(m, -1, -1):
#         if j >= arr[i]:
#             if dp[j - arr[i]] == MAX:
#                 continue
#             dp[j] = min(dp[j], dp[j - arr[i]] + 1)

# ans = dp[m]
# if ans == MAX:
#     ans = -1

# print(ans)