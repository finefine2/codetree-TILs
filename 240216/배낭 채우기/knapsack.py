n, m = map(int, input().split())

dp = [-1] * (m+1)

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

dp[0] = 0
for i in range(n):
    for j in range(m, -1, -1):
        if j >= arr[i][0]:
            if dp[j - arr[i][0]] == -1:
                continue
            dp[j] = max(dp[j], dp[j - arr[i][0]] + arr[i][1])

# for i in range(m+1):
#     print(dp[i], end = " ")

print(max(dp))