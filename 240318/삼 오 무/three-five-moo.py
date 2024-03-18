n = int(input())

import sys
left = 1
right = sys.maxsize
Min = sys.maxsize

while left <= right:
    mid = (left + right) // 2
    cnt = (mid // 3) + (mid // 5) - (mid // 15)

    if mid - cnt < n:
        left = mid + 1
    else:
        right = mid - 1
        Min = min(Min, mid)

print(Min)