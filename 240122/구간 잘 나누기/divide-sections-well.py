n, m = map(int, input().split())

arr = list(map(int, input().split()))

import sys
MinMax = sys.maxsize

# for i in range(n-m+1):
#     s = sum(arr[i:i+m])
#     MinMax = min(MinMax, max(s, sum(arr[i+m:])))

def find(num):
    s = 0
    div = 1
    for i in range(n):
        if arr[i] > num:
            return False
        if s + arr[i] > num:
            s = 0
            div += 1
        
        s += arr[i]
    if div <= m:
        return True
        

for i in range(1, sum(arr)):
    if find(i):
        print(i)
        break
    # s = 0
    # div = 1
    # for j in range(n):
    #     if arr[j]> i:
    #         continue
    #     if s + arr[j] > i:
    #         s = 0
    #         div += 1
    #     s += arr[i]
    # if div <= m:
    #     print(i)
    #     break

# print(MinMax)