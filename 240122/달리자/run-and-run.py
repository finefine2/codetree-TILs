n = int(input())

arr = [0] + list(map(int, input().split()))
arr2 = [0] + list(map(int, input().split()))

ans = 0
for i in range(1, n+1):
    if arr[i] > arr2[i]:
        num = arr[i] - arr2[i]
        arr[i+1] += num
        arr[i] -= num
        ans += num
    
print(ans)

# dp = [0] * n

# dp[0] = abs(arr[0] - arr2[0])

# for i in range(1, n):
#     dp[i] = min(dp[i-1] + abs(arr[i] - arr2[i]), dp[i-1] + abs(arr[i-1] - arr2[i]))

# print(dp[-1])

# for k in dp:
#     print(k, end= " ")