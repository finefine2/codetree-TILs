n = int(input())

arr = list(map(int, input().split()))

s = sum(arr)
dp = [0] * (s + 1)

dp[0] = 1
for i in range(n):
    for j in range(1, s + 1):
        if j - arr[i] >= 0 and dp[j - arr[i]]:
            dp[j] = 1

import sys
ans = sys.maxsize
for i in range(s + 1):
    if dp[i]:
        ans = min(ans, abs(s - 2 * i))

if ans == 0:
    print("Yes")
else:
    print("No")