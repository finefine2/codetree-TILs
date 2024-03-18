n, m = map(int, input().split())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

left = 1
right = max(arr)
ans = 0

while left <= right:
    mid = (left + right) // 2

    num = 0
    for k in arr:
        num += (k // mid)
    
    if num >= m:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)