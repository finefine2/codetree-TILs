n = int(input())

arr =  [0] + list(map(int, input().split()))

dp = [[0] * 4 for _ in range(n+1)]

dp[0][0] = 0
dp[1][1] = arr[1]
for i in range(2, n+1):
    for j in range(4):

        if j == 0:
            dp[i][j] = dp[i-2][j] + arr[i]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-2][j]) + arr[i]


        # if i >= 2:  # i에서 두칸 전
        
        # if j > 0:   # 한칸 건너는 경우이므로 j도 하나 작다 (한칸 건너면 j가 커진다.)
        #     dp[i][j] = max(dp[i][j], dp[i-1][j-1] + arr[i])

        # # 2계단 오르기, 이전 계단을 밟지 않고 현재만 밟을 때
        # if i >= 2:
        #     dp[i][j] = max(dp[i][j], dp[i-2][j] + arr[i])
        # else:
        #     dp[i][j] = max(dp[i][j], dp[i-1][j] + arr[i], arr[i])
        # 첫번째에서 바로 2계단 오르는 경우
        # if i == 1:
        #     dp[i][j] = max(dp[i][j], arr[i])


ans = 0
# for j in range(4):
#     ans = max(ans, dp[n][j])
print(max(dp[n]))

# print(ans)