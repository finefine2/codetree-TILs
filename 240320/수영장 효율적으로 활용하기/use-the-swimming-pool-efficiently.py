n, m = map(int, input().split())

arr = list(map(int, input().split()))

def find(mid):
    s = 0
    num = 0

    for i in range(n):
        if arr[i] > mid:
            return False
        
        s += arr[i]
        if s > mid:
            num += 1
            s = arr[i]

    return num < m



ans = 100000
left = 1
right = sum(arr)
while left <= right:
    mid = (left + right) // 2
    if find(mid):
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1

print(ans)