n = int(input())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

arr.sort()

a = arr[0]
b = arr[-1]

import sys
ans = sys.maxsize
num_a = 0
num_b = 0

# 0 부터 100 - 17 까지
for i in range(83):
    num = 0
    for j in range(n):
        if arr[j] < i:
            num += (i - arr[j]) ** 2
        elif arr[j] > i + 17:
            num += (arr[j] - (i + 17)) * (arr[j] - (i + 17))
    
    # i 부터 i + 17 이라고 가정
    # i + 17 보다 높으면 i + k가 되게 깎고
    # i보다 작으면 i가 되게 쌓는다.

    ans = min(ans, num)

print(ans)