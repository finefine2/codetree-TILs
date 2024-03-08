import sys

n, k = map(int, input().split())

arr = list(map(int, input().split()))

one = 0

ans = sys.maxsize
left = 0
for right in range(len(arr)):
    if arr[right] == 1:
        one += 1
    
    while one >= k:
        ans = min(ans, right - left + 1)
        if arr[left] == 1:
            one -= 1
        left += 1

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)