n, k = map(int, input().split())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

ans = 0

for coin in arr[::-1]:
    ans += k // coin
    k %= coin

print(ans)

# dp = [0] * (k+1)

# dp[0] = 1
# arr.sort()

# for i in range(n):
#     for j in range(arr[i], k+1):
#         if j - arr[i] >= 0:
#             dp[j] += dp[j - arr[i]]

# print(dp[k])