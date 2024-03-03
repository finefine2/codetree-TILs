n, s = map(int, input().split())

arr = list(map(int, input().split()))

import sys
ans = sys.maxsize

left, right = 0, 0
sum_total = 0

while True:
    if sum_total >= s:
        ans = min(ans, right - left)
        sum_total -= arr[left]
        left += 1
    elif right == n:
        break
    else:
        sum_total += arr[right]
        right += 1

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)