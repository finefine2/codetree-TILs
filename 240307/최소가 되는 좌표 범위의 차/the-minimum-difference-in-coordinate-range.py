# n, d = map(int, input().split())

# arr = []
# for i in range(n):
#     x, y = map(int, input().split())
#     arr.append((x, y))

# arr.sort(key = lambda x : x[0])

# left = 0
# right = 0

# import sys
# ans = sys.maxsize

# while right < n:
#     MIN = min(arr[left][1], arr[right][1])
#     MAX = max(arr[left][1], arr[right][1])

#     if MAX - MIN >= d:
#         ans = min(ans, arr[right][0] - arr[left][0])
#         left += 1
#     else:
#         right += 1
        
# if ans == sys.maxsize:
#     print(-1)
# else:
#     print(ans)


import math
from sortedcontainers import SortedSet

n, d = map(int, input().split())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr = [(0,0)] + sorted(arr)
point_count = SortedSet()

def get_min():
    if not point_count:
        return 0
    return point_count[0][0]

def get_max():
    if not point_count:
        return 0
    return point_count[-1][0]

ans = math.inf
j = 0

for i in range(1, n+1):
    while j + 1 <= n and get_max() - get_min() < d:
        point_count.add((arr[j+1][1], arr[j+1][0]))
        j += 1

    if get_max() - get_min() < d:
        break

    ans = min(ans, arr[j][0] - arr[i][0])

    point_count.remove((arr[i][1], arr[i][0]))

if ans == math.inf: 
    print(-1)
else: 
    print(ans)