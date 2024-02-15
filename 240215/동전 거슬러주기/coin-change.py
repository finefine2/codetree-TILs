n, m = map(int, input().split())

arr = list(map(int, input().split()))

dp = [-1] * (m+1)
# dp는 지금까지 선택한 동전의 합이 i라 했을 때 가능한 최대 동전의 개수

# arr.sort()

dp[0] = 0
for i in range(1, m+1):
    for j in range(1, n):
        if i >= arr[j]:
            if dp[i - arr[j]] == -1:
                continue

            dp[i] = max(dp[i], dp[i - arr[j]] + 1)

if dp[m] == -1:
    print(-1)
else:
    print(dp[m])

# for k in dp:
#     print(k, end = " ")