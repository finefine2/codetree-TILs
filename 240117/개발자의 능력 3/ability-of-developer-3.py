arr = list(map(int, input().split()))

def diff(i, j, k):
    min1 = arr[i] + arr[j] + arr[k]
    min2 = sum(arr) - min1
    return abs(min1 - min2)

import sys
Min = sys.maxsize
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            Min = min(Min, diff(i, j, k))

print(Min)