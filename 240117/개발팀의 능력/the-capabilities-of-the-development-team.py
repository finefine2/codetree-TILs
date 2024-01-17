arr = list(map(int, input().split()))
n = len(arr)

def diff(a, b, c, d):
    
    num = sys.maxsize
    sum1 = abs(arr[a] + arr[b])
    sum2 = abs(arr[c] + arr[d])
    sum3 = sum(arr) - sum1 - sum2 

    Max = abs(sum1 - sum2)
    Max = max(Max, abs(sum2 - sum3))
    Max = max(Max, abs(sum3 - sum1))

    if sum1 == sum2 or sum2 == sum3 or sum3 == sum1:
        return num
    
    return Max

import sys
Min = sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        for k in range(n):
            for l in range(k+1, n):
                if i == k or i == l or j == k or j == l:
                    continue
                Min = min(Min, diff(i, j, k, l))

if Min == sys.maxsize:
    print(-1)
else:
    print(Min)