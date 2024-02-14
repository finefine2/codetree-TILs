n = int(input())
dp = [[0] * n for _ in range(n)]

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

dp[0][0] = arr[0][0]

for i in range(1, n):
    dp[0][i] = min(dp[0][i-1], arr[0][i])
    dp[i][0] = min(dp[i-1][0], arr[i][0])


for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(max(dp[i][j-1], dp[i-1][j]), arr[i][j])
# 두개의 오른쪽으로 온, 밑으로 온 최솟값들 중에 더 큰 값을 가져와서 min으로 비교한다.

# for i in range(n):
#     for j in range(n):
#         print(dp[i][j], end = " ")
#     print()

print(dp[n-1][n-1])