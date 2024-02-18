n, m = map(int, input().split())

arr = []
arr.append((0,0,0))
for i in range(n):
    s, e, v = map(int, input().split())
    arr.append((s, e, v))

import sys
MIN = -sys.maxsize
dp = [[MIN] * (n+1) for _ in range(m+1)]

for i in range(1, n+1):
    if arr[i][0] == 1:
        dp[1][i] = 0
# 첫날의 옷을 입는 경우 0

for i in range(2, m+1):
    for j in range(1, n+1):
        # i번째 날에 j번째 옷을 입을 수 있고
        if arr[j][0] <= i <= arr[j][1]:
            # i-1번째 날에 k번째 옷을 입는 경우를 찾는다.
            for k in range(1, n+1):
                # i-1번째 날에 k번째 옷을 입을 수 있어야 한다.
                if arr[k][0] <= i - 1 <= arr[k][1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(arr[j][2] - arr[k][2]))
                    # 이렇게 해서 i날에는 j, i-1날에는 k, 거기다가 j값에서 k값의 절대값 차를 더해준다.
print(max(dp[-1]))