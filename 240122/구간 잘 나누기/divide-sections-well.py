n, m = map(int, input().split())

arr = list(map(int, input().split()))

import sys
MinMax = sys.maxsize

for i in range(n-m+1):
    s = sum(arr[i:i+m])
    MinMax = min(MinMax, max(s, sum(arr[i+m:])))

print(MinMax)