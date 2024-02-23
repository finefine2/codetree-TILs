import sys

MIN = - sys.maxsize
n = int(input())

# arr = []
# for i in range(n):
#     tmp = list(map(int, input().split()))
#     arr.append(tmp)
arr = [[0] * (n + 1)]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))

pre_sum = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        pre_sum[i][j] = pre_sum[i-1][j] + pre_sum[i][j-1] - pre_sum[i-1][j-1] + arr[i][j]

ans = MIN

for i in range(1, n+1):
    for j in range(i, n+1):  # 수정된 부분
        dp = [0] * (n+1)

        for k in range(1, n+1):
            s = pre_sum[j][k] - pre_sum[i-1][k] - pre_sum[j][k-1] + pre_sum[i-1][k-1]
            dp[k] = max(s, dp[k-1] + s)

        area = MIN
        for k in range(1, n+1):
            area = max(area, dp[k])

        ans = max(ans, area)


print(ans)