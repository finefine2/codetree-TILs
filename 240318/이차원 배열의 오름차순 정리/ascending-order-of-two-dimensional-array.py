n = int(input())
k = int(input())

left = 1
right = min(10 ** 9, n * n)
ans = min(10 ** 9, n * n)

while left <= right:
    mid = (left + right) // 2

    num = 0
    for i in range(1, n+1):
        num += min(mid // i, n)
    
    if num >= k:
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)