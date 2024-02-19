n = int(input())

st_a = input()
st_b = input()

# 다같이 움직이는 시계 반대 방향 -> 1 씩 감소
# 독립적으로 움직이는 방향 -> 1 증가

a = " " + st_a
b = " " + st_b

import sys
MAX = sys.maxsize
dp = [[MAX] * 11 for _ in range(n+1)]

dp[0][0] = 0

for i in range(n):
    for j in range(10):
        if dp[i][j] == MAX:
            continue
        
        now = (int(a[i+1]) + j) % 10
        want = int(b[i+1])

        turn = (want - now + 10) % 10
        next = (turn + j) % 10

        dp[i+1][next] = min(dp[i+1][next], dp[i][j] + turn)

        turn = (now - want + 10) % 10
        next = j

        dp[i+1][next] = min(dp[i+1][next], dp[i][j] + turn)



print(min(dp[n]))