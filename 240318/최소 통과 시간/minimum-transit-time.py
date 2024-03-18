n, m = map(int, input().split())

arr = []
for i in range(m):
    a = int(input())
    arr.append(a)

arr.sort()

left = 1
right = arr[0] * n
ans = 0

while left <= right:
    mid = (left + right) // 2

    num = 0
    for i in range(m):
        num += (mid // arr[i])

    if num >= n:
        if (ans > mid) or ans == 0:
            ans = mid
        right = mid - 1
    else:
        left = mid + 1
    
print(ans)