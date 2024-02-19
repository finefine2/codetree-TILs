n, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))

import sys
MIN = -sys.maxsize
dp = [[[MIN for _ in range(5)] for _ in range(m+1)] for _ in range(n+1)]

for k in range(1, 5):
    # k가 arr[1]과 같을 경우 유사도는 1이 되고 아닌 경우에는 0이 된다.
    if k == arr[1]:
        dp[1][0][k] = 1
    else:
        dp[1][0][k] = 0

for i in range(2, n+1):
    for j in range(m+1):
        for k in range(1, 5):
            for l in range(1, 5):
                if l == k:
                    if arr[i] == k:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][l] + 1)
                    else:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][l])
                # i번째에 k를 사용했지만 숫자를 변경하지 않은 경우
                # 숫자 변경이 없기위해서는 l==k이어야 한다.
                # dp[i-1][j][l]에 새롭게 얻은 유사도를 더한다.

                if l != k and j > 0:
                    if arr[i] == k:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][l] + 1)
                    else:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][l])
                # i번째에 k를 사용해서 숫자가 변경된 경우
                # 숫자 변경이 일어나기 위해서는 i!=k여야 한다.
                # 숫자 변경이 되어 총 변경 횟수가 j가 되기 위해서는
                # i-1번째 까지 총 변경 횟수가 j-1이어야 한다.

ans = 0
for j in range(m+1):
    for k in range(1, 5):
        ans = max(ans, dp[n][j][k])

print(ans)