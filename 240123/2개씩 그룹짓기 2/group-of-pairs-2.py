n = int(input())

arr = list(map(int, input().split()))

arr.sort()

import sys
ans = sys.maxsize

for i in range(n):
    ans = min(ans, arr[i + n] - arr[i])
# 정렬을 하였을때 (큰 수, 작은 수) 배치를 하여야 하므로
# i에서 기준을 넘는 큰 수로 넘어갈 수 있게 n을 더해서 매칭해준다.
# 2 5 7 9 10 15

print(ans)