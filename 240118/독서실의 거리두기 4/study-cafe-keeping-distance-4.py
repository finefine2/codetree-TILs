n = int(input())

arr = list(input())

def max_dist():
    dist = n
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == '1' and arr[j] == '1':
                dist = min(dist, j-i)
    
    return dist

import sys
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if arr[i] == '0' and arr[j] == '0':
            arr[i] = '1'
            arr[j] = '1'

            ans = max(ans, max_dist())

            arr[i] = '0'
            arr[j] = '0'

print(ans)