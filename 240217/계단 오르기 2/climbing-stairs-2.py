n = int(input())

arr = list(map(int, input().split()))

dp = [[0] * 4 for _ in range(n)]

dp[0][0] = 0

for i in range(1, n):
    for j in range(4):
        # if i >= 2:  # i에서 두칸 전
        
        if j > 0:   # 한칸 건너는 경우이므로 j도 하나 작다 (한칸 건너면 j가 커진다.)
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + arr[i])

        # 2계단 오르기, 이전 계단을 밟지 않고 현재만 밟을 때
        if i > 1:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + arr[i])

        # 첫번째에서 바로 2계단 오르는 경우
        if i == 1:
            dp[i][j] = max(dp[i][j], arr[i])

# for i in range(n):
#     for j in range(4):
#         print(dp[i][j], end = " ")
#     print()

ans = 0
for j in range(4):
    ans = max(ans, dp[n-1][j])

print(ans)