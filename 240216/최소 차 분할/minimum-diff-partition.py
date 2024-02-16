n = int(input())

arr = [0] + list(map(int, input().split()))

Max = sum(arr)
dp = [0] * (Max + 1)

dp[0] = True
for i in range(n):
    for j in range(Max, 0, -1):
        if j - arr[i] >= 0 and dp[j - arr[i]]:
            dp[j] = True


ans = 100001
for i in range(1, Max):
    if dp[i]:
        ans = min(ans, abs(Max - 2 * i))

print(ans)
# num = Max - sum(ans)
# print(abs(sum(ans) - num))