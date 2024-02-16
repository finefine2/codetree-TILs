n = int(input())

arr = [0] + list(map(int, input().split()))

# MAX = 10001
dp = [-1] * 10001

dp[0] = 0
for i in range(1, len(dp)):
    for j in range(1, len(arr)):
        if i >= j:
            if dp[i - j] == -1:
                continue
            dp[i] = max(dp[i], dp[i - j] + arr[j])

# for i in range(20):
#     print(dp[i], end = " ")

print(dp[n])