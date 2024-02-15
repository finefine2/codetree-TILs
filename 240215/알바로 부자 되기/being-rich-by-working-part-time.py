n = int(input())

Max = -1
arr = []
for i in range(n):
    s, e, p = map(int, input().split())
    arr.append((s, e, p))
    Max = max(e, Max)

arr.sort(key=lambda x: x[1])

dp = [0] * (n+1)

dp[0] = arr[0][2]
for i in range(1, n):
    for j in range(i):
        s1, e1, p1 = arr[i][0], arr[i][1], arr[i][2]
        s2, e2, p2 = arr[j][0], arr[j][1], arr[j][2]

        if e2 < s1:   # 안겹칠때는 원래의 dp에 cost를 더해준다.
            dp[i] = max(dp[i], dp[j] + p2)
        else:         # 겹치는 경우에는 원래 dp에 새로 p2를 넣어 비교해준다.
            dp[i] = max(dp[i], p2)

ans = max(dp)
print(ans)