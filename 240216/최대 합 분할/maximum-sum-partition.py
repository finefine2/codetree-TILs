n = int(input())

arr = [0] + list(map(int, input().split()))

Max = sum(arr)
dp = [0] * (Max + 1)

dp[0] = True
for i in range(1, n+1):
    for j in range(Max):
        if j - arr[i] >= 0 and dp[j - arr[i]]:
            dp[j] = True

ans = 0
for i in range(Max + 1):
    if dp[i] and (Max - i) % 2 == 0 and dp[(Max - i) // 2]:
        ans = max(ans, (Max - i) // 2)

print(ans)