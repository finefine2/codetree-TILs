n, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))
# coin에 있어서 인덱스로 했기에 이제까지 인덱스 오류였음..

import sys
Max = sys.maxsize
dp = [Max] * (m+1)
# dp는 지금까지 선택한 동전의 합이 i라 했을 때 가능한 최대 동전의 개수

# arr.sort()

dp[0] = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        if i >= arr[j]:
            if dp[i - arr[j]] == Max:
                continue

            dp[i] = min(dp[i], dp[i - arr[j]] + 1)

ans = dp[m]

if ans == Max:
    ans = -1
print(ans)

# for k in dp:
#     print(k, end = " ")