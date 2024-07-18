n = int(input())

# T를 총 세번이상 or 연속으로 B를 3번 받으면 해고

MOD = 10 ** 9 + 1
dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(1004)]

# dp[i][j][k] : i번재 날에 T를 j번, B를 연속 k번 받는 경우

dp[1][0][0] = 1
dp[1][1][0] = 1
dp[1][0][1] = 1

for i in range(1, n):
    for j in range(3):
        for k in range(3):
            dp[i+1][j+1][0] = (dp[i+1][j+1][0] + dp[i][j][k]) % MOD
            # T가 나오는 경우 T의 개수를 늘려준다.
            dp[i+1][j][0] = (dp[i+1][j][0] + dp[i][j][k]) % MOD
            # G가 나오는 경우 k=0으로 다시 돌아간다.
            if k + 1 < 1:
                dp[i+1][j][k+1] = (dp[i+1][j][k+1] + dp[i][j][k]) % MOD
            # B가 나오는 경우 원래에서 k를 증가시켜 준다.

ans = 0
for j in range(3):
    for k in range(3):
        ans = (ans + dp[n][j][k]) % MOD

print(ans)




# n = int(input())
# MOD = 10**9 + 7

# dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(1004)]

# # T B G
# dp[1][0][1] = 1
# dp[1][1][0] = 1
# dp[1][0][0] = 1

# # dp[i][j][k] : i번째 날에 T를 j회 받았고, B를 k회 연속 받은 경우
# for i in range(1, n):
#     for j in range(3):
#         for k in range(3):
#             dp[i+1][j+1][0] = (dp[i+1][j+1][0] + dp[i][j][k]) % MOD
#             # T를 받는 경우를 위해서 T의 횟수를 늘려준다.
#             dp[i+1][j][0] = (dp[i+1][j][0] + dp[i][j][k]) % MOD
#             # G를 받는 경우 k를 0으로 리셋한다.
#             dp[i+1][j][k+1] = (dp[i+1][j][k+1] + dp[i][j][k]) % MOD
#             # B를 받는 경우 k를 1 증가시킨다.

# ans = 0
# for j in range(3):
#     for k in range(3):
#         ans = (ans + dp[n][j][k]) % MOD

# print(ans)