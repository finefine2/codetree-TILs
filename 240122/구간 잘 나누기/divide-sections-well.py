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
        # 다음 수를 넣었는데 우리가 생각하는 구간의 최대값을 넘을 경우 새롭게 구역을 나누어준다.
        if s + arr[i] > num:
            s = 0
            div += 1
        
        # 아닌 경우에는 그냥 arr[i]를 넣고 넘어가준다.
        s += arr[i]
    if div <= m:
        return True
    # 모든 조건을 만족하면서 m개만큼 나누었을 경우 되므로 True

# 각각 구간합의 최대가 i일 때 모든 경우를 고려해 보는 것
for i in range(1, sum(arr)):
    if find(i):
        print(i)
        break