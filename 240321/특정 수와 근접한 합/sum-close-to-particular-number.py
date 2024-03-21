from itertools import combinations

n, s = map(int, input().split())

arr = list(map(int, input().split()))

arr_comb = combinations(arr, n-2)

import sys
Min = sys.maxsize

for k in arr_comb:
    current_sum = sum(k)
    current_diff = abs(current_sum - s)

    if current_diff < Min:
        Min = current_diff

print(Min)