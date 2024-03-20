n = int(input())

arr = list(map(int, input().split()))

import sys
ans = -sys.maxsize
s = 0

for i in range(n):
    if s < 0:
        s = arr[i]
    else:
        s += arr[i]
    
    ans = max(ans, s)



# while idx < n-1:

#     if s + arr[idx] < 0:
#         ans = max(ans, s)
#         idx += 1
#         s = arr[idx]
#         print(ans)
#     else:
#         s += arr[idx]
#         idx += 1
#         ans = max(ans, s)


print(ans)