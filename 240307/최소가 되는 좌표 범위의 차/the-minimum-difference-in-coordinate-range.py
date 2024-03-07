n, d = map(int, input().split())

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key = lambda x : x[0])

left = 0
right = 0

import sys
ans = sys.maxsize

while right < n:
    MIN = min(arr[left][1], arr[right][1])
    MAX = max(arr[left][1], arr[right][1])

    if MAX - MIN >= d:
        ans = min(ans, arr[right][0] - arr[left][0])
        left += 1
    else:
        right += 1
        
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)