n = int(input())

arr = list(map(int, input().split()))

dp = [[0] * 4 for _ in range(n)]

dp[0][0] = 0
for i in range(1, n):
    for j in range(4):
        if i >= 2:  # i에서 두칸 전
            dp[i][j] = max(dp[i][j], dp[i-2][j] + arr[i])
        if j > 0:   # 한칸 건너는 경우이므로 j도 하나 작다 (한칸 건너면 j가 커진다.)
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + arr[i])

# for i in range(n):
#     for j in range(4):
#         print(dp[i][j], end = " ")
#     print()

print(max(dp[n-1]))