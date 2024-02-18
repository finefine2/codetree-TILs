n, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))

import sys
MIN = -sys.maxsize
# dp = [[0] * (m+1) for _ in range(n+1)]
dp = [[[0 for _ in range(2)] for _ in range(m+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        dp[i][j][0] = MIN
        dp[i][j][1] = MIN
        # i개의 숫자 중에서 j개의 구간이 선택되었을때 연속 되는 경우, 안되는 경우 모두 최소값으로 논다.

for i in range(n+1):
    dp[i][0][0] = 0
    # 구간이 0개일 때는 일단 다 0

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j][1] = max(dp[i-1][j-1][0] + arr[i], dp[i-1][j][1] + arr[i])
        # 연속되고 있을 경우에 m개의 구간 정하기 전에서 arr을 더하거나 연속되는 경우 거기에다가 arr 똑같이 더하기
        dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1])
        # 연속 안되는 경우에는 그 전에 끝내기

print(max(dp[n][m][0], dp[n][m][1]))