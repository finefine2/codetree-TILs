n = int(input())

arr = [0] + list(map(int, input().split()))

Max = sum(arr)
dp = [0] * (Max + 1)

for i in range(1, n+1):
    for j in range(Max, -1, -1):
        if j - arr[i] >= 0:
            dp[j] = True


ans = 100001
for i in range(1, Max):
    if dp[i]:
        ans = min(ans, abs(Max - 2 * i))

print(ans)
# num = Max - sum(ans)
# print(abs(sum(ans) - num))