n = int(input())
arr = list(map(int, input().split()))

dp = arr
for i in range(1, len(arr)):
    dp[i] = max(dp[i-1] + arr[i], arr[i])

print(max(dp))



# n = int(input())
# arr = list(map(int, input().split()))

# import sys
# MIN = -sys.maxsize
# dp = [MIN] * (n+1)

# dp[0] = arr[0]
# for i in range(1, n):
#     dp[i] = max(arr[i], dp[i-1] + arr[i])

# print(max(dp))