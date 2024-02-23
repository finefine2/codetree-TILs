n, k = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + arr[i-1][j-1]
    # 여기서 dp는 가로방향 부분합을 뜻한다.

ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        s = 0
        for r in range(i - k, i + k + 1):
            c = k - abs(i - r)

            # r,c 는 움직이는 수직, 수평 방향 크기이다.
            if 1<=r<=n:
                s += dp[r][min(j + c, n)] - dp[r][max(j - c - 1, 0)]
        
        ans = max(ans, s)

print(ans)