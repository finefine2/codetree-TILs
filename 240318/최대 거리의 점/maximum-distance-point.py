n, m = map(int, input().split())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

arr.sort()

import sys
def find(dist):
    start = -sys.maxsize

    cnt = 0
    for i in range(n):
        if arr[i] >= start + dist:
            start = arr[i]
            cnt += 1
    
    return cnt >= m

left = 1
right = sys.maxsize
ans = 0

while left <= right:
    mid = (left + right) // 2

    if find(mid):   # cnt >= m 일때
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)