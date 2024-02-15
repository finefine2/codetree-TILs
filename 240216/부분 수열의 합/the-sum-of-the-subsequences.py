n, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))

dp = [-1] * (m+1)

dp[0] = 0

# arr의 원소하나에 대해서 각각 dp를 돌아야 하니까 1 ~ n이 바깥에 와야 한다.
for i in range(1, n+1):
    for j in range(m, -1, -1):
        if j >= arr[i]:
            if dp[j - arr[i]] == -1:
                continue
            dp[j] = max(dp[j], dp[j - arr[i]] + 1)

# for i in range(m+1):
#     print(dp[i], end = " ")

if dp[m] == -1:
    print("No")
else:
    print("Yes")