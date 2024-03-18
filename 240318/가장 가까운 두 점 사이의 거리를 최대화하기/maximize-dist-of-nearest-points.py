n = int(input())

Max = 0
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
    Max = max(Max, b)

arr.sort()
ans = 0

import sys
def find(dist):
    point = -dist

    for start, end in arr:
        if point + dist > end:
            return False

        point = max(start, point + dist)
    
    return True

left = 1
right = Max

while left <= right:
    mid = (left + right) // 2

    if find(mid):
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1
    
print(ans)