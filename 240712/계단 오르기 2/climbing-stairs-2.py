# # 1 계단 오르는 것은 최대 3번
# # 2계단 올라도 정확히 목적지에 도착해야 한다. 넘으면 안됨
# # 따라서 n이 목적지일 경우에 n-2에 1계단을 다 쓰고도착하였거나, 
# # n-1에 도착하였는데 1계단 오르는 횟수가 남아있으면 된 것이다.
# # 하지만 1 계단 오르는 찬스를 다 안써도 최대가 될 수 있다.

# n = int(input())
# arr = [0] + list(map(int, input().split()))

# dp = [[0] * 4 for _ in range(n + 1)]

# import sys
# MIN = -sys.maxsize

# dp[0][0] = 0
# dp[1][0], dp[1][1], dp[1][2], dp[1][3] = 0, arr[1], MIN, MIN
# dp[2][0], dp[2][1], dp[2][2], dp[2][3] = arr[2], MIN, arr[1] + arr[2], MIN

# for i in range(3, n+1):
#     for j in range(4):
#         dp[i][j] = max(dp[i][j], dp[i-2][j] + arr[i])

#         # 도착한 i,j의 경우에서 j가 0이 아닐 경우 즉 한번이라도 써서 왔을 경우에는 한칸 전의 값을 검사해준다.
#         # 이렇게 하면서 j를 늘려나가는 것이다. 위에는 1칸 움직이는 경우를 고려안했기에
#         if j:
#             dp[i][j] = max(dp[i][j], dp[i-1][j-1] + arr[i])

# ans = max(dp[n])
# print(ans)




n = int(input())

arr =  [0] + list(map(int, input().split()))

import sys
MIN = -sys.maxsize
dp = [[0] * 4 for _ in range(n+1)]

dp[0][0] = 0
dp[1][1] = arr[1]
dp[1][0] = MIN
dp[1][2] = MIN
dp[1][3] = MIN

dp[2][0] = arr[2]
dp[2][2] = arr[1] + arr[2]
dp[2][1] = MIN
dp[2][3] = MIN

for i in range(3, n+1):
    for j in range(4):
        dp[i][j] = max(dp[i][j], dp[i-2][j] + arr[i])
        
        if j:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + arr[i])

        


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

ans = max(dp[n])
print(ans)
# ans = 0
# for j in range(4):
#     ans = max(ans, dp[n][j])
# print(max(dp[n]))

# print(ans)