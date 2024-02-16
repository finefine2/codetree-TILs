n, m = map(int, input().split())

arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

dp = [-1] * 10001

dp[0] = 0
for i in range(1, m+1):
    for j in range(n):
        if i >= arr[j][0]:
            dp[i] = max(dp[i], dp[i - arr[j][0]] + arr[j][1])


print(max(dp))