n, k = map(int, input().split())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

arr.sort()

def find(r):
    num = 1
    idx = 0

    for i in range(n):
        if arr[i] - arr[idx] <= 2 * r:
            continue
        else:
            num += 1
            idx = i
    
    return num <= k

left = 0
right = 1000000000
ans = 1000000000

while left <= right:
    mid = (left + right) // 2

    if find(mid):
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1

print(ans)