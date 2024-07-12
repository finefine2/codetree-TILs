n = int(input())

red = [0]
blue = [0]
for i in range(2 * n):
    a, b = map(int, input().split())
    red.append(a)
    blue.append(b)

import sys
MIN = -sys.maxsize
dp = [[MIN] * (2 * n + 1) for _ in range(2 * n + 1)]

dp[0][0] = 0
for i in range(1, 2 * n + 1):
    # j는 지금까지 뽑은 빨간색 수를 뜻한다.
    for j in range(i+1):
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + red[i])
            # 따라서 레드를 추가할때는 i-1, j-1
        
        dp[i][j] = max(dp[i][j], dp[i-1][j] + blue[i])

print(dp[2 * n][n])




# n = int(input())

# red = [0]
# blue = [0]
# for i in range(2*n):
#     a, b = map(int, input().split())
#     red.append(a)
#     blue.append(b)

# import sys
# MIN = -sys.maxsize
# dp = [[MIN] * (2*n + 1) for _ in range(2 * n + 1)]

# dp[0][0] = 0
# for i in range(1, 2*n+1):
#     for j in range(i+1):
#         if j > 0:
#             dp[i][j] = max(dp[i][j], dp[i-1][j-1] + red[i])
#         # 빨간색을 더할때 i + 1 j + 1로 해서 n개를 만든다.
#         # 어차피 2*n 번 하므로 n번 되면 끝
        
#         # elif j > 0 and i >= n:
#         #     dp[i][j] = max(dp[i][j], dp[i-1][j-1])
        
#         # if i - j > 0:
#         dp[i][j] = max(dp[i][j], dp[i-1][j] + blue[i])
#         # elif i - j > 0 and i >= n:
#         #     dp[i][j] = max(dp[i][j], dp[i-1][j])


# print(dp[2*n][n])