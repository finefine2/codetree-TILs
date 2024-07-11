n = int(input())
arr = list(map(int, input().split()))

dp = arr
for i in range(len(arr)):
    dp[i] = max(dp[i-1] + arr[i], arr[i])

print(max(dp))